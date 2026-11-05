# Python Port Scanner

## Project Overview

Python Port Scanner is a basic network security tool developed using Python and Socket Programming. It is designed to scan TCP ports on a target IP address and identify which ports are open and which do not accept connection attempts.

The tool helps users understand network port scanning, TCP connections, and basic network security concepts. It runs through a command-line interface on Kali Linux.

## Features

- **Target IP Selection:** Allows users to enter the IP address of the system they want to scan.
- **Single Port Scanning:** Scans one specific port selected by the user.
- **Port Range Scanning:** Allows users to scan a custom range of ports by specifying starting and ending port numbers.
- **Common Port Scanning:** Provides a predefined list of commonly used ports for quick scanning.
- **Open Port Detection:** Identifies ports where a TCP connection is successfully established.
- **Connection Status:** Displays ports that do not accept a connection attempt as closed/filtered.
- **Scan Completion Status:** Displays a message when the scanning process is completed.

## Technologies Used

- Python 3
- Socket Programming
- TCP/IP Networking
- Kali Linux

## How It Works

1. The user enters the target IP address.
2. The user selects a scanning option.
3. Based on the selection, the tool determines which ports to scan.
4. The scanner attempts to establish a TCP connection with each selected port.
5. It checks the connection response to determine whether the port is open.
6. The scanning results are displayed in the terminal.

## Purpose

The main purpose of this project is to develop a basic understanding of network reconnaissance and port scanning using Python. It demonstrates how socket programming can be used to identify accessible network services.

## Disclaimer

This tool is developed for educational and authorized security testing purposes only. Users should scan only systems they own or have explicit permission to test.
## Screenshots

### Single Port Scan
![Single Port Scan](Python%20Port%20Scanner%20(1st%20Pic).png)

### Port Range Scan
![Port Range Scan](Python%20Port%20Scanner%20(2nd%20Pic).png)

### Common Ports Scan
![Common Ports Scan](Pythin%20Port%20Scanner%20(3rd%20pic).png)

### Scan Output
![Scan Output](Python%20Port%20Scanner%20(4th%20Pic).png)

### Scan Completed
![Scan Completed](Python%20Port%20Scanner%20(5th%20Pic).png)

### Additional Result
![Additional Result](Python%20Port%20Scanner%20(6th%20pic).png)
