## 4. Beginner guide

### Your first line of defence: passphrases, password managers and MFA

Most student accounts are not hacked by geniuses. They are opened with a password that was already leaked somewhere else, or with a code someone was tricked into sharing. Three habits fix most of that: a long passphrase, a password manager, and a second login step. This guide explains each in plain words.

### Why passwords fail

When a website is breached, the stolen email and password pairs get sold and tried on other sites by automated bots. This is called credential stuffing, and it works because people reuse passwords. A strong password does not help if you used it twice and one site leaked it. Another attack, brute force, simply guesses many passwords; short and predictable ones fall first. So you need passwords that are both long and unique.

### Passphrases: long beats clever

For years we were told to add a capital letter, a number and a symbol. Current guidance from NIST, the US standards body, moves away from that. It says systems should not force these mixes, and it puts length first: at least 15 characters when a password is your only protection, and at least 8 if it is only one part of multi-factor login. India's CERT-In advises at least 12 characters and unique passwords.

A passphrase is the easy way to get length. Pick five or six random, unrelated words, for example from a dice-based word list, and join them. It is long, hard to guess, and far easier to remember than Hostel@2026. The key word is random. A song lyric, a quote or "my dog's name plus my birth year" is guessable. Never use a phrase from this guide as your real password.

### Password managers: one memory, many passwords

You cannot memorise forty unique passphrases, and you should not try. A password manager creates a random password for each site, stores it encrypted, and fills it in for you. You remember only one strong master passphrase.

Reputable managers use zero-knowledge design. For example, Bitwarden's documentation says your vault is encrypted on your device and the company cannot read it. The flip side: if you forget the master passphrase, the company cannot recover it, so set up emergency access or recovery options and practise unlocking the vault. Turn on two-step login for the manager itself, so a leaked master passphrase alone is not enough. Paste and autofill are supported and recommended by NIST, so do not let a site talk you out of pasting.

### MFA: a second lock on the door

Multi-factor authentication asks for something besides your password, such as a code or a device. If your password leaks, the attacker is still stopped. CISA says any MFA is better than none, but not all MFA is equal.

**SMS codes.** A text message with a six-digit code. Easy and familiar, but a fake website can trick you into typing the code, and NIST's guidance notes that SMS and one-time codes can be phished. Use it only when nothing better is offered.

**Authenticator apps.** An app on your phone generates a changing code. It works without mobile network, and it is stronger than SMS. A convincing fake site can still collect the code, so check the web address before typing it.

**Security keys and passkeys.** These use the FIDO/WebAuthn standard. The device proves your identity only to the real website, so a look-alike page gets nothing. CISA calls this phishing-resistant and the gold standard. Keys cost money, but many phones and laptops now support passkeys at no extra cost.

### Three myths to drop

**"I change my password every month, so I'm safe."** NIST now advises against forced scheduled changes. Swapping Hostel@2026 for Hostel@2027 adds almost nothing. Change a password when there is a reason: a breach alert, a suspicious login, or the discovery that you reused it.

**"Nobody wants my account."** Attackers do not choose victims by hand. Bots try leaked passwords everywhere, and a taken-over account is used to scam your friends and family.

**"Complex means safe, so reuse is fine."** Reuse beats complexity every time. If one site leaks a complex password, every site that shares it is exposed.

### Rules that stop most attacks

Never share an OTP, even with someone who says they are from your bank or college. Approve only logins you started. Save your recovery codes offline, in a safe place away from your phone. Secure your email first, because it can reset every other account.

### Your first thirty minutes

1. Install a password manager and create a master passphrase.
2. Set a new passphrase on your main email and turn on MFA.
3. Add MFA to your college portal and payment apps.
4. Write down recovery codes and lock them away.

Then repeat one small habit each week. Security grows from routine, not from one heroic afternoon.
