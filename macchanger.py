import subprocess
import random
import re

def get_random_mac_address():
    """Generate and return a random MAC address."""
    uppercased_hexdigits = ''.join(set("0123456789ABCDEF"))
    mac = ""
    for i in range(6):
        for j in range(2):
            if i == 0:
                mac += random.choice("02468ACE")
            else:
                mac += random.choice(uppercased_hexdigits)
        mac += ":"
    return mac.strip(":")

def get_current_mac_address(interface):
    """Get the current MAC address of the specified interface."""
    output = subprocess.check_output(f"ifconfig {interface}", shell=True).decode()
    return re.search(r"ether (.+) ", output).group(1)

def change_mac_address(interface, new_mac_address):
    """Change the MAC address of the specified interface."""
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac_address])
    subprocess.call(["ifconfig", interface, "up"])

if _name_ == "_main_":
    interface = "eth0"  # Change this to your network interface
    new_mac = get_random_mac_address()
    print(f"Changing MAC address for {interface} to {new_mac}")
    change_mac_address(interface, new_mac)
    print(f"New MAC address: {get_current_mac_address(interface)}")
