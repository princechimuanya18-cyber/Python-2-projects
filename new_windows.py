# login_signup_windows.py
import tkinter as tk
import uuid
from PIL import Image, ImageTk, ImageFilter
import re  # for strong password checking
from dashboard import profile_window


DATA_FILE = "users.json"

# ----------------------------
# JSON HELPERS
# ----------------------------
def save_user(data):
    try:
        with open(DATA_FILE, "r") as f:
            all_users = json.load(f)
    except FileNotFoundError:
        all_users = {}

    all_users[data["user_id"]] = data

    with open(DATA_FILE, "w") as f:
        json.dump(all_users, f, indent=4)


def load_users():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# ----------------------------
# PASSWORD TOGGLE ICON HANDLER
# ----------------------------
def create_eye_button(entry_widget, parent):
    show_password = tk.BooleanVar(value=False)

    def toggle():
        if show_password.get():
            entry_widget.config(show="*")
            eye_btn.config(text="👁")   # closed eye
            show_password.set(False)
        else:
            entry_widget.config(show="")
            eye_btn.config(text="👁‍🗨")  # open eye
            show_password.set(True)

    eye_btn = tk.Button(
        parent,
        text="👁",
        font=("Arial", 12),
        bg="white",
        bd=0,
        command=toggle
    )
    return eye_btn


# ---------------------------------------------------
#                 LOGIN WINDOW
# ---------------------------------------------------
def login_window(parent):
    top = tk.Toplevel(parent)
    top.attributes("-fullscreen", True)
    top.title("Login")
    top.bind("<Escape>", lambda e: top.destroy())

    # ----------------------------
    # LOGGIN BACKGROUND
    # ----------------------------
    img_path = r"C:\Users\úú\Documents\GitHub\python-1-projects\finance_and_expense\PYTHON_PROJECTS_2\login.jpg"
    bg = Image.open(img_path)
    bg = bg.resize(
        (top.winfo_screenwidth(), 
         top.winfo_screenheight())
    )
    bg = bg.filter(ImageFilter.GaussianBlur(12))

    bg_photo = ImageTk.PhotoImage(bg)
    label_bg = tk.Label(top, image=bg_photo)
    label_bg.place(x=0, y=0, relwidth=1, relheight=1)
    top.bg_photo = bg_photo

    # ----------------------------
    # LOGIN CARD
    # ----------------------------
    card = tk.Frame(
        top, 
        bg ="white", 
        highlightbackground="#cccccc", 
        highlightthickness=2
    )
    card.configure(width=500, height=350)
    card.pack_propagate(False)
    card.place(relx=0.5, rely=0.5, anchor="center")

    label_login= tk.Label(card, text="Login", font=("Segoe UI", 24, "bold"), bg="white").pack(pady=10)

    # Login Username
    label_login= tk.Label(
        card, 
        text="Username", 
        font=("Segoe UI", 14), 
        bg="white"
    )
    label_login.pack()
    user_entry = tk.Entry(card, font=("Segoe UI", 14))
    user_entry.pack(pady=5)

    # Login Password
    pw_login = tk.Label(
        card, 
        text="Password", 
        font=("Segoe UI", 14), 
        bg="white"
    )
    pw_login.pack()

    pw_frame = tk.Frame(card, bg="white")
    pw_frame.pack()

    pw_entry = tk.Entry(pw_frame, font=("Segoe UI", 14), show="*")
    pw_entry.pack(side="left")

    eye_button = create_eye_button(pw_entry, pw_frame)
    eye_button.pack(side="left", padx=5)

    result = tk.Label(
        card, text="", 
        fg="red", bg="white", 
        font=("Segoe UI", 12)
    )
    result.pack(pady=5)

    # LOGIN LOGIC
    def process_login():
        users = load_users()
        username = user_entry.get().strip()
        pw = pw_entry.get().strip()

        user_record = None

    # Find user by username
        for uid, info in users.items():
            if info["username"] == username:
                user_record = (uid, info)
                break

        if not user_record:
            result.config(text="Invalid username or password!", fg="red")
            return

    # Validate password
        if user_record[1]["password"] != pw:
            result.config(text="Invalid username or password!", fg="red")
            return

    user_record = None
    # SUCCESS
    result.config(text="Login Successful!", fg="green")
    uid = user_record[0]

    # Open dashboard
    profile_window(top, uid)

    tk.Button(
        card,
        text="Login",
        font=("Segoe UI", 14, "bold"),
        bg="#0d6efd",
        fg="white",
        command=lambda: profile_window(root),
        
    ).pack(pady=10)



        

# ---------------------------------------------------
#                 SIGNUP WINDOW
# ---------------------------------------------------
def signup_window(parent):
    top = tk.Toplevel(parent)
    top.attributes("-fullscreen", True)
    top.title("Signup")
    top.bind("<Escape>", lambda e: top.destroy())

    # Background
    img_path = r"C:\Users\úú\Documents\GitHub\python-1-projects\finance_and_expense\PYTHON_PROJECTS_2\login.jpg"
    bg = Image.open(img_path)
    bg = bg.resize((top.winfo_screenwidth(), top.winfo_screenheight()))
    bg = bg.filter(ImageFilter.GaussianBlur(12))
    bg_photo = ImageTk.PhotoImage(bg)

    label_bg = tk.Label(top, image=bg_photo)
    label_bg.place(x=0, y=0, relwidth=1, relheight=1)
    top.bg_photo = bg_photo

    # CARD
    card = tk.Frame(top, bg="white", highlightbackground="#cccccc", highlightthickness=2)
    card.configure(width=550, height=450)
    card.pack_propagate(False)
    card.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(card, text="Create Account", font=("Segoe UI", 24, "bold"), bg="white").pack(pady=10)

    # Username
    tk.Label(card, text="Username:", font=("Segoe UI", 14), bg="white").pack()
    username_entry = tk.Entry(card, font=("Segoe UI", 14))
    username_entry.pack(pady=5)

    # Password
    tk.Label(card, text="Password:", font=("Segoe UI", 14), bg="white").pack()

    pw_frame = tk.Frame(card, bg="white")
    pw_frame.pack()

    pw_entry = tk.Entry(pw_frame, font=("Segoe UI", 14), show="*")
    pw_entry.pack(side="left")

    eye_btn = create_eye_button(pw_entry, pw_frame)
    eye_btn.pack(side="left", padx=5)

    # PIN creation
    tk.Label(card, text="Create 4-digit PIN:", font=("Segoe UI", 14), bg="white").pack(pady=5)
    pin_entry = tk.Entry(card, font=("Segoe UI", 14))
    pin_entry.pack()

    # Status
    result = tk.Label(card, text="", font=("Segoe UI", 12), fg="red", bg="white")
    result.pack(pady=10)

    # STRONG PASSWORD CHECK
    def strong_password(pw):
        return (
            len(pw) >= 6
            and re.search(r"[A-Za-z]", pw)
            and re.search(r"[0-9]", pw)
            and re.search(r"[^A-Za-z0-9]", pw)
        )

    # SIGNUP LOGIC
    def process_signup():
        username = username_entry.get().strip()
        pw = pw_entry.get().strip()
        pin = pin_entry.get().strip()

        if not strong_password(pw):
            result.config(text="Password must include letter, number, special character!", fg="red")
            return

        if not (pin.isdigit() and len(pin) == 4):
            result.config(text="PIN must be 4 digits!", fg="red")
            return

        user_id = str(uuid.uuid4())[:8].upper()

        users = load_users()
        for _, info in users.items():
            if info["username"] == username:
                result.config(text="Username already exists!", fg="red")
                return

        data = {
            "user_id": user_id,
            "username": username,
            "password": pw,
            "pin": pin
        }

        save_user(data)
        result.config(text="Account created successfully! Redirecting...", fg="green")

        # OPEN LOGIN WINDOW IMMEDIATELY
        top.after(1200, lambda: login_window(parent))

    tk.Button(
        card,
        text="Create Account",
        font=("Segoe UI", 14, "bold"),
        bg="#198754",
        fg="white",
        command=process_signup
    ).pack(pady=20)

