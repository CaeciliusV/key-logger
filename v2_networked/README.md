# Networked Python Key Logger

## Status: Complete

This is a software surveillance tool that is able to listen to the client's keyboard and record every keystroke and send it to the server to be saved onto a txt file. I built it to understand how keylogging remotely works and the utility of it.

This project is part of a bigger series in which I learn real-world cybersecurity skills alongside my T Level

## What it does

- Listens to client's keyboard
- Sends recorded keystrokes as bytes from client to server
- Server decodes bytes to readable string
- Create, open and write in a file
- Record in batches every 30 seconds
- Works in the background
- Works remotely (Within a home network)

## What I learned

- How remote keylogging works
- What sockets are and how they work
- What threading does
- How real malware exfiltrates data
- Encoding and Decoding to send data
- IP and Ports
- Network monitoring
- What Endpoint Detection (EDR) is and how it works
- Why EDR would flag this program and what EDR looks for 

## How to run it

- NOTE: You will need two devices that you have full permission to test this on - One as a server and one as a client. Both devices will also need to be on the same network and have Python installed.

1. Download or clone this repository
2. Have pynput installed on both devices
3. Run key_log_v2_server on the server device
4. Run key_log_v2_client on the client device
5. Start typing anything on the client device
   e.g. "Hello welcome to my remote key logger"
   This can be written anywhere and on anything, even on nothing
6. Press 'Esc' to stop logging
7. Type something else
   e.g. "Thank You for using my key logger"
8. Open the file named: key_log_file.txt
   
## Example output

2026-04-19 15:38:56.248950
[SHIFT] hello welcome to my key logger [BACKSPACE]

## Limitation
- Does not record mouse
- Can only record other devices on the same network as the server device
- Server device cannot pause or end logging only client device can

## Tools used
- Python 3
- pynput (pip install pynput)
- key_log_file.txt 

## WARNING!
Please know this is essentially real malware and as such is ILLEGAL to use on any machines WITHOUT permission!
This tool was made for educational purposes only!
This tool is significantly more powerful than v1 as this works remotely so use with caution.

## Ethical Note
This tool was made for educational purposes only.
Using this tool on any machine without permission is illegal.
