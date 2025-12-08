
    # (step 1) Check that the total IBAN length is correct as per the country 
    # (this program won't do that, but you can modify the code to meet this 
    # requirement if you wish; note: you have to teach the code all the lengths used in Europe)

    # (step 2) Move the four initial characters to the end 
    # of the string (i.e., the country code and the check digits)

    # (step 3) Replace each letter in the string with two digits, 
    # thereby expanding the string, where A = 10, B = 11 ... Z = 35;

    # (step 4) Interpret the string as a decimal integer and compute the remainder 
    # of that number by modulo-dividing it by 97; If the remainder is 1, 
    # the check digit test is passed and the IBAN might be valid.

from collections import Counter

iban = input("Please enter your iban number: ").upper() 

if iban.startswith("NG50") and len(iban) < 15:
        print("IBAN number length is too short")

elif iban.startswith("NG50") and len(iban) > 30:
        print("IBAN number is too long")
else:
    try:
        iban_2 = iban[4:] + iban[:4]
        
        numeric = ""
        for ch in iban_2:
             if ch.isdigit():
                 numeric += ch
             else:
                 numeric += str(10 + ord(ch) - ord("A"))
        
        ib = int(numeric) % 97
        if ib == 1:
          print("Valid IBAN")
        else:
           print("Invalid IBAN")     
    except:
       print("it won't work")

# NEW TASK

# our task is to write a program which:

#  asks the user for one line of text to encrypt;
#  asks the user for a shift value (an integer number from the range 1..25 - 
# note: you should force the user to enter a valid shift value (don't give up and don't let bad data fool you!)
#  prints out the encoded text. 

text = input("Enter text: ")
att = ""

shift = int(input("Enter shift value: "))

if shift < 1:
    print("Shift value is invalid **lower than expected")
elif shift > 25:
    print("Shift value is invalid **higher than expected")

else:
   for t in text: 
        if not t.isalpha():
        continue
     t = t.upper()
     code_t = ord(t) + shift
        if code_t > ord('Z'):
           code_t = ord('A')
           att += chr(code_t)

# print(att)


# # Creating a palindrome

pal = input("Enter text: ")

clean = pal.replace(" ", "").lower()
attempts = 0
while True:

    if clean == clean[::-1]:
        print("It is a palindrome")
        break

    else:
       final_attempt = 3
       attempts += 1
       trials = final_attempt - attempts
       if 0 < trials < 3:
         print("It is not a palindrome and you have", trials, "more attempts left.")
         pal = input("\nEnter text: ")
       else:
           print("🚫 Too many attempts. System locked 🔐", end="\n")  # system goes temporarily locked
           print("⏰ Try again in 10 minutes.", end="\n")
           exit() 


# Creating anagram

ana_1 = input("Enter text 1: ")
ana_2 = input("\nEnter text 2: ")

clear_1 = ana_1.replace(" ", "").lower()
clear_2 = ana_2.replace(" ", "").lower()


if len(clear_1) == len(clear_2):
    if Counter(clear_1) == Counter(clear_2):
       print("It is an anagram")

else:
   print("It is not an anagram")

    
birth = input("Enter birthday(YY/MM/DD): ")

clean_birth = birth.replace("/", "")

total_sum = 0
if clean_birth.isdigit():  # Check if the character is a digit
    for cl in clean_birth:
         total_sum += int(cl)
         while total_sum > 9:
             total_sum = sum(int(d) for d in str(total_sum))

    print("Final single digit:", total_sum)

else:
 print("Invalid input")

# Find a word

text_1 = input("Enter your first word: ").lower()
text_2 = input("Enter your second word: ").lower()

pos = -1   # starting position before the string
found = True

for char in text_1:
    pos = text_2.find(char, pos + 1)    # search forward
    if pos == -1:                       # not found in order
        found = False
        break

if found:
    print("yes")
else:
    print("no")
