# 1. Register a new user
# Ask for name
# Auto-generate an ID
# Ask for password (validate strongly)
# Ask for / generate 4-digit PIN
# Save everything in JSON
# 2. Login system
# Enter ID
# Enter password
# Compare against stored JSON data
# 3. PIN confirmation
# Before “simulating a transaction”
# Enter 4-digit PIN
# Approve or deny
# 4. Display user profile
# Shows ID
# Shows masked password (e.g. ******3B!)
# Shows when last modified (using dateutil)


# main.py
import tkinter as tk
from PIL import Image, ImageTk, ImageFilter
import new_windows   # import the other file


# ----------------------------
# ROOT WINDOW
# ----------------------------
root = tk.Tk()
root.attributes("-fullscreen", True)
root.title("Smart Password Validator")
root.configure(bg="#ffffff")
root.bind("<Escape>", lambda e: root.attributes("-fullscreen", False))

# ----------------------------
# BACKGROUND
# ----------------------------
img_path = r"C:\Users\úú\Documents\GitHub\python-1-projects\finance_and_expense\PYTHON_PROJECTS_2\image.webp"

bg = Image.open(img_path)

screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()
bg = bg.resize((screen_w, screen_h))

# blur background
bg = bg.filter(ImageFilter.GaussianBlur(12))

bg_photo = ImageTk.PhotoImage(bg)
label_bg = tk.Label(root, image=bg_photo)
label_bg.image = bg_photo
label_bg.place(x=0, y=0, relwidth=1, relheight=1)

# ----------------------------
# MAIN CARD
# ----------------------------
card = tk.Frame(
    root, 
    bg="#ffffff", 
    bd=0, 
    highlightbackground="#dddddd",
    highlightthickness=2
)
card.configure(width=800, height=350)
card.pack_propagate(False)
card.place(relx=0.5, rely=0.5, anchor="center")

# ----------------------------
# HEADER
# ----------------------------
title = tk.Label(
    card, 
    text="Smart Password & ID Validator",
    font=("Segoe UI", 28, "bold"), 
    bg="#ffffff", 
    fg="#222222"
)
title.pack(pady=(10, 5))

subtitle = tk.Label(
    card, 
    text="Signup / Login",
    font=("Segoe UI", 16), 
    bg="#ffffff", 
    fg="#444444"
)
subtitle.pack(pady=(0, 20))

# ----------------------------
# QUESTION
# ----------------------------
q = tk.Label(
    card, 
    text="Already have an account?",
    font=("Segoe UI", 14), 
    bg="#ffffff", 
    fg="#333333"
)
q.pack()

# ----------------------------
# BUTTONS
# ----------------------------
btn_frame = tk.Frame(card, bg="#ffffff")
btn_frame.pack(pady=15)

style = {
    "font": ("Segoe UI", 12, "bold"), 
    "padx": 20, 
    "pady": 8
}

btn_yes = tk.Button(
    btn_frame, 
    text="Yes", 
    bg="#198754", 
    fg="white",
    activebackground="#157347", 
    command=lambda: new_windows.login_window(root),
    **style
)
btn_yes.grid(row=0, column=0, padx=10)

btn_no = tk.Button(
    btn_frame, 
    text="No", 
    bg="#dc3545", 
    fg="white",
    activebackground="#bb2d3b", 
    command=lambda: new_windows.signup_window(root),
    **style
)
btn_no.grid(row=0, column=1, padx=10)

# ----------------------------
# FOOTER
# ----------------------------
footer = tk.Label(
    root, 
    text="Powered by Metafrica",
    font=("Segoe UI", 9), 
    bg="#ffffff"
)
footer.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)

root.mainloop()
