# libraries needed
import os
import platform
import subprocess

#Function for pinging the subnet IP address
def subnet_ping(ip_address, count=4):
    # to determine the operating system
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, str(count), ip_address]
    try:
        # Execute the ping command
        output = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return output.returncode == 0  # Return True if ping was successful
    except Exception as e:
        print(f"An error occurred while pinging {ip_address}: {e}")
        return False


# logfile to store  result
output_file = "ping_results.txt"

#clear or create the output file if it does exist or not
with open(output_file, 'w') as f:
    #clear the file
    f.write("")


# Getting the user input for each subnet IP Address
subnet_ip_list = input("\nEnter the default gateway IP address for each subnet you want to ping, seperated by commas: ").split(',')

#Stripping the whitespace from each IP address
subnet_ip_list = [ip_address.strip() for ip_address in subnet_ip_list]
pi = '142.250.178.142'
#looping through each IP adresses and pinging each IP
for ip in subnet_ip_list:
    if subnet_ping(ip):
        result = f" {ip} is online"
        print(f"{result}")
    else:
        result = f" {ip} is offline"
        print(f"{result}")

    # Appending or adding the  result into the output file
    with open(output_file, 'a') as f :
        f.write(result + '\n')


print(f"\nResult of the ping is saved to {output_file}\n\nThank you for using this app!!!")