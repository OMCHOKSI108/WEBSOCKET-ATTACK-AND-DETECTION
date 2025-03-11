# WebSocket Attack Detection Tool

## Overview
The **WebSocket Attack Detection Tool** is a cybersecurity project designed to **monitor network traffic** and detect potential attacks using Wireshark JSON exports. This tool helps identify various network threats such as **SYN Flood, UDP Flood, Port Scanning, and more.**

## Features
- **Simulate Attacks**: Perform SYN Flood, UDP Flood, and Slowloris attacks on a test environment.
- **Capture Network Traffic**: Use Wireshark to monitor and export network packets in JSON format.
- **Analyze Traffic**: Detect suspicious activities from the captured packets using predefined attack patterns.
- **Graphical User Interface (GUI)**: User-friendly interface to analyze Wireshark logs.

## File Structure
```
WebSocket_Detection_Tool/
│── attack/                # Attack simulation scripts
│   ├── dos_attack.py
│   ├── header_injection_attack.py
│   ├── malformed_attack.py
│   ├── slowloris_attack.py
|   ├── syn_udp.py
│── detection/               # Attack detection scripts
│   ├── detection.py           # Reads JSON and detects attacks 
│── data/               # Attack detection scripts
│   ├── final_attack.csv
│── requirements.txt          # Dependencies
│── README.md                 # Documentation
 
```

## Setup and Installation
### Prerequisites
- **Python 3.x** installed
- **Wireshark** installed for network packet capturing
- Required Python libraries:
  ```bash
  pip install -r requirements.txt
  ```

## Usage
### Step 1: Capture Network Traffic
1. Open **Wireshark**.
2. Start capturing packets on the target network.
3. Save the capture as **JSON format** (`File > Export Packet Dissections > As JSON`).

### Step 2: Perform Attacks (Optional for Testing)
1. Run an attack script from the `attacks/` folder:
   ```bash
   python attacks/syn_flood.py <target_ip> <port>
   ```

### Step 3: Analyze Captured Traffic
1. Run the detection tool:
   ```bash
   python detection/analyze.py
   ```
2. Enter the path to your Wireshark JSON file.
3. The tool will analyze the traffic and report detected attacks.

## Supported Attack Detections
| Attack Type        | Detection Method |
|-------------------|----------------|
| **SYN Flood**    | High volume of TCP SYN requests |
| **UDP Flood**    | Large number of UDP packets from a single source |
| **Slowloris**    | Multiple half-open HTTP connections |
| **Port Scanning** | Multiple connection attempts to different ports |

## Future Enhancements
- **Add GUI for better visualization**
- **Implement Machine Learning for advanced anomaly detection**
- **Support additional network attack types**

## Disclaimer
This tool is for **educational and research purposes only.** It should **only** be used in authorized test environments. The developers are not responsible for any misuse.

---
**Author:** [OM CHOKSI]  
**License:** MIT

