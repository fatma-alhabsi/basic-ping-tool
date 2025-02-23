import os
import platform

def ping_host(host):
    # Determine the ping command based on OS
    command = "ping -n 1 " + host if platform.system().lower() == "windows" else "ping -c 1 " + host
    response = os.system(command)

    if response == 0:
        print(f"{host} is reachable ✅")
    else:
        print(f"{host} is unreachable ❌")

# Example Usage
if __name__ == "__main__":
    target = input("Enter IP or domain to ping: ")
    ping_host(target)
