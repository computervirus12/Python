import tkinter as tk
from tkinter import messagebox
import time
import datetime

# Configurable delays
STARTUP_DELAY = 7  # or 19
SHUTDOWN_DELAY = 7  # or 8

# Simulated status
BATTERY_LEVEL = 76
WIFI_STATUS = "Connected"

# Startup screen with logo
def show_startup():
    splash = tk.Tk()
    splash.attributes('-fullscreen', True)
    splash.configure(bg="black")
    tk.Label(splash, text="🖥️ PyOS Booting...", font=("Arial", 40), fg="white", bg="black").pack(expand=True)
    splash.update()
    time.sleep(STARTUP_DELAY)
    splash.destroy()

# Login screen
def show_login():
    login = tk.Tk()
    login.attributes('-fullscreen', True)
    login.configure(bg="darkblue")

    def attempt_login():
        if username.get() == "admin" and password.get() == "1234":
            login.destroy()
            launch_desktop()
        else:
            messagebox.showerror("Login Failed", "Incorrect username or password")

    tk.Label(login, text="🔐 Welcome to PyOS", font=("Arial", 30), fg="white", bg="darkblue").pack(pady=50)
    username = tk.Entry(login, font=("Arial", 20))
    username.pack(pady=10)
    password = tk.Entry(login, font=("Arial", 20), show="*")
    password.pack(pady=10)
    tk.Button(login, text="Login", font=("Arial", 20), command=attempt_login).pack(pady=20)
    login.mainloop()

# Desktop shell
def launch_desktop():
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.configure(bg="skyblue")

    # Wallpaper toggle
    def toggle_wallpaper():
        current = root.cget("bg")
        root.configure(bg="lightgreen" if current == "skyblue" else "skyblue")

    # Shutdown screen
    def shutdown():
        root.withdraw()
        shut = tk.Toplevel()
        shut.attributes('-fullscreen', True)
        shut.configure(bg="black")
        tk.Label(shut, text="🛑 Shutting down PyOS...", font=("Arial", 40), fg="white", bg="black").pack(expand=True)
        shut.update()
        time.sleep(SHUTDOWN_DELAY)
        shut.destroy()

    # Taskbar
    taskbar = tk.Frame(root, bg="gray", height=40)
    taskbar.pack(side="bottom", fill="x")
    tk.Button(taskbar, text="Start", command=lambda: show_start_menu(root)).pack(side="left", padx=5)
    tk.Button(taskbar, text="Wallpaper", command=toggle_wallpaper).pack(side="left", padx=5)
    tk.Button(taskbar, text="Shutdown", command=shutdown).pack(side="right", padx=5)

    # Battery & Wi-Fi
    tk.Label(taskbar, text=f"🔋 {BATTERY_LEVEL}%", bg="gray", fg="white").pack(side="right", padx=10)
    tk.Label(taskbar, text=f"📶 {WIFI_STATUS}", bg="gray", fg="white").pack(side="right", padx=10)

    # Clock
    clock_label = tk.Label(taskbar, bg="gray", fg="white")
    clock_label.pack(side="right", padx=10)
    def update_clock():
        now = datetime.datetime.now()
        clock_label.config(text=now.strftime("%Y-%m-%d %H:%M:%S"))
        root.after(1000, update_clock)
    update_clock()

    # Desktop icons
    apps = [
        ("Notepad", open_notepad),
        ("Calculator", open_calculator),
        ("Browser", open_browser),
        ("File Explorer", open_file_explorer)
    ]
    for i, (name, command) in enumerate(apps):
        tk.Button(root, text=name, command=command, width=12, height=2).place(x=100, y=100 + i * 100)

    root.mainloop()

# Start menu
def show_start_menu(parent):
    menu = tk.Toplevel(parent)
    menu.geometry("200x250+0+350")
    menu.title("Start Menu")
    tk.Button(menu, text="Notepad", command=open_notepad).pack(fill="x")
    tk.Button(menu, text="Calculator", command=open_calculator).pack(fill="x")
    tk.Button(menu, text="Browser", command=open_browser).pack(fill="x")
    tk.Button(menu, text="File Explorer", command=open_file_explorer).pack(fill="x")

# Apps
def open_notepad():
    app = tk.Toplevel()
    app.title("Notepad")
    app.geometry("400x300")
    text = tk.Text(app)
    text.pack(expand=True, fill="both")

def open_calculator():
    app = tk.Toplevel()
    app.title("Calculator")
    app.geometry("300x200")
    tk.Label(app, text="Calculator (Simulated)", font=("Arial", 16)).pack(pady=20)

def open_browser():
    app = tk.Toplevel()
    app.title("Browser")
    app.geometry("500x400")
    tk.Label(app, text="Web Browser (Simulated)", font=("Arial", 16)).pack(pady=20)

def open_file_explorer():
    app = tk.Toplevel()
    app.title("File Explorer")
    app.geometry("400x300")
    files = ["Document.txt", "Photo.jpg", "Music.mp3", "Video.mp4"]
    for f in files:
        tk.Label(app, text=f, font=("Arial", 14)).pack(anchor="w", padx=10)

# Run the OS
show_startup()
show_login()