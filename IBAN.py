# What it will do
# Accept an IBAN from the user
# Validate length per country using a dictionary (e.g., {"NG": 15, "DE": 22, …})
# Move the first 4 characters to the end
# Convert letters to numbers (A=10 … Z=35)
# Perform modulo-97
# Print: Valid IBAN or Invalid IBAN

import json
from time import sleep
import os
# ----------------------------
# JSON USER DATA FUNCTIONS
# ----------------------------

USERS_FILE = os.path.join(os.path.dirname(__file__), "user.json")

def load_users():
    """Load users from JSON file."""
    try:
        with open(USERS_FILE, "r") as f:
            data = json.load(f)
       
            # If "users" is missing, auto-fix it
            if "user" not in data:
                data["user"] = []

            return data

    except FileNotFoundError:
        return {"user": []}


def save_users(data):
    """Save users back to JSON file."""
    with open(USERS_FILE, "w") as f:
        json.dump(data, f, indent=4)

def timecount():
    print("processing...")
    sleep(1)
    print("processing...")
    sleep(1) 
# ----------------------------
# WELCOME MESSAGE
# ----------------------------
print(
'''
\t\t=========================
\t\tWELCOME TO THE CHIJULY IBAN 
\t\tVALIDATOR
\t\t=========================
''')
print("\n\t\tEuropean's Best Account Trust")

# ----------------------------
# LOGIN SECTION
# ----------------------------
users_data = load_users()     #Make sure this is BEFORE login loop


current_user = None

# ====================
# SIGN UP AND PASSWORD SYSTEM
# ====================

sign_up = input("Do you have an account already(yes/no): ").lower()

try:
    if sign_up == "yes" or sign_up == "no":
        if sign_up == "yes":
            attempt = 0
            while attempt < 3:
                username = input("Enter username: ").lower().replace(" ", "")
                password = input("Enter password: ").upper()

            # check users
                for user in users_data["user"]:
                    if user["username"] == username and\
                        user["password"] == password:
                        current_user = user
                        break

                if current_user:
                    timecount()
                    print("Password verified ✔️\n")
                    break
                else:
                    attempt += 1
                    timecount()
                    print(f"❌ Invalid credentials. {3 - attempt} attempt(s) left.\n")

                    if attempt == 3:
                        print("🚫 Too many attempts. System locked 🔐")
                        exit()
        else:
            #else:
            # --- CREATE NEW USER ---
            create_username = input("Create username: ").lower().replace(" ", "")

            if not create_username.isalpha():
                print("❌ Username must contain letters only!")
                exit()

            create_password = input("Create user password (only letters): ").upper()

            if not create_password.isalpha():
                    print("❌ Password must contain letters only!")
                    exit()
            elif not len(create_password) >= 5:
                    print("❌ Password must be at least 5 characters long!")
                    exit()

    # --- SAVE NEW USER INTO JSON ---
            new_user = {
                "username": create_username,
                "password": create_password,
                "history": []
            }

    # Add to users list
            users_data["user"].append(new_user)
            save_users(users_data)

            print("\n✅ Successfully signed up!")
            print("➡ Please log in now.\n")

    # --- AUTO LOGIN IMMEDIATELY ---
            attempt = 0
            while attempt < 3:
                login_username = input("Enter username: ").lower()
                login_password = input("Enter password: ").upper()

                for user in users_data["user"]:
                    if user["username"] == login_username and \
                        user["password"] == login_password:
                        current_user = user
                        break

                if current_user:
                    timecount()
                    print("Login successful ✔️\n")
                    break
                else:
                    attempt += 1
                    timecount()
                    print(f"❌ Invalid login. {3 - attempt} attempt(s) left.")

                    if attempt == 3:
                        print("🚫 Too many attempts. System locked 🔐")
                        exit()
    else:
        print("Invalid input command")
        exit()
except:
    print("Invalid command")
    exit()

# ----------------------------
# IBAN VALIDATOR SETUP
# ----------------------------
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

iban_entry = input("\nEnter IBAN number (start with country code): ").replace(" ", "").upper()
if len(iban_entry) != required_len:
    print("\n❌ IBAN length does not match required length!")
    exit()

# ----------------------------
# IBAN VALIDATION
# ----------------------------
# Step 1: Rearrange IBAN
iban_rearranged = iban_entry[4:] + iban_entry[:4]

# Step 2: Convert letters to numbers
numeric_iban = ""
for ch in iban_rearranged:
    if ch.isdigit():
        numeric_iban += ch
    else:
        numeric_iban += str(ord(ch) - ord("A") + 10)

try:
    # Step 3: Modulo 97
    result = int(numeric_iban) % 97
    validation_result = "VALID" if result == 1 else "INVALID"

    if validation_result == "VALID":
        print("\n✅ VALID IBAN")
    else:
        print("\n❌ INVALID IBAN")

except Exception:
    print("\n⚠️ Error processing IBAN. Ensure input format is correct.")
    validation_result = "ERROR"

# ----------------------------
# SAVE TO USER HISTORY
# ----------------------------
if current_user:
    current_user.setdefault("history", []).append({
        "iban number": iban_entry,
        "country": country,
        "result": validation_result
    })
    save_users(users_data)

# ----------------------------
# SHOW USER HISTORY
# ----------------------------
print("\nYour IBAN validation history:")
for entry in current_user.get("history", []):
    print(f"{entry['iban number']} ({entry['country']}) - {entry['result']}")

print("\nThank you for using Chijuly IBAN Validator! ✅")
