# 🔍 Network Packet Analyzer

A Python-based **Network Packet Analyzer** developed using **Python** and **Scapy**. This project captures live network packets and displays essential information such as **Source IP**, **Destination IP**, **Protocol**, **Packet Length**, and **Packet Summary** in real time.

It is designed as a beginner-friendly cybersecurity project to help understand how network communication works and how packet sniffing can be performed ethically.

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
- Networking Fundamentals

---

# 📂 Project Structure

```text
network-packet-analyzer/
│
├── packet_analyzer.py
├── requirements.txt
├── README.md
├── screenshots/
│   ├── output1.png
│   └── output2.png
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
git clone https://github.com/pashteshubham9-afk/network-packet-analyzer.git
```

## 2. Navigate to the Project Folder

```bash
cd network-packet-analyzer
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install scapy
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

Store your output screenshots inside the **screenshots** folder.

```text
screenshots/
├── output1.png
└── output2.png
```

Display them in the README using:

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
4. Extracts Source and Destination IP addresses.
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
- Scapy Library
- Cybersecurity Fundamentals

---

# 🎯 Future Improvements

- GUI using Tkinter
- Save packets as PCAP files
- Export captured data to CSV
- Advanced packet filtering
- DNS packet analysis
- HTTP/HTTPS packet inspection
- Live traffic statistics
- Network traffic visualization dashboard

---

# ⚠ Disclaimer

This project is intended **only for educational and ethical purposes**. Use it only on networks that you own or have explicit permission to monitor.

---

# 🤝 Contributing

Contributions are welcome!

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

**Shubham Sudhakar Pashte**

Diploma in Information Technology Student  
Cybersecurity Enthusiast | Python Learner

### GitHub

https://github.com/pashteshubham9-afk

### Repository

https://github.com/pashteshubham9-afk/network-packet-analyzer

### LinkedIn

https://www.linkedin.com/in/YOUR-LINKEDIN-USERNAME/

---

# ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub. Your support is greatly appreciated!
