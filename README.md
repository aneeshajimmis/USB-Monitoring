# USB Device Control & Monitoring Framework

A Python-based USB security monitoring framework developed on Kali Linux for detecting, monitoring, and auditing USB device activity.

## Project Overview

This project provides real-time monitoring of USB devices and file activities within connected storage devices. It maintains an allowlist of authorized USB devices and logs all authorized and unauthorized device connections.

The framework also tracks file creation, modification, and deletion events while generating SHA-256 hashes for integrity verification.

## Features

### USB Device Monitoring
- Detects USB device insertion and removal
- Captures Vendor ID, Product ID, and Serial Number
- Allowlist-based device authorization
- Identifies unauthorized USB devices
- Real-time monitoring using PyUDev

### File Activity Monitoring
- Detects file creation
- Detects file modification
- Detects file deletion
- Monitors directories recursively using Watchdog

### File Integrity Verification
- Generates SHA-256 hashes
- Tracks content changes through hash comparison
- Logs hash values for auditing

### Logging & Auditing
- Detailed audit logs
- Authorized and unauthorized device tracking
- File activity logging
- Timestamped event records

### Security Reporting
- Generates security reports
- Displays device statistics
- Displays file activity statistics
- Maintains audit trail

---

## Technologies Used

- Python 3
- PyUDev
- Watchdog
- Hashlib
- JSON
- Logging Module
- Kali Linux
- VirtualBox

---

## Project Structure

```text
USB-Monitoring/
│
├── usb_monitor.py
├── allowlist.json
├── usb_audit.log
├── report.txt
├── test_usb/
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/aneeshajimmis/USB-Monitoring.git
cd USB-Monitoring
```

### Install Dependencies

```bash
pip install pyudev watchdog
```

---

## Configuration

Add authorized USB devices inside:

```json
{
  "devices": [
    {
      "vendor": "05ac",
      "product": "12a8",
      "serial": "00008120001665AE1ED8C01E"
    }
  ]
}
```

---

## Running the Framework

```bash
python3 usb_monitor.py
```

The framework will:

- Monitor USB device events
- Detect authorized devices
- Detect unauthorized devices
- Monitor file activities
- Generate audit logs

---

## Example Output

```text
Action : add
vendor : 05ac
product : 12a8
serial : 00008120001665AE1ED8C01E

Authorized Device
```

### File Monitoring

```text
File created:
./test_usb/test.txt

SHA256:
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

---

## Log File Example

```text
AUTHORIZED | Action=add | Vendor=05ac | Product=12a8

File Modified | ./test_usb/test.txt
SHA256=5891b5b522d5df086d0ff0b110fbd9d21bb4fc7163af34d08
```

---

## Security Report Example

```text
USB SECURITY REPORT

Total devices seen : 4
Authorized devices : 2
Blocked devices : 2

Files Created : 1
Files Modified : 7
Files Deleted : 1
```

---

## Testing Environment

### Host System
- macOS
- VirtualBox

### Virtual Machine
- Kali Linux

### Test Device
- Apple iPhone

USB devices were attached to the Kali Linux virtual machine through VirtualBox USB passthrough functionality.

---

## Learning Outcomes

- USB device monitoring using PyUDev
- File system monitoring using Watchdog
- USB allowlisting concepts
- Security auditing and logging
- File integrity verification using SHA-256
- Linux device event handling
- Virtual machine USB passthrough

---

## Future Enhancements

- GUI Dashboard
- Database Logging
- Email Alerts
- Device Blocking Automation
- Real-time Threat Detection
- PDF Report Generation
- Web-Based Monitoring Dashboard

---

## Author

**Aneesha Jimmis**

Cybersecurity Enthusiast | Network Security | Digital Forensics

GitHub:
https://github.com/aneeshajimmis

---

## License

This project is developed for academic and educational purposes.
