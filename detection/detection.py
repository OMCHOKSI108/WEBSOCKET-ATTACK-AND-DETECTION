# csv_attack_analyzer.py
import csv
import time

# Attack Signatures and Impact Descriptions
attack_signatures = {
    "SYN Flood Attack": {
        "signatures": ["[syn]"],
        "impact": "Floods the target with TCP SYN packets, potentially exhausting the server's connection table. High impact if >100,000 packets."
    },
    "UDP Flood Attack": {
        "signatures": ["udp"],
        "impact": "Sends massive UDP packets to saturate bandwidth. Severe impact at >50,000 packets/sec."
    },
    "HTTP DDoS Attack": {
        "signatures": ["get / http/1.1", "host: test.com"],
        "impact": "Overwhelms server with HTTP requests, taxing CPU and memory. Significant impact at >10,000 requests/sec."
    },
    "Malformed Packet Attack": {
        "signatures": ["get /a"],
        "impact": "Sends oversized or invalid requests to crash poorly coded servers. Moderate impact at >1,000 packets."
    },
    "Slowloris Attack": {
        "signatures": ["x-a:", "partial", "http"],  # Broader terms for slow requests
        "impact": "Keeps many connections open with slow requests, locking server resources. High impact with >100 simultaneous connections."
    },
    "Header Injection Attack": {
        "signatures": ["x-inject:", "<script>", "inject"],  # Added "inject" for flexibility
        "impact": "Attempts to inject malicious headers, exploiting vulnerabilities. Low direct impact unless server is vulnerable."
    }
}

def analyze_csv(csv_file):
    print(f"[*] Analyzing CSV file: {csv_file} at {time.ctime()}")
    detected_attacks = {}
    total_packets = 0
    sample_unmatched = []  # For debugging unmatched packets

    try:
        with open(csv_file, "r") as f:
            reader = csv.DictReader(f)
            packets = list(reader)
            total_packets = len(packets)
            print(f"[*] Total packets in CSV: {total_packets:,}")

            for row in packets:
                timestamp = row.get("Time", "Unknown")
                info = row.get("Info", "").lower()
                protocol = row.get("Protocol", "").lower()
                length = int(row.get("Length", "0"))

                matched = False
                for attack, details in attack_signatures.items():
                    for sig in details["signatures"]:
                        if attack == "SYN Flood Attack":
                            if sig in info and protocol == "tcp" and "ack" not in info:
                                if attack not in detected_attacks:
                                    detected_attacks[attack] = {"count": 0, "timestamps": [], "total_bytes": 0}
                                detected_attacks[attack]["count"] += 1
                                detected_attacks[attack]["timestamps"].append(timestamp)
                                detected_attacks[attack]["total_bytes"] += length
                                matched = True
                        elif attack == "UDP Flood Attack":
                            if protocol == "udp" and sig in info:
                                if attack not in detected_attacks:
                                    detected_attacks[attack] = {"count": 0, "timestamps": [], "total_bytes": 0}
                                detected_attacks[attack]["count"] += 1
                                detected_attacks[attack]["timestamps"].append(timestamp)
                                detected_attacks[attack]["total_bytes"] += length
                                matched = True
                        elif sig in info:
                            if attack not in detected_attacks:
                                detected_attacks[attack] = {"count": 0, "timestamps": [], "total_bytes": 0}
                            detected_attacks[attack]["count"] += 1
                            detected_attacks[attack]["timestamps"].append(timestamp)
                            detected_attacks[attack]["total_bytes"] += length
                            matched = True

                # Debug unmatched packets
                if not matched and len(sample_unmatched) < 10:
                    sample_unmatched.append(info[:100])

    except Exception as e:
        print(f"[!] Error loading CSV: {e}")
        return

    # Output Results
    if not detected_attacks:
        print("[!] No attacks detected.")
    else:
        print("[*] Detected Attacks:")
        for attack, data in detected_attacks.items():
            count = data["count"]
            timestamps = data["timestamps"]
            total_bytes = data["total_bytes"]
            impact = attack_signatures[attack]["impact"]
            duration = float(max(timestamps)) - float(min(timestamps)) if timestamps else 1
            rate = count / duration if duration > 0 else count

            print(f"\n[+] {attack} (Occurred {count:,} times):")
            print(f"  Rate: {rate:,.0f} packets/sec")
            print(f"  Total Data: {total_bytes:,} bytes")
            print(f"  Impact: {impact}")
            print(f"  Sample Timestamps and Payloads:")
            for i, ts in enumerate(timestamps[:5], 1):
                payload = next((row["Info"][:100] for row in packets if row["Time"] == ts), "N/A")
                print(f"    {i}. Timestamp: {ts}")
                print(f"       Payload: {payload}{'...' if len(payload) > 100 else ''}")
            if count > 5:
                print(f"    ...and {count - 5:,} more instances")

    print(f"[*] Total attack packets detected: {sum(data['count'] for data in detected_attacks.values()):,}")
    if sample_unmatched:
        print("\n[*] Sample Unmatched Packets (first 10):")
        for i, unmatched in enumerate(sample_unmatched, 1):
            print(f"  {i}. {unmatched}")
    print("-" * 50)

if __name__ == "__main__":
    csv_file = "final_attack.csv" # Your CSV file
    analyze_csv(csv_file)