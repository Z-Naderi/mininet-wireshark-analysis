# Mininet Wireshark Analysis

This repository contains the results and documentation of a practical network analysis project using **Mininet**, **Wireshark**, and the **Ryu OpenFlow Controller**.

## 🔧 Tools Used
- **Mininet** – to emulate network topologies and hosts
- **Wireshark** – to capture and analyze network traffic
- **Ryu Controller** – a software-defined networking controller used to manage switch behavior

## 📁 Repository Structure

```
.
├── traffic-analysis/      # Analysis of ARP, ICMP, and OpenFlow packets during initial topology run
├── openflow-messages/     # Feature Request/Reply and Packet-In message inspection
├── ping-test/             # Ping tests and ICMP packet evaluation between hosts
└── README.md              # Project documentation (this file)
```

## 🧪 Project Objectives

1. **Traffic Analysis in Mininet**
   - Observe and analyze ARP, ICMP, and OpenFlow packets
   - Understand the reason each protocol is used during topology initialization

2. **OpenFlow Message Exchange**
   - Identify and interpret Feature Request and Feature Reply messages
   - Detect Packet-In messages sent when switches lack matching flow entries

3. **Ping Communication Test**
   - Validate connectivity using ping between Mininet hosts
   - Capture ICMP Echo Request and Reply packets using Wireshark

## 🖼 Documentation
Each folder contains screenshots and `.pcapng` captures that illustrate specific protocol behaviors as observed in Wireshark.


