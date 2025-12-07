# What it will do
# Accept an IBAN from the user
# Validate length per country using a dictionary (e.g., {"NG": 15, "DE": 22, …})
# Move the first 4 characters to the end
# Convert letters to numbers (A=10 … Z=35)
# Perform modulo-97
# Print: Valid IBAN or Invalid IBAN

from time import sleep

# Welcome board
print(
'''
\t\t=========================
    \t\tWELCOME TO THE CHIJULY IBAN 
        \t\tVALIDATOR
\t\t=========================
''')
print("\n\t\tEuropean's Best Account Trust")

# ---- LOGIN SECTION ----
log_in = input("\nWant to login? (yes/no): ").lower()

if log_in != "yes":
    print("\nThank you for using Chijuly IBAN Validator.")
    print("See you on your next transaction.")
    exit()

attempt = 0
while attempt < 3:
    try:
        password = input("Enter system password: ").upper()

        if password.endswith("IBAN") and len(password) == 8:
            print("processing...")
            sleep(1)
            print("processing...")
            sleep(1)
            print("Password verified ✔️\n")
            break

        attempt += 1
        print("\n❌ Invalid password. You have", 3 - attempt, "attempt(s) left.\n")

        if attempt == 3:
            print("🚫 Too many attempts. System locked 🔐")
            print("⏰ Try again in 10 minutes.")
            exit()

    except Exception:
        print("⚠️ Error in password verification system.")
        exit()

# ---- IBAN VALIDATOR STARTS HERE ----

iban_length = {
    "NG": 20,
    "US": 15,
    "UK": 30,
    "AG": 17,
    "GH": 18
}

print(
'''
------------------------
| LIST OF IBAN COUNTRIES
------------------------
| COUNTRY | CODE
-------------------------
| NIGERIA  = NG
| USA      = US
| UNITED K = UK
| ARGENT   = AG
| GHANA    = GH
-------------------------
''')

country = input("Enter IBAN country code: ").upper()

if country not in iban_length:
    print("\n❌ Invalid country code.")
    exit()

required_len = iban_length[country]
print("You are to input an IBAN number of length:", required_len)

# ---- IBAN NUMBER PROCESSING ----
iban_entry = input("\nEnter IBAN number (start with country code): ").replace(" ", "").upper()

if len(iban_entry) != required_len:
    print("\n❌ IBAN length does not match required length!")
    exit()

# Step 1: Rearrange IBAN
iban_rearranged = iban_entry[4:] + iban_entry[:4]

# Step 2: Convert letters → numbers
numeric_iban = ""
for ch in iban_rearranged:
    if ch.isdigit():
        numeric_iban += ch
    else:
        numeric_iban += str(ord(ch) - ord("A") + 10)
try:
    # Step 3: Modulo 97
    result = int(numeric_iban) % 97
    if result == 1:
        print("\n✅ VALID IBAN")
    else:
        print("\n❌ INVALID IBAN")
except:
    print("\n⚠️ Error processing IBAN. Ensure input format is correct.")
