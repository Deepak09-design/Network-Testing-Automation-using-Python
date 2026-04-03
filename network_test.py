import os
import platform
from datetime import datetime

# List of IP addresses to test
ip_list = ["8.8.8.8", "1.1.1.1", "192.168.1.1", "10.0.0.1"]

# Detect OS and set ping parameter
param = "-n" if platform.system().lower() == "windows" else "-c"

# Log file name
log_file = "network_test_log.txt"

def ping_ip(ip):
    """Ping a single IP and return True if reachable"""
    command = f"ping {param} 1 {ip}"
    response = os.system(command)
    return response == 0

def log_result(ip, status):
    """Write result to log file"""
    with open(log_file, "a") as file:
        file.write(f"{datetime.now()} - {ip} is {status}\n")

def main():
    print("\n🔍 Starting Network Testing Automation...\n")
    
    up_count = 0
    down_count = 0

    for ip in ip_list:
        result = ping_ip(ip)
        status = "UP" if result else "DOWN"
        
        print(f"{ip} is {status}")
        log_result(ip, status)

        if result:
            up_count += 1
        else:
            down_count += 1

    print("\n📊 Summary:")
    print(f"UP: {up_count} | DOWN: {down_count}")
    print("\n✅ Testing completed. Check log file for details.\n")

if __name__ == "__main__":
    main()