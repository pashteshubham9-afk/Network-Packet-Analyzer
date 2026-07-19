# 🔍 Network Packet Analyzer

A Python-based **Network Packet Analyzer** developed using **Python** and **Scapy**. This project captures live network packets and displays essential information such as **Source IP**, **Destination IP**, **Protocol**, **Packet Length**, and **Packet Summary** in real time.

It is designed as a beginner-friendly cybersecurity project to help students and networking enthusiasts understand how network communication works and how packet sniffing can be performed ethically.

---

# 📖 About the Project

The **Network Packet Analyzer** is a simple cybersecurity tool that captures live network traffic using the **Scapy** library. It analyzes each packet and extracts useful information, allowing users to understand how data travels between devices over a network.

This project was developed as part of the **CodSoft Cyber Security Internship** and demonstrates the fundamentals of packet sniffing, protocol analysis, and network monitoring using Python.

---

# ✨ Features

- Capture live network packets
- Display Source IP Address
- Display Destination IP Address
- Detect Protocol (TCP, UDP, ICMP, etc.)
- Display Packet Length
- Show Packet Summary
- Real-time packet monitoring
- Beginner-friendly command-line interface

---

# 🛠 Technologies Used

- Python 3
- Scapy
- VS Code
- Windows
- Npcap
- Networking Fundamentals

---

# 📂 Project Structure

```text
Network-Packet-Analyzer/
│
├── packet_analyzer.py
├── requirements.txt
├── README.md
├── LICENSE
├── screenshots/
│   ├── output1.png
│   └── output2.png
```

---

# 📋 Requirements

- Python 3.x
- Scapy
- Npcap
- Windows 10/11
- Administrator Privileges
- VS Code (Recommended)

---

# 💻 Windows Setup Guide

## Step 1: Install Python

Download Python from:

https://www.python.org/downloads/

✔ During installation, enable:

```
Add Python to PATH
```

---

## Step 2: Install Npcap

Download Npcap from:

https://npcap.com/

✔ During installation enable:

```
Install Npcap in WinPcap API-compatible Mode
```

---

## Step 3: Clone the Repository

```bash
git clone https://github.com/pashteshubham9-afk/Network-Packet-Analyzer.git
```

---

## Step 4: Open the Project Folder

```bash
cd Network-Packet-Analyzer
```

---

## Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install scapy
```

---

## Step 6: Verify Installation

```bash
python --version
```

```bash
pip show scapy
```

---

## Step 7: Run the Project

Open **Command Prompt** or **PowerShell** as Administrator.

```bash
python packet_analyzer.py
```

---

# 🖥 Example Output

```text
========== Packet Captured ==========

Source IP      : 192.168.29.15
Destination IP : 142.250.183.78
Protocol       : TCP
Packet Length  : 60 Bytes

Summary:
IP / TCP 192.168.29.15:51234 > 142.250.183.78:https

=====================================
```

---

# 📷 Screenshots

Save your screenshots inside the **screenshots** folder.

```text
screenshots/
├── output1.png
└── output2.png
```

Display them in README:

```md
## Screenshots

![Output 1](screenshots/output1.png)

![Output 2](screenshots/output2.png)
```

---

# 🧠 How It Works

1. Starts packet sniffing using Scapy.
2. Listens for live network traffic.
3. Captures incoming and outgoing packets.
4. Extracts Source IP and Destination IP.
5. Identifies the packet protocol.
6. Calculates packet length.
7. Displays packet information in real time.

---

# 📚 Concepts Used

- Packet Sniffing
- IP Packet Analysis
- TCP
- UDP
- ICMP
- Network Interfaces
- Packet Parsing
- Scapy
- Cybersecurity Fundamentals

---

# ❓ Troubleshooting

## ModuleNotFoundError: No module named 'scapy'

Install Scapy:

```bash
pip install scapy
```

---

## Permission Error

Run Command Prompt or PowerShell as **Administrator**.

---

## No Packets Captured

- Make sure Npcap is installed.
- Check your internet connection.
- Run the program with Administrator privileges.

---

## Python Not Found

Verify Python installation:

```bash
python --version
```

If Python is not recognized, reinstall Python and enable **Add Python to PATH**.

---

# 🎯 Future Improvements

- GUI using Tkinter
- Save packets as PCAP files
- Export captured packets to CSV
- Advanced packet filtering
- DNS Packet Analysis
- HTTP/HTTPS Packet Inspection
- Live Network Statistics
- Network Traffic Visualization Dashboard

---

# ⚠ Disclaimer

This project is developed **only for educational and ethical purposes**.

Please use it **only on networks that you own or have explicit permission to monitor.**

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a new branch.
3. Commit your changes.
4. Push the branch.
5. Open a Pull Request.

---

# 📄 License

This project is licensed under the **MIT License**.

---

# 👨‍💻 Author

## Shubham Sudhakar Pashte

Diploma in Computer Science & Engineering Student

Cybersecurity Enthusiast | Python Learner 

### GitHub

https://github.com/pashteshubham9-afk

### Repository

https://github.com/pashteshubham9-afk/Network-Packet-Analyzer

### LinkedIn

https://www.linkedin.com/in/YOUR-LINKEDIN-USERNAME/

---

# ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

Your support motivates me to build more open-source cybersecurity projects.
