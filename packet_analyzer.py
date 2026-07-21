from scapy.all import sniff, IP, TCP, UDP, ICMP
from datetime import datetime

packet_count = 0

def analyze_packet(packet):
    global packet_count
    packet_count += 1

    print("=" * 70)
    print(f"Packet No : {packet_count}")
    print(f"Time      : {datetime.now().strftime('%H:%M:%S')}")

    if packet.haslayer(IP):
        print(f"Source IP        : {packet[IP].src}")
        print(f"Destination IP   : {packet[IP].dst}")

        if packet.haslayer(TCP):
            print("Protocol         : TCP")
            print(f"Source Port      : {packet[TCP].sport}")
            print(f"Destination Port : {packet[TCP].dport}")

        elif packet.haslayer(UDP):
            print("Protocol         : UDP")
            print(f"Source Port      : {packet[UDP].sport}")
            print(f"Destination Port : {packet[UDP].dport}")

        elif packet.haslayer(ICMP):
            print("Protocol         : ICMP")

        else:
            print(f"Protocol Number  : {packet[IP].proto}")

        print(f"Packet Length    : {len(packet)} Bytes")

    else:
        print("Non-IP Packet Captured")

    print("=" * 70)
    print()


print("=" * 50)
print("      Network Packet Analyzer")
print("=" * 50)
print("Capturing 20 packets...")
print("Press Ctrl + C to Stop\n")

try:
    sniff(prn=analyze_packet, count=20, store=False)

except PermissionError:
    print("\nRun this program as Administrator.")

except KeyboardInterrupt:
    print("\nPacket Capture Stopped.")