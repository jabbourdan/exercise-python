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

def get_cidr(ip_address):

    cidr=0

    ip=ip_address.split(".") #Splitting the ip

    num=int(ip[0]) #getting the first octet

    if(num>=0 and num<=127): #class A       # (0 <= num <=127)

         cidr=8

    elif(num>127 and num<=191): #class B

       cidr=16

    elif(num>=192 and num<=223): #class C

        cidr=24

    return cidr

def get_subnet(ip, cidr):
    if (cidr < 32):
        octa = cidr//8                                     #ocat-1
        target_octa_value = int(ip.split(".")[octa])
        host_bit = 8 - cidr % 8                          #every octa 8 bits
        group_size = 2 ** host_bit
        octa_subnet_id = target_octa_value-(target_octa_value % group_size)
        new_ip = "" #192.168.135.31/23 -> 192.168.135.0
        octa_index = 0
        while (octa_index < 4):
            if (octa_index < octa):
                new_ip += ip.split(".")[octa_index]+"."
            elif (octa_index == octa):
                new_ip += str(octa_subnet_id)
                if (octa_index <3 ):
                    new_ip +="."
            else:
                new_ip +="0"
                if (octa_index < 3):
                    new_ip += "."
            octa_index += 1
        print(new_ip)
    else:
        print(ip)

        
def get_subnetmask(cidr):
    octa=cidr//8
    subnet_bits_in_octa=8-cidr%8
    subnet_num=256-2**subnet_bits_in_octa
    index=0
    subnetmask=""
    while index < 4:
        if(index<octa):
            subnetmask += "255"+"."
        elif(index==octa):
            subnetmask += str(subnet_num) + "."
        else:
            subnetmask += "0"
        index+=1
    return subnetmask

# Input positive number
def get_bits_number(num):
    bit = math.log2(num)
    return math.ceil(bit)
