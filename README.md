 

# WEBSOCKETS ATTACK AND ITS DETECTION PROJECT 
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.x-green.svg)
![Platform](https://img.shields.io/badge/platform-Ubuntu%20|%20Windows%20(WSL)-lightgrey.svg)

Welcome to the **DDoS Attack Simulation Toolkit**, a project by **Om Choksi**. This repository contains a collection of Python scripts designed for educational purposes to simulate various types of Denial-of-Service (DoS) and Distributed Denial-of-Service (DDoS) attacks. Additionally, it includes a packet analysis tool to detect and analyze attack patterns from CSV data.

> **Disclaimer**: This toolkit is intended for **educational and research purposes only**. Unauthorized use of these scripts against systems without explicit permission is illegal and unethical. Use responsibly and within legal boundaries.

## Table of Contents
- [Features](#features)
- [Scripts Overview](#scripts-overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
  - [Ubuntu](#ubuntu)
  - [Windows (via WSL)](#windows-via-wsl)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Features
- Simulate various DoS/DDoS attacks with GUI interfaces using `tkinter`.
- Analyze attack packets from CSV files with detailed detection and impact assessment.
- Multi-threaded attack implementations for realistic simulation.
- Cross-platform support (Ubuntu natively, Windows via WSL for `syn_udp.py`).

---

## Scripts Overview
| Script                  | Description                                                                 | Attack Type              |
|-------------------------|-----------------------------------------------------------------------------|--------------------------|
| `dos_attack.py`         | Launches a basic HTTP DoS attack with multiple threads.                    | HTTP Flood              |
| `header_injection_attack.py` | Simulates header injection with malicious payloads.                  | Header Injection        |
| `malformed_packet_attack.py` | Sends oversized/malformed HTTP packets to disrupt servers.           | Malformed Packet Attack |
| `slowloris_attack.py`   | Implements a Slowloris attack to exhaust server connections.              | Slowloris Attack        |
| `syn_udp.py`            | Launches SYN/UDP floods using `hping3` (Ubuntu only, WSL on Windows).     | SYN/UDP Flood           |
| `detection.py`          | Analyzes CSV packet captures to detect and assess attack patterns.        | Analysis Tool           |

---

## Prerequisites
- **Python 3.x**: Required for all scripts.
- **Ubuntu**: Native support for all scripts (including `syn_udp.py`).
- **Windows**: Requires WSL (Windows Subsystem for Linux) for `syn_udp.py`.
- **Dependencies**: 
  - `tkinter` (GUI library)
  - `hping3` (for `syn_udp.py`)
- **CSV File**: For `detection.py`, a packet capture in CSV format (e.g., from Wireshark).

---

## Installation

### Ubuntu
1. **Update System**:
   ```bash
   sudo apt update && sudo apt upgrade -y
   ```
2. **Install Python and Tkinter**:
   ```bash
   sudo apt install python3 python3-tk -y
   ```
3. **Install `hping3` (for `syn_udp.py`)**:
   ```bash
   sudo apt install hping3 -y
   ```
4. **Clone the Repository**:
   ```bash
   git clone https://github.com/omchoksi108/ddos-attack-toolkit.git
   cd ddos-attack-toolkit
   ```

### Windows (via WSL)
To run `syn_udp.py` on Windows, you need to set up WSL with Ubuntu:

1. **Enable WSL**:
   Open PowerShell as Administrator and run:
   ```powershell
   wsl --install
   ```
   Restart your system if prompted.

2. **Set WSL Default Version to 2**:
   ```powershell
   wsl --set-default-version 2
   ```

3. **Install Ubuntu**:
   ```powershell
   wsl --install -d Ubuntu
   ```

4. **Launch WSL and Set Up Ubuntu**:
   - Open a terminal and type `wsl`.
   - Follow the prompts to set a username and password for Ubuntu.

5. **Convert Ubuntu to WSL 2** (if needed):
   ```powershell
   wsl --set-version Ubuntu 2
   ```

6. **Update and Install Dependencies in Ubuntu**:
   Inside the WSL Ubuntu terminal:
   ```bash
   sudo apt update && sudo apt upgrade -y
   sudo apt install python3 python3-tk hping3 -y
   ```

7. **Clone the Repository**:
   ```bash
   git clone https://github.com/omchoksi/ddos-attack-toolkit.git
   cd ddos-attack-toolkit
   ```

---

## Usage
1. **Run Attack Scripts**:
   - For Python-based scripts (e.g., `dos_attack.py`, `slowloris_attack.py`):
     ```bash
     python3 dos_attack.py
     ```
   - A GUI will launch. Click "Run Attack" to start and "Exit" to stop.
   - For `syn_udp.py` (Ubuntu/WSL only):
     ```bash
     python3 syn_udp.py
     ```
     Select the attack type (SYN Flood, UDP Flood, or Slowloris) and provide target IP/port.

2. **Analyze Packets**:
   - Edit `detection.py` to point to your CSV file:
     ```python
     csv_file = "path/to/your/final_attack.csv"
     ```
   - Run the script:
     ```bash
     python3 detection.py
     ```
   - Review the detailed output of detected attacks.

3. **Customization**:
   - Modify `TARGET_IP`, `PORT`, `NUM_THREADS`, and `REQUESTS_PER_THREAD` in each script as needed.

---

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m "Add your feature"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a Pull Request.

Feel free to report bugs or suggest enhancements via the [Issues](https://github.com/omchoksi/ddos-attack-toolkit/issues) tab.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact
- **Author**: Om Choksi
- **GitHub**: [omchoksi108](https://github.com/omchoksi108)
- **Email**: omchoksi108@example.com (replace with your email)

Happy coding, and use this toolkit responsibly!

---

 
