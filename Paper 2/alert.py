
import tkinter as tk
from tkinter import ttk
import winsound

# Window setup
root = tk.Tk()
root.title("Security Alert Simulator")
root.configure(bg="#090d16")
root.attributes("-fullscreen", True)

# Variables
scan_value = 0
animation_state = True
revealed = False

# Colors
BG = "#090d16"
RED = "#ff3030"
GREEN = "#00ff88"
WHITE = "#ffffff"
GREY = "#8b96a8"

# Main container
main = tk.Frame(root, bg=BG)
main.pack(expand=True, fill="both")

# Simulated alert label
simulation = tk.Label(
    main,
    text="● SIMULATED ALERT ",
    font=("Consolas", 14, "bold"),
    fg="#ffbd44",
    bg=BG
)
simulation.pack(pady=(35, 15))

# Warning icon
warning = tk.Label(
    main,
    text="⚠",
    font=("Arial", 75, "bold"),
    fg=RED,
    bg=BG
)
warning.pack(pady=5)

# Main heading
title = tk.Label(
    main,
    text="SECURITY ALERT",
    font=("Arial", 32, "bold"),
    fg=RED,
    bg=BG
)
title.pack(pady=10)

# Message
message = tk.Label(
    main,
    text="A simulated security event has been detected.\n"
         "This is a visual security demonstration.",
    font=("Arial", 15),
    fg=WHITE,
    bg=BG,
    justify="center"
)
message.pack(pady=15)

# Status
status = tk.Label(
    main,
    text="INITIALIZING SIMULATED SCAN...",
    font=("Consolas", 13, "bold"),
    fg="#ffbd44",
    bg=BG
)
status.pack(pady=10)

# Progress bar
progress = ttk.Progressbar(
    main,
    length=450,
    mode="determinate",
    maximum=100
)
progress.pack(pady=15)

percentage = tk.Label(
    main,
    text="0%",
    font=("Consolas", 14),
    fg=WHITE,
    bg=BG
)
percentage.pack()

# Button
check_button = tk.Button(
    main,
    text="CHECK SECURITY ISSUE",
    font=("Arial", 15, "bold"),
    bg=RED,
    fg=WHITE,
    activebackground="#aa1111",
    activeforeground=WHITE,
    padx=25,
    pady=12,
    command=lambda: reveal_prank()
)

close_button = tk.Button(
    main,
    text="EXIT",
    font=("Arial", 13, "bold"),
    bg="#087a50",
    fg=WHITE,
    padx=25,
    pady=10,
    command=root.destroy
)


# Warning animation
def animate_warning():
    global animation_state

    if revealed:
        return

    animation_state = not animation_state

    warning.config(
        fg=RED if animation_state else "#751515"
    )

    root.after(500, animate_warning)


# Scanning animation
def update_scan():
    global scan_value

    if revealed:
        return

    if scan_value < 100:
        scan_value += 1

        progress["value"] = scan_value
        percentage.config(text=f"{scan_value}%")

        root.after(250, update_scan)

    else:
        status.config(
            text="SIMULATED SCAN COMPLETED",
            fg=GREEN
        )

        message.config(
            text="The simulated scan has finished.\n"
                 "Click below to view the security report."
        )

        winsound.MessageBeep(
            winsound.MB_ICONASTERISK
        )

        check_button.pack(pady=30)


# Reveal prank
def reveal_prank():
    global revealed

    if revealed:
        return

    revealed = True

    winsound.MessageBeep(
        winsound.MB_ICONEXCLAMATION
    )

    warning.config(
        text="✓",
        fg=GREEN
    )

    title.config(
        text="JUST KIDDING!",
        fg=GREEN
    )

    message.config(
        text="YOUR LAPTOP IS SAFE!\n\n"
             "You just got pranked!\n"
             "This was only a simulated security alert.\n\n"
             "No files were accessed or changed.",
        fg=WHITE
    )

    status.config(
        text="SIMULATION COMPLETE",
        fg=GREEN
    )

    progress.pack_forget()
    percentage.pack_forget()
    check_button.pack_forget()

    close_button.pack(pady=30)

    winsound.MessageBeep(
        winsound.MB_ICONASTERISK
    )

# Keyboard control during animation
def control_keyboard(event):

    # Allow emergency exit
    if event.keysym == "Escape":
        root.destroy()
        return "break"

    # Block other keys during animation
    if scan_value < 100:
        return "break"


root.bind_all("<KeyPress>", control_keyboard)

# Start animations
animate_warning()
root.after(250, update_scan)

# Run application
root.mainloop()
