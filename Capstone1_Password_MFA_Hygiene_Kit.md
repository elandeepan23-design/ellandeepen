# Password & MFA Hygiene Kit – Capstone 1

26 Oct 2026

A habit-building kit for first-year hostel residents in India: why accounts get taken over, and the few habits that stop it.

## 1. Research report

**Audience:** first-year hostel residents in India. They share Wi-Fi, lab PCs and phones, reuse one password for everything, and sign up for many new portals in the first month.

**Finding:** student accounts are mostly lost through reused passwords and phished codes, not clever hacking. Unique long passphrases in a password manager, plus MFA (ideally phishing-resistant), close most of that gap.

### How accounts get taken

| Attack | How it works | What stops it |
| --- | --- | --- |
| Credential stuffing | Bots replay username–password pairs leaked from one breach against other sites. OWASP treats it as a subset of brute force, but the attacker already holds real passwords. | A unique password per site, MFA, breached-password screening |
| Brute force | Many guesses against one account. Weak, short passwords fall first. | Long passwords, rate limiting and lockout |
| Password spraying | One common password tried across many accounts, staying under lockout limits. | Banning common passwords, lockout |
| Password reuse | Not an attack but the habit that powers stuffing: a strong password still fails if it was exposed once and reused. | Password manager, unique passwords |
| Phishing of codes | A fake login page captures the password and the OTP and replays both. | Phishing-resistant MFA (security keys, passkeys), checking the URL |

### What the authorities say

- **NIST SP 800-63B Rev. 4 (final, July 2025):** minimum 15 characters when the password is the only factor, 8 when it is one part of MFA; accept at least 64 characters; no forced mixes of symbols or case; no scheduled changes (change only after suspected compromise); screen new passwords against a blocklist; allow paste and password managers.
- **CERT-In:** after a large credential leak it advised changing passwords on key accounts, using unique passwords of at least 12 characters, enabling MFA and moving to passkeys. It also says to change passwords regularly, which NIST now advises against. The kit follows NIST here (see the verification report).
- **CISA:** any MFA beats none, but phishing-resistant MFA is the gold standard. FIDO/WebAuthn (security keys and passkeys) is the widely available form.
- **NIST small-business fact sheet:** SMS codes and one-time PINs can be phished.
- **Password-manager documentation (Bitwarden):** zero-knowledge design means the company cannot read or recover your vault; a forgotten master password means a locked vault unless you set up emergency access. Two-step login protects the vault even if the master password leaks.

### MFA methods compared

| Method | Phishing-resistant? | Works without mobile network? | Student verdict |
| --- | --- | --- | --- |
| SMS OTP | No | No | Better than nothing; use only where nothing else exists |
| Authenticator app (TOTP) | No, a fake site can still collect the code | Yes | The sensible default for most accounts |
| Security key / passkey (FIDO2) | Yes | Yes | Best for email and your password-manager vault |

### Design decisions for the programme

1. Fix email first: it resets every other account.
2. Teach passphrases and a password manager together, so reuse stops without memorising 40 passwords.
3. Teach the OTP rule as a social rule: nobody legitimate ever asks for your OTP.
4. Move people up the MFA ladder in steps: SMS, then authenticator app, then passkey or key.
5. Practise with dummy accounts only; no real password is ever typed into a demo or tool.

**Limits:** the research used web search plus secondary summaries of NIST and CERT-In; the primary NIST text and the CERT-In advisory page should be opened and quoted by the student before submission (listed in the verification report).

## 2. Habit checklist

Tick one block per week. Each item takes about ten minutes.

### Week 1: set up (one time)

- [ ] Pick one password manager and install it on your phone and laptop (a reputable free option exists; read its security page first).
- [ ] Create a master passphrase of 5–6 random words (15+ characters). Memorise it; do not store it in chat or Notes.
- [ ] Give your main email its own unique passphrase and turn on MFA. Email resets every other account.
- [ ] Turn on MFA for: college portal, UPI/banking apps, Google/Apple account, social media, cloud storage.
- [ ] Write down your recovery codes and keep them in a locked drawer, not in a chat or shared device.
- [ ] Set a screen-lock PIN on your phone; your phone is now a security factor.

### Every week

- [ ] Deny any login approval you did not start, then change that account's password.
- [ ] Install phone and laptop updates.
- [ ] On shared hostel or lab PCs: private window, no "remember me", sign out when done.
- [ ] Pick the next weekly reminder from the 12-week list and do it.

### Every month

- [ ] Open the manager's reuse and weak-password report; fix the three most important accounts.
- [ ] Delete accounts you no longer use.
- [ ] Move one account up the MFA ladder: SMS, then authenticator app, then passkey or security key.
- [ ] Check your own email on the official Have I Been Pwned site. Enter only your email address, never a password.

### After a breach alert

- [ ] Change that site's password, and every other site where you used it.
- [ ] Sign out of all sessions and review recovery email and phone.
- [ ] Watch for phishing messages that mention the breached service.

### Never

- [ ] Never share an OTP, a recovery code or a master passphrase, with anyone.
- [ ] Never reuse a password.
- [ ] Never send passwords over WhatsApp, email or screenshots.
- [ ] Never approve a prompt you did not trigger.

**On changing passwords on a schedule:** NIST advises against forced periodic changes; change a password when it may be compromised or reused. CERT-In's advisory says to change regularly. This kit follows NIST and keeps changes event-driven, a decision recorded in the verification report.

## 3. Scenarios

### 1. The reused password

**Situation:** you get a breach alert for an old shopping site. You use the same password for your email.

**Safe response:** change the email password first, then the shop's, then every other site that shared it. Turn on MFA on email. Move each new password into the manager.

**Why:** credential stuffing replays leaked passwords on other sites; a strong password still fails once reused.

### 2. The shared OTP

**Situation:** a caller says they are from your bank or the scholarship office and reads out your name. They ask for the OTP "to stop a payment".

**Safe response:** do not share it. Hang up and call the number printed on your card or the official website. An OTP is a key to your account; real staff never need it.

**Why:** a code you read out lets the attacker finish a login or payment you did not start.

### 3. The approval you did not start

**Situation:** at 2 a.m. your phone shows "Approve sign-in?" five times in a row.

**Safe response:** tap Deny, change that account's password now, and sign out other sessions. Do not approve "just to make it stop".

**Why:** attackers who already know your password spam prompts hoping you tap Approve. CERT-In advises approving only requests you made.

### 4. The shared lab PC

**Situation:** you log into email on a lab computer, class ends in a rush, and the browser asks to save the password.

**Safe response:** use a private window, choose Never save, and sign out and close the window. If you forgot, sign out remotely from your account's device list and change the password.

**Why:** a saved session or password gives the next user your account.

### 5. The lost phone

**Situation:** your phone with the authenticator app is stolen. You can't get the codes.

**Safe response:** get a new SIM and phone, restore the authenticator from a backup, or use your saved recovery codes to log in. Then reset MFA and passwords for email first. Ask your carrier to block the old SIM.

**Why:** recovery codes are the planned way back in. That is why they live offline, separate from the phone.

### 6. The fake college login

**Situation:** a message says "hostel Wi-Fi password expired, log in here" and links to a page that looks like the college portal.

**Safe response:** don't enter anything. Open the portal by typing its address or using a saved bookmark. Report the message to your hostel IT desk. If you did enter a password, change it and report to CERT-In at incident@cert-in.org.in.

**Why:** fake pages capture passwords and SMS/app codes. Only phishing-resistant keys and passkeys refuse to work on the wrong site.

## 4. Beginner guide

(See also the standalone file 05_extras/beginner_guide_800_words.md, which is the same text.)

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

## 5. Quiz and answer key

Ten multiple-choice questions. Answers and one-line reasons are in the key below.

1. Credential stuffing is best described as:
   - A. Guessing every possible password on one account
   - B. Automated login attempts using username–password pairs leaked from another site
   - C. Tricking a user into opening a fake page
   - D. Stealing a phone
2. Which habit most directly defeats credential stuffing?
   - A. A password with 3 symbols
   - B. Changing your password every month
   - C. A unique password on every site
   - D. Hiding your username
3. Under current NIST SP 800-63B guidance, a website should:
   - A. Force at least one symbol and one capital letter
   - B. Not require forced character mixes, and screen new passwords against a blocklist
   - C. Force a password change every 30 days
   - D. Limit passwords to 12 characters
4. Which MFA method is described by CISA as phishing-resistant?
   - A. SMS code
   - B. Emailed code
   - C. Authenticator app code
   - D. FIDO/WebAuthn security key or passkey
5. A caller claiming to be from your bank asks for the OTP you just received. You should:
   - A. Read it out to prove your identity
   - B. Hang up and call the number on your card or the bank's official site
   - C. Share only the last three digits
   - D. Ask them to text it to you instead
6. Which is a better passphrase approach?
   - A. Hostel@2026
   - B. Your favourite song lyric
   - C. Five or six random, unrelated words
   - D. Your name and birth year
7. You forget the master passphrase of a zero-knowledge password manager. What is true?
   - A. The company can read your vault and email it to you
   - B. The company cannot recover it, so you need emergency access or a recovery option you set up earlier
   - C. Support can reset it with your date of birth
   - D. The vault becomes unprotected
8. Your phone shows five login approvals you did not start. You should:
   - A. Approve one to stop the noise
   - B. Ignore them
   - C. Deny them, change the account password and sign out other sessions
   - D. Restart the phone
9. Which statement about SMS and authenticator-app codes is correct?
   - A. Both can be collected by a convincing fake website
   - B. Both are immune to phishing
   - C. SMS is phishing-resistant, apps are not
   - D. Apps stop working without mobile data
10. Where should recovery codes be stored?
    - A. In a WhatsApp chat to yourself
    - B. In a screenshot on the phone that holds the authenticator
    - C. Offline in a safe place, separate from your phone
    - D. In a shared hostel group

### Answer key

| Q | Answer | Why |
| --- | --- | --- |
| 1 | B | Stuffing replays real leaked pairs on other sites. |
| 2 | C | Unique passwords mean a leak elsewhere gives nothing. |
| 3 | B | NIST drops composition rules and adds blocklist screening. |
| 4 | D | CISA: FIDO/WebAuthn is the widely available phishing-resistant MFA. |
| 5 | B | Real staff never need your OTP; call back on an official number. |
| 6 | C | Length and randomness make passphrases strong and memorable. |
| 7 | B | Zero-knowledge design means the vendor cannot recover the master passphrase. |
| 8 | C | Prompt spam is a sign the password is known; deny and secure the account. |
| 9 | A | Both SMS and app codes can be typed into a fake site. |
| 10 | C | Recovery codes are the way back in, so keep them offline and apart from the phone. |

## 6. Python entropy demo and automation

**Entropy demo.** `entropy_demo.py` (in 04_python) runs on made-up strings only. It compares a naive estimate (length × character pool) with a realistic one that accounts for blocklists and common-word patterns, and it generates a random password and passphrases on the spot. Assumed attacker speed: 10 billion guesses per second against a fast hash. That figure is illustrative; slow salted hashing makes real cracking much slower.

| Dummy password | Naive bits | Realistic bits | Average guess time |
| --- | --- | --- | --- |
| Pass@123 | 52.4 | 16.6 (on blocklist) | under a second |
| Hostel@2026 | 72.1 | 30.0 (common word + decoration) | under a second |
| Welcome1! | 59.0 | 30.0 | under a second |
| k7#Qm2$vL9xP (random-looking) | 78.7 | 78.7 | about 754,000 years |
| 16 random characters | 104.9 | 104.9 | astronomically long |
| 4 random words, 7776-word list | – | 51.7 | about 2 days |
| 5 random words | – | 64.6 | about 45 years |
| 6 random words | – | 77.5 | about 350,000 years |

**Lessons from the run:**

- The naive score flatters human patterns: Hostel@2026 "scores" 72 bits but falls in seconds because attackers guess common words with decorations first.
- Words are random only if chosen randomly from a big list. The demo's own 64-word list gives just 6 bits per word, so six words is only 36 bits. Use a 7776-word dice list for real passphrases.
- Six random words from a 7776-word list is about 77.5 bits: strong and memorable.

**Automation.** `weekly_reminder.py` turns the checklist into a 12-week reminder set (`weekly_reminders.md`) and prints this week's tip. To run it without code, paste each weekly text into a repeating calendar event, or use a free Make or Notion automation that posts it to the hostel group every Monday. Nothing in it touches real accounts.

**Google Sheets:** import `entropy_results.csv` and chart the realistic-bits column.

## 7. Verification report

**Method:** claims in the report, guide, quiz and scenarios were checked against pages retrieved by web search in this session (Claude with web search). Status key: Verified = primary source seen; Corroborated = several secondary sources agree, primary not opened; Conflict = sources disagree.

| # | Claim used | Source type | Status | Note |
| --- | --- | --- | --- | --- |
| 1 | NIST SP 800-63B Rev. 4: 15 characters minimum if password is the only factor, 8 if part of MFA | Four secondary pages agree (Rev. 4 final, July 2025) | Corroborated | Two older or simplified pages say "minimum 8"; that is the MFA case or Rev. 3. Open NIST §3.1.1.2 to confirm before submitting |
| 2 | No composition rules, no forced periodic change, blocklist screening, accept 64+ characters, allow paste | Many secondary pages agree | Corroborated | Consistent across all pages checked |
| 3 | CERT-In advised unique passwords of 12+ characters, MFA, passkeys | News report of a June 23 advisory after a large credential leak | Corroborated | Advisory year not shown in the snippet; check cert-in.org.in |
| 4 | CERT-In: change passwords regularly | Same news report | Conflict | NIST advises against scheduled changes. Kit follows NIST (change on compromise or reuse) and tells students why |
| 5 | CERT-In: composition of letters, numbers and symbols | Same news report | Conflict | NIST drops composition rules. Kit says "long and unique", does not require symbols |
| 6 | CERT-In: approve only logins you made, keep recovery codes safe, report to incident@cert-in.org.in | Secondary news summary | Corroborated | Confirm the address on the official site before printing it in a poster |
| 7 | CISA: phishing-resistant MFA is the gold standard; FIDO/WebAuthn is the widely available form | CISA statements quoted by trade press; archived CISA pages | Corroborated | Open the current CISA "Implementing phishing-resistant MFA" page for the final citation |
| 8 | SMS codes and one-time PINs can be phished | NIST fact sheet (nist.gov, Feb 2024) | Verified | Primary NIST document |
| 9 | Authenticator-app codes can also be phished | CISA-related reporting; consistent with the above | Corroborated | Kit words it as "a fake site can still collect the code" |
| 10 | OWASP treats credential stuffing as a subset of brute force | Vendor pages quoting OWASP | Corroborated | Check OWASP's own page |
| 11 | Bitwarden: zero-knowledge, vault encrypted on device, master passphrase unrecoverable, two-step login supported | Bitwarden security white paper | Verified | Primary documentation; other managers differ, so students should read their chosen vendor's page |
| 12 | Entropy and crack-time numbers | Python script, reproducible | Verified | Crack times depend on an assumed 10 billion guesses per second; labelled illustrative |

### Claims deliberately left out

- "MFA makes you 99% less likely to be hacked": a campaign quote with no study attached.
- "51% of passwords are reused" and similar percentages: old, second-hand figures.
- Any article about NIST from 2017–2019: they describe the older 8-character rule.

### Unsafe or outdated advice screened out

The draft was checked for these common errors: mandatory symbols, 90-day rotation, "SMS is enough", recovery codes kept in a notes app or chat, real-looking example passwords, and "read the OTP to support". None remain; the before/after section shows each.

### Student to-do before submission

- [ ] Open the NIST SP 800-63B Rev. 4 text and quote §3.1.1.2 (length) and the periodic-change rule.
- [ ] Open the CERT-In advisory and record its year and exact wording.
- [ ] Re-run the same research prompt in a second AI tool (e.g. Perplexity or Gemini) and note any claims that differ.
- [ ] Add your own findings to the table above.

## 8. Prompt library and tool log

**Used in this project:** Claude (with web search; drafting, checking, building files), Python (entropy demo and reminder script), Google Sheets (CSV import, optional). **To add yourself** so the project meets the four-free-AI-tool rule: Perplexity or Gemini (cross-check research), NotebookLM (summarise the source PDFs), Leonardo.ai or Gamma (visuals and slides), Make or Notion (reminder automation). The prompts below work in any of them.

| # | Purpose | Prompt | What to check |
| --- | --- | --- | --- |
| P1 | Scope the project | "I'm building a password and MFA habit kit for first-year hostel residents in India. List the 8 habits that matter most, and tag each as one-time, weekly or monthly. Cite NIST SP 800-63B, CISA or CERT-In for each." | Every tag has a real citation |
| P2 | Research (used) | Searches run: "NIST SP 800-63B password guidelines length blocklist no composition rules"; "CERT-In password security guidelines multi-factor authentication advisory"; "CISA more than a password multi-factor authentication phishing-resistant FIDO"; "OWASP credential stuffing password reuse brute force attack explained"; "Bitwarden security whitepaper zero-knowledge encryption master password" | Prefer .gov and vendor primary pages |
| P3 | Cross-check | "Give the current NIST SP 800-63B minimum password length when a password is the only authenticator, and when it is used with MFA. Give the section number and a link to the NIST page." | Link opens and section matches |
| P4 | Scenarios | "Write 6 short hostel-student scenarios (reused password, shared OTP, MFA fatigue, shared PC, lost phone, fake portal). For each: situation, safe response, why. No real brand names or real passwords." | Safe response never asks for OTP or passwords |
| P5 | Guide | "Write an 800-word beginner guide on passphrases, password managers and MFA types for 18-year-olds. Use NIST length-first guidance. Do not use realistic example passwords. Plain words, short paragraphs." | Word count; no composition-rule advice |
| P6 | Quiz | "Write 10 multiple-choice questions from the guide only, with an answer key and a one-line reason. One clearly correct answer each." | Every answer is in the guide |
| P7 | Infographic image | "Flat vector infographic, three columns comparing SMS code, authenticator app and security key. Icons only, no text, calm blue and green palette." Add the words yourself in Canva or Docs; AI image tools often garble text | Labels match the comparison table |
| P8 | Slides | "Make a 5-slide deck from this guide: the problem, the three attacks, passphrases and managers, the MFA ladder, a 30-minute action plan. One idea per slide." | Slides match the report's facts |
| P9 | Automation | "Turn this checklist into 12 weekly reminder messages, 40 words each, friendly, one action per message." | No message asks for a password or OTP |
| P10 | Red-team | "Review this guide for wrong, outdated or unsafe security advice. List each item, the rule it breaks, and the source that corrects it." | Compare against the verification table |

**Log of runs (fill in):**

| Date | Tool | Prompt # | What you changed after checking |
| --- | --- | --- | --- |
| | | | |

## 9. Before/after analysis

The "before" column holds common legacy advice that AI tools and older blogs often repeat when the prompt gives no source or date. It is an illustrative baseline, not a captured output from a named tool. Replace or add rows with what your own tools produced for prompt P5.

| Topic | Before (legacy advice) | Problem | After (this kit) |
| --- | --- | --- | --- |
| Password rules | "Use 8+ characters with a capital, a number and a symbol." | NIST Rev. 4 drops forced mixes and sets 15 characters when a password is the only factor | Long random passphrase, 5–6 words, never reused |
| Changing passwords | "Change it every 90 days." | NIST advises against scheduled changes; people just add a digit | Change on breach, suspicious login or reuse |
| MFA | "SMS codes are secure enough." | SMS and one-time codes can be phished | Authenticator app by default; key or passkey for email and vault |
| Recovery codes | "Save them in your notes app." | A single stolen phone or synced note exposes them | Written down, locked away, separate from the phone |
| OTP | "Share the code with support to verify you." | Anyone asking for an OTP is attacking you | Never share an OTP; call back on the official number |
| Examples | "For example, P@ssw0rd!" | Realistic examples get copied and appear on blocklists | Placeholders only; dummy strings in the demo |
| Shared PCs | "Let the browser remember your password." | The next user logs in as you | Private window, no remember, sign out |

### Before/after on the kit itself

| Measure | Before review | After review |
| --- | --- | --- |
| Statements checked against a source | 0 | 12 claims in the verification table |
| Conflicts found between sources | not looked for | 2 (rotation, composition) resolved in favour of NIST |
| Risky statistics | several percentages | all removed |
| Real-looking sample passwords | possible | none; dummy only |

### Your own run (fill in)

| Prompt | Tool | Output problem found | Fix |
| --- | --- | --- | --- |
| | | | |

## 10. Ethics and final demo

### Ethics

- **No real passwords.** Never type, paste, test or collect a real password, OTP or recovery code, in any tool, quiz or AI prompt. The entropy demo accepts no input.
- **Dummy accounts only** for any MFA practice. Create throwaway accounts that hold nothing of value.
- **No attack tools.** The project explains attacks; it does not run credential-stuffing or cracking against anyone.
- **Do not weaken security.** No advice to reuse passwords, skip MFA, share OTPs or disable lockouts, even for convenience.
- **Honest sourcing.** AI output is a draft. Every fact is checked, dated and cited; unchecked claims are removed.
- **Privacy.** Examples use no real people, schools or numbers. Report scams to your hostel IT desk or to CERT-In.

### Final demo (4 minutes)

1. **Problem (30 s).** Show the slide on reuse and credential stuffing.
2. **Entropy demo (60 s).** Run `python3 entropy_demo.py`. Point at Hostel@2026: a high naive score, under a second to guess.
3. **Passphrase (30 s).** Show six random words and their 77.5-bit score.
4. **MFA ladder (60 s).** Show the infographic: SMS, authenticator app, security key.
5. **Scenario (45 s).** Ask the class scenario 2 (the caller wants the OTP). Take answers, then reveal the safe response.
6. **Quiz and reminder (15 s).** Launch the quiz; show the weekly reminder for this week.

## 11. Sources

Found by web search on 26 Oct 2026. Items marked secondary are summaries of the primary document; open the primary before citing.

- NIST SP 800-63B Digital Identity Guidelines (Rev. 4): primary at pages.nist.gov/800-63-4. Secondary summaries read: [Axonbuild](https://axonbuild.com/blog/nist-minimum-password-length/), [Security Scientist](https://www.securityscientist.net/blog/password-policy-evidence-length-complexity-rotation/), [Optro](https://optro.ai/blog/nist-password-guidelines), [NHI Mgmt Group](https://nhimg.org/articles/nist-800-63b-rev-4-resets-password-policy-priorities/), [Netwrix](https://netwrix.com/en/resources/blog/nist-password-guidelines/).
- [NIST Small Business Fact Sheet: Multi-Factor Authentication (Feb 2024)](https://www.nist.gov/media/634876)
- CERT-In advisory on a large credential leak (June 23), secondary report: [Outlook Business](https://www.outlookbusiness.com/amp/story/deeptech/tech/cyber-watchdog-flags-16-bn-credentials-leak-what-users-can-do-to-stay-safe). Primary at cert-in.org.in.
- CERT-In MFA guidance, secondary: [NewsBytes](https://www.newsbytesapp.com/news/science/cert-in-urges-mfa-using-authenticator-apps-or-hardware-keys/tldr)
- CISA: [Creating and managing strong passwords](https://www.cisa.gov/news-events/alerts/2018/03/27/creating-and-managing-strong-passwords); [Next-level MFA: FIDO authentication](https://cisa.gov/blog/2022/10/18/next-level-mfa-fido-authentication); [CISA on phishing-resistant MFA, via SC Media](https://www.scmagazine.com/brief/cisa-phishing-resistant-mfa-necessary-in-combating-cyber-threats)
- Credential stuffing vs brute force vs spraying: [SecureW2](https://securew2.com/blog/credential-stuffing-what-it-is), [Ping Identity](https://www.pingidentity.com/en/resources/cybersecurity-fundamentals/threats/credential-stuffing.html), [Abnormal](https://abnormal.ai/ja/glossary/credential-stuffing)
- [Bitwarden security white paper](https://bitwarden.com/help/bitwarden-security-white-paper/)
