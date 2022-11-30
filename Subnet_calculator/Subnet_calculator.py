is a sample Python script.

import math

import re

#Given an IP address as input,
#the task is to write a Python program to check whether the given IP Address is Valid or not

def is_ip(ip_address): #asd127.21.12.2

    ip_regex="^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$"

    ip_regex_2="^([0-9]{1,3}\.){3}[0-9]{1,3}$"

    ip_regex_3="^(((25[0-5])|(2[0-4][0-9])|([0-1][0-9][0-9])|([0-9][0-9]?))\.){3}((25[0-5])|(2[0-4][0-9])|([0-1][0-9][0-9])|([0-9][0-9]?))"

    if not re.search(ip_regex_2, ip_address):

        print(f"The IP address {ip_address} is not valid")

        return False

    octa = ip_address.split(".")

    for ip_octa in octa:

        if int(ip_octa) < 0 or int(ip_octa) > 255:

            print(f"The IP address {ip_address} is not valid")

            return False

    print(f"The IP address {ip_address} is valid")

    return True
