# profile_window.py
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageFilter
from dateutil import parser
import json
import datetime

DATA_FILE = "users.json"


# ----------------------------
# Load User Data
# ----------------------------
def load_users():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


# ----------------------------
# Mask Password (******3B!)
# ----------------------------
def mask_password(pw):
    if len(pw) <= 3:
        return "*" * len(pw)
    return "*" * (len(pw) - 3) + pw[-3:]


# ----------------------------
# Profile Window
# ----------------------------
def profile_window(parent, user_id):
    users = load_users()

    if user_id not in users:
        messagebox.showerror("Error", "User data not found.")
        return

    user_data = users[user_id]

    # Update "last modified"
    user_data["last_modified"] = datetime.datetime.now().isoformat()
    with open(DATA_FILE, "w") as f:
        json.dump(users, f, indent=4)

    # Window Setup
    top = tk.Toplevel(parent)
    top.attributes("-fullscreen", True)
    top.title("User Profile")
    top.bind("<Escape>", lambda e: top.destroy())

    # ----------------------------
    # Background (Blurred)
    # ----------------------------
    try:
        bg = Image.open("login.jpg")
    except:
        bg = Image.new("RGB", (1920, 1080), "gray")

    screen_w = top.winfo_screenwidth()
    screen_h = top.winfo_screenheight()
    bg = bg.resize((screen_w, screen_h))
    bg = bg.filter(ImageFilter.GaussianBlur(18))

    bg_photo = ImageTk.PhotoImage(bg)
    top.bg_photo = bg_photo

    tk.Label(top, image=bg_photo).place(x=0, y=0, relwidth=1, relheight=1)

    # ----------------------------
    # PROFILE CARD
    # ----------------------------
    card = tk.Frame(
        top,
        bg="white",
        bd=0,
        highlightbackground="#cccccc",
        highlightthickness=3
    )
    card.configure(width=650, height=400)
    card.pack_propagate(False)
    card.place(relx=0.5, rely=0.5, anchor="center")

    # Title
    tk.Label(
        card,
        text="USER PROFILE",
        font=("Segoe UI", 22, "bold"),
        bg="white"
    ).pack(pady=20)

    # User ID
    tk.Label(
        card,
        text=f"User ID: {user_id}",
        font=("Segoe UI", 16),
        bg="white"
    ).pack(pady=10)

    # Masked Password
    masked_pw = mask_password(user_data["password"])
    tk.Label(
        card,
        text=f"Password: {masked_pw}",
        font=("Segoe UI", 16),
        bg="white"
    ).pack(pady=10)

    # Last Modified
    last_modified = parser.parse(user_data.get("last_modified", datetime.datetime.now().isoformat()))
    formatted = last_modified.strftime("%A, %d %B %Y  •  %I:%M %p")

    tk.Label(
        card,
        text=f"Last Modified: {formatted}",
        font=("Segoe UI", 14),
        fg="#555555",
        bg="white"
    ).pack(pady=10)

    # Close Button
    tk.Button(
        card,
        text="Close",
        font=("Segoe UI", 14, "bold"),
        bg="#dc3545",
        fg="white",
        padx=20,
        pady=8,
        command=top.destroy
    ).pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    root.attributes("-fullscreen", True)
    # Call your dashboard opening window here
    profile_window(root, "USER_ID_HERE")
    root.mainloop()
