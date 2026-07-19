# 🔍 Network Packet Analyzer

A Python-based **Network Packet Analyzer** developed using **Python** and **Scapy**. This project captures live network packets and displays important information such as Source IP, Destination IP, Protocol, Packet Length, and Packet Summary in real time.

It is designed as a beginner-friendly cybersecurity project to understand how network communication works and how packet sniffing can be performed ethically.

---

# 📖 About the Project

The **Network Packet Analyzer** is a simple cybersecurity tool that captures live network traffic using the Scapy library. It analyzes each packet and extracts useful information, allowing users to understand how data travels between devices over a network.

This project was developed as part of a cybersecurity learning journey and demonstrates the fundamentals of packet sniffing, protocol analysis, and network monitoring using Python.

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
- Networking Fundamentals

---

# 📂 Project Structure

```text
Network-Packet-Analyzer/
│
├── packet_analyzer.py
├── requirements.txt
├── README.md
├── screenshots/
│   ├── output1.png
│   └── output2.png
│
└── LICENSE
```

---

# 📋 Requirements

- Python 3.x
- Scapy
- Npcap (Required on Windows)
- Administrator Privileges
- VS Code (Optional)

---

# ⚙ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/pashteshubham9-afk/CODSOFT_CYBER_SECURITY.git
```

## 2. Open the Project Folder

```bash
cd CODSOFT_CYBER_SECURITY
```

## 3. Install Dependencies

```bash
pip install scapy
```

or

```bash
pip install -r requirements.txt
```

---

# ▶ Running the Project

Run the program with Administrator privileges.

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

Example:

```text
screenshots/output1.png
screenshots/output2.png
```

Display them like this:

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
5. Identifies the network protocol.
6. Calculates packet length.
7. Displays packet information in real time.

---

# 📚 Concepts Used

- Packet Sniffing
- IP Packet Analysis
- TCP
- UDP
- ICMP
- Networking Basics
- Scapy Library
- Cybersecurity Fundamentals

---

# 🎯 Future Improvements

- GUI Interface using Tkinter
- Save Captured Packets to PCAP
- Export Packet Details to CSV
- Advanced Packet Filtering
- DNS Packet Analysis
- HTTP/HTTPS Packet Inspection
- Live Traffic Statistics
- Network Traffic Dashboard

---

# ⚠ Disclaimer

This project is developed **only for educational and ethical purposes**. Capture network traffic only on networks that you own or have permission to monitor.

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Push the branch
5. Open a Pull Request

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Shubham Sudhakar Pashte**

Diploma in Information Technology Student  
Cybersecurity & Python Enthusiast

### GitHub

https://github.com/pashteshubham9-afk

### LinkedIn

https://www.linkedin.com/in/YOUR-LINKEDIN-USERNAME/

---

# ⭐ Support

If you found this project helpful, please consider giving this repository a ⭐ on GitHub.
