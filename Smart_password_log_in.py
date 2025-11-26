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


import tkinter as tk
from PIL import Image, ImageTk, ImageFilter
import new_windows

# ----------------------------
# ROOT WINDOW
# ----------------------------
root = tk.Tk()
root.attributes('-fullscreen', True)
root.title("Smart Password Validator")
root.configure(bg="#ffffff")

root.bind("<Escape>", lambda e: root.attributes('-fullscreen', False))


# ----------------------------
# LOAD + BLUR BACKGROUND IMAGE
# ----------------------------
image_path = r"C:\Users\úú\Documents\GitHub\python-1-projects\finance_and_expense\PYTHON_PROJECTS_2\image.webp"

bg_image = Image.open(image_path)

# Resize to full screen
screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()
bg_image = bg_image.resize((screen_w, screen_h))

# Apply blur
blur_bg = bg_image.filter(ImageFilter.GaussianBlur(radius=12))

# Convert to Tkinter
bg_photo = ImageTk.PhotoImage(blur_bg)

# Display background
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)


# ----------------------------
# MAIN CONTAINER (SEMI-OPAQUE CARD)
# ----------------------------
card = tk.Frame(root, bg="#ffffff", bd=0, highlightthickness=2)
card.configure(width=800, height=300)
card.pack_propagate(False)

card.place(relx=0.5, rely=0.5, anchor="center")

# ----------------------------
# HEADER TEXT
# ----------------------------
title = tk.Label(
    card,
    text="Smart Password/ID Validator",
    font=("Segoe UI", 28, "bold"),
    bg="#ffffff",
    fg="#222222",
)
title.pack(pady=(0, 10))

subtitle = tk.Label(
    card,
    text="Signup / Login",
    font=("Segoe UI", 16),
    bg="#ffffff",
    fg="#444444",
)
subtitle.pack(pady=(0, 20))


# ----------------------------
# QUESTION
# ----------------------------
question = tk.Label(
    card,
    text="Already have an account?",
    font=("Segoe UI", 14),
    bg="#ffffff",
    fg="#333333"
)
question.pack(pady=(10, 10))


# ----------------------------
# BUTTONS
# ----------------------------
btn_frame = tk.Frame(card, bg="#ffffff")
btn_frame.pack()

style_btn = {"font": ("Segoe UI", 12, "bold"), "padx": 20, "pady": 8}

yes_btn = tk.Button(
    btn_frame,
    text="Yes",
    bg="#198754",
    fg="white",
    activebackground="#157347",
    activeforeground="white",
    command=new_windows.login_window,
    **style_btn
)
yes_btn.grid(row=0, column=0, padx=10)

no_btn = tk.Button(
    btn_frame,
    text="No",
    bg="#dc3545",
    fg="white",
    activebackground="#bb2d3b",
    activeforeground="white",
    command=new_windows.signup_window,
    **style_btn
)
no_btn.grid(row=0, column=1, padx=10)


# ----------------------------
# FOOTER
# ----------------------------
footer = tk.Label(
    root,
    text="Powered by Metafrica",
    font=("Segoe UI", 9),
    bg="#ffffff",
    fg="#000000"
)
footer.place(relx=1.0, rely=1.0, x=-20, y=-20, anchor="se")


root.mainloop()
