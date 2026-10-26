#!/usr/bin/env python3
"""
Password entropy demo - DUMMY DATA ONLY.

ETHICS: Never type or paste a real password into this tool or any other
calculator. This script only analyses the made-up strings listed in DEMO_PASSWORDS.

What it shows:
  1. "Naive" entropy (length x character pool) - what many strength meters imply.
  2. "Realistic" entropy - what an attacker's guess list actually faces. Human-made
     patterns like Hostel@2026 are guessed far sooner than the naive number says.
  3. Why random passphrases (several random words) are strong AND memorable.

Assumptions (illustrative, not measurements):
  - Offline attack speed: 1e10 guesses/second against a fast hash. Real speed depends
    heavily on how the site stores passwords (slow salted hashes are far slower).
  - A common-password list of ~100,000 entries is tried first  -> ~16.6 bits.
  - A "common word + decoration" pattern is capped at 30 bits (attacker rules/mangling).

Usage:
  python3 entropy_demo.py                 # run the demo, writes entropy_results.csv
  python3 entropy_demo.py --wordlist F    # use a real word list file (one word per line),
                                          # e.g. the EFF large list (7776 words)
"""
import argparse
import csv
import math
import re
import secrets
import string

GUESSES_PER_SEC = 1e10
BLOCKLIST_BITS = math.log2(100_000)   # ~16.6 bits
PATTERN_CAP_BITS = 30.0

# Tiny dummy blocklist. Real services use lists with millions of breached passwords.
COMMON_FULL = {"password", "123456", "12345678", "qwerty", "111111", "letmein",
               "iloveyou", "admin", "welcome", "abc123", "pass@123", "password@123"}
COMMON_WORDS = ["password", "welcome", "qwerty", "letmein", "iloveyou", "admin",
                "hostel", "college", "cricket", "india", "student", "pass", "troubad"]
LEET = {"@": "a", "4": "a", "3": "e", "1": "i", "!": "i", "0": "o", "$": "s", "5": "s", "7": "t"}

# Made-up examples. None of these is a real password.
DEMO_PASSWORDS = [
    "Pass@123",
    "Hostel@2026",
    "Welcome1!",
    "Tr0ub4dor&3",
    "k7#Qm2$vL9xP",         # dummy 12-char random-looking string
]

# 64 dummy words (6 bits each) - deliberately tiny so the demo runs anywhere.
DEMO_WORDS = ("amber anchor apple basil bridge cactus candle canyon cedar cloud copper coral "
              "daisy delta ember fable falcon fern flint garnet ginger harbor hazel indigo "
              "iris jasper kettle lemon lotus maple marble meadow mint nectar olive onyx "
              "orchid pearl pepper pine plum quartz raven river saffron sage silver spruce "
              "sunset thistle tulip umber velvet violet walnut willow yarrow zephyr zinc "
              "acorn birch comet dune ash").split()
assert len(DEMO_WORDS) == len(set(DEMO_WORDS)) == 64, len(DEMO_WORDS)


def pool_size(pw: str) -> int:
    pool = 0
    if re.search(r"[a-z]", pw): pool += 26
    if re.search(r"[A-Z]", pw): pool += 26
    if re.search(r"[0-9]", pw): pool += 10
    if re.search(r"[^A-Za-z0-9]", pw): pool += 32
    return pool


def naive_bits(pw: str) -> float:
    return len(pw) * math.log2(pool_size(pw))


def realistic_bits(pw: str):
    """Return (bits, reason). Deliberately simple - real tools (e.g. zxcvbn) do far more."""
    low = pw.lower()
    if low in COMMON_FULL:
        return BLOCKLIST_BITS, "on blocklist"
    core = re.sub(r"[^a-z]", "", low.translate(str.maketrans(LEET)))
    if any(w in core for w in COMMON_WORDS):
        return min(naive_bits(pw), PATTERN_CAP_BITS), "common word + decoration"
    return naive_bits(pw), "no pattern found (random-looking)"


def human_time(seconds: float) -> str:
    if seconds < 1: return "under a second"
    units = [("year", 31_557_600), ("day", 86_400), ("hour", 3_600), ("minute", 60), ("second", 1)]
    for name, size in units:
        if seconds >= size:
            n = seconds / size
            if name == "year" and n > 1e9: return f"{n:.1e} years"
            return f"{n:,.0f} {name}s" if n >= 2 else f"{n:.1f} {name}"
    return "under a second"


def avg_crack_time(bits: float) -> str:
    return human_time((2 ** (bits - 1)) / GUESSES_PER_SEC)


def random_password(n=16) -> str:
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(secrets.choice(alphabet) for _ in range(n))


def passphrase(words, n) -> str:
    return "-".join(secrets.choice(words) for _ in range(n))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--wordlist", help="optional word list file, one word per line")
    args = ap.parse_args()

    words = DEMO_WORDS
    if args.wordlist:
        with open(args.wordlist, encoding="utf-8") as f:
            words = [w.split()[-1] for w in f if w.strip()]
    bits_per_word = math.log2(len(words))

    rows = []
    for pw in DEMO_PASSWORDS:
        nb = naive_bits(pw)
        rb, why = realistic_bits(pw)
        rows.append([pw, len(pw), round(nb, 1), round(rb, 1), why, avg_crack_time(rb)])

    rp = random_password(16)
    rows.append([rp + "  (generated now)", len(rp), round(naive_bits(rp), 1),
                 round(naive_bits(rp), 1), "truly random", avg_crack_time(naive_bits(rp))])

    for n in (4, 6):
        pp = passphrase(words, n)
        b = n * bits_per_word
        rows.append([pp + f"  ({n} words, {len(words)}-word list)", len(pp), "-", round(b, 1),
                     "random words", avg_crack_time(b)])

    # Theory rows using the standard 7776-word dice list (no list needed to compute this)
    for n in (4, 5, 6, 7):
        b = n * math.log2(7776)
        rows.append([f"(theory) {n} random words from a 7776-word list", "-", "-", round(b, 1),
                     "random words", avg_crack_time(b)])

    header = ["password (DUMMY)", "length", "naive_bits", "realistic_bits", "reason", "avg_time_at_1e10_guesses_per_s"]
    print(f"Assumed attacker speed: {GUESSES_PER_SEC:.0e} guesses/second (offline, fast hash) - illustrative only\n")
    w = [62, 8, 12, 16, 30, 32]
    print("".join(h.ljust(x) for h, x in zip(header, w)))
    print("-" * sum(w))
    for r in rows:
        print("".join(str(c)[:x - 1].ljust(x) for c, x in zip(r, w)))

    with open("entropy_results.csv", "w", newline="", encoding="utf-8") as f:
        csv.writer(f).writerows([header] + rows)
    print("\nWrote entropy_results.csv (import into Google Sheets to chart it).")
    print("Lesson: naive_bits flatters human patterns; random length (passphrases) wins.")
    print(f"Note: your current word list has {len(words)} words = {bits_per_word:.1f} bits/word; "
          "use a 7776-word list for real passphrases.")


if __name__ == "__main__":
    main()
