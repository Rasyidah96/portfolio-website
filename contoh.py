
# LOVE SCAMMER DETECTOR (BASIC)

# Senarai keyword scam biasa
scam_keywords = [
    "money", "western union", "transfer", "bank", "urgent",
    "gift card", "investment", "bitcoin", "need help",
    "i love you", "baby", "dear", "sweetheart", "marry me",
    "alone", "widow", "trust me", "i promise"
]

# Minta input dari user
message = input("💌 Paste love message here:\n> ").lower()

# Flag untuk kenal pasti scam
is_scam = False

# Semak jika mesej ada keyword scam
for keyword in scam_keywords:
    if keyword in message:
        is_scam = True
        break

# Papar hasil
if is_scam:
    print("\n🚨 Warning: This message may be a SCAM!")
else:
    print("\n✅ This message looks safe (no scam keywords found).")
