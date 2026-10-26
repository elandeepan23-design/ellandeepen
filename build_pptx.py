from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor

NAVY, LIGHT, TEAL, AMBER = RGBColor(0x14,0x21,0x3D), RGBColor(0xF6,0xF5,0xF0), RGBColor(0x17,0x69,0x5F), RGBColor(0xF2,0xB2,0x6B)
prs = Presentation(); prs.slide_width, prs.slide_height = Inches(13.333), Inches(7.5)
blank = prs.slide_layouts[6]

def bg(slide, color):
    f = slide.background.fill; f.solid(); f.fore_color.rgb = color

def text(slide, x, y, w, h, lines, size, color, bold=False):
    tb = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h)); tf = tb.text_frame; tf.word_wrap = True
    for i, ln in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = ln; p.font.size = Pt(size); p.font.bold = bold; p.font.color.rgb = color; p.space_after = Pt(10)

def table(slide, rows, widths, y=2.0, size=16):
    t = slide.shapes.add_table(len(rows), len(rows[0]), Inches(0.9), Inches(y), Inches(sum(widths)), Inches(0.6*len(rows))).table
    for c, w in enumerate(widths): t.columns[c].width = Inches(w)
    for r, row in enumerate(rows):
        for c, val in enumerate(row):
            cell = t.cell(r, c); cell.text = val
            for p in cell.text_frame.paragraphs: p.font.size = Pt(size); p.font.bold = (r == 0 or c == 0)

def slide(title, dark, notes, footer):
    s = prs.slides.add_slide(blank); bg(s, NAVY if dark else LIGHT)
    text(s, 0.9, 0.6, 11.5, 1.4, [title], 36 if dark else 34, LIGHT if dark else NAVY, True)
    text(s, 0.9, 6.8, 11.5, 0.5, [footer], 12, RGBColor(0xA9,0xB4,0xCC) if dark else RGBColor(0x5B,0x64,0x72))
    s.notes_slide.notes_text_frame.text = notes
    return s

s = slide("One leaked password can open every account you reuse it on.", True,
  "Credential stuffing replays real leaked logins on other sites; it works because of reuse.", "Credential stuffing (OWASP). Practise on dummy accounts only.")
text(s, 0.9, 2.6, 11.5, 3.5, ["1  A site you used is breached and its logins leak.", "2  Bots replay the same email and password on other sites.", "3  Your reused password opens your email, then everything else."], 24, LIGHT)

s = slide("Three attacks, three different defences", False,
  "A strong password stops brute force. Only a unique one stops credential stuffing.", "Sources: OWASP; vendor explainers.")
table(s, [["Attack","What the attacker starts with","What stops it"],
  ["Credential stuffing","Real passwords leaked from another site","Unique password per site, plus MFA"],
  ["Brute force","Nothing; guesses many passwords","Long passphrase, lockout"],
  ["Password spraying","A short list of very common passwords","Block common passwords, lockout"]], [3,4.5,4.5])
text(s, 0.9, 5.2, 11.5, 1, ["A strong password stops brute force. Only a unique one stops credential stuffing."], 22, NAVY, True)

s = slide("Long and random beats complex", False,
  "Pick words randomly from a big list. Crack times assume 10 billion guesses per second and are illustrative.", "Numbers from the entropy demo (dummy data). NIST SP 800-63B Rev. 4: length first, no forced symbols.")
text(s, 0.9, 1.9, 5.6, 2.8, ["LOOKS COMPLEX", "Hostel@2026", "Common word plus decoration. Guessed in under a second."], 20, NAVY)
text(s, 7.0, 1.9, 5.6, 2.8, ["ACTUALLY STRONG", "six random words", "About 77.5 bits from a 7776-word list. Hundreds of thousands of years at an assumed 10 billion guesses/s."], 20, TEAL)
text(s, 0.9, 5.0, 11.5, 1.5, ["A password manager remembers the rest.", "You memorise one master passphrase; it creates a unique random password for every site."], 22, NAVY, True)

s = slide("Climb the MFA ladder", False,
  "SMS today, authenticator app this month, passkey or key for email when you can.", "Sources: CISA; NIST small-business MFA fact sheet.")
table(s, [["Method","Phishing-resistant?","Works offline?","Use it for"],
  ["SMS code","No","No, needs mobile network","Only if nothing better exists"],
  ["Authenticator app","No, a fake site can collect the code","Yes","Most accounts"],
  ["Security key or passkey","Yes (FIDO2 / WebAuthn)","Yes","Email and your password-manager vault"]], [2.8,3.4,2.8,3.0])
text(s, 0.9, 5.2, 11.5, 1, ["Any MFA beats none. Phishing-resistant MFA is the gold standard (CISA)."], 22, NAVY, True)

s = slide("Your first 30 minutes", True,
  "Each step takes about ten minutes. Dummy accounts only for practice.", "Never type a real password into a demo or an AI tool.")
text(s, 0.9, 2.2, 6.0, 4, ["1  Install a password manager; set a master passphrase.", "2  New passphrase on your main email; turn on MFA.", "3  Add MFA to your college portal and payment apps.", "4  Write down recovery codes and lock them away."], 22, LIGHT)
text(s, 7.4, 2.2, 5.2, 4, ["THREE RULES, ALWAYS", "Never share an OTP with anyone.", "Deny any login prompt you did not start.", "Keep recovery codes offline, away from your phone."], 22, AMBER)

prs.save("Password_MFA_Habits_5_slides.pptx")
