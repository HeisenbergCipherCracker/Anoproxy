import re
import asyncio

"""Creates an empty list for retrieving the data from the C++ sqlite3 database. """
#######################################################################################
ipS = []
portS = []
typeS = []
########################################################################################


async def extract_data_from_database():
    try:
        """This coroutine will extract the data from the sqlite3 C++"""
        file = "output.txt" #* Indicating the output.txt file as an target file

        with open(file, "r") as file: #* opening the file as read mode
            data = file.read() #* read the file data

        #* Define the regular expressions to match the desired fields
        ip_pattern = r"ip_address:\s+([\d\.]+)" #* Use regex to find the ipaddress pattern in the output.txt file
        port_pattern = r"port:\s+(\d+)" #* Do the same for the port 
        type_pattern = r"type:\s+([A-Z0-9, ]+)" #* Do the same for the proxy type
        #! The reason that we are just extracting the IP,Port and the type is only these information are needed for proxychaining 

        #* Use regular expressions to extract all the data
        ip_matches = re.findall(ip_pattern, data)  #*use regex to extract the ip
        port_matches = re.findall(port_pattern, data) #* Doing the same for port
        type_matches = re.findall(type_pattern, data) #* Doing the same for the proxy type

        #* Iterate over the matches and print the extracted information
        for i in range(len(ip_matches)): #* Iterate over the matches
            global portS,ipS,typeS #* Declaring these three lists as an global variable 
            ip = ip_matches[i] if i < len(ip_matches) else "" #* Use conditions
            port = port_matches[i] if i < len(port_matches) else ""
            proxy_type = type_matches[i] if i < len(type_matches) else ""

            print("IP Address:", ip) #* Printing the values
            print("Port:", port)
            print("Proxy Type:", proxy_type)
            print()
            ipS.append(ip)
            portS.append(port)
            typeS.append(proxy_type)
    
    except Exception as e:
        print("Unexpected error:",e)
        return False
    
    except KeyboardInterrupt:
        print("[INFO] User exited the program")
        return False

#? asyncio.run(extract_data_from_database())
#? you can run it for extracting data
#TODO: you can use if __name__ == "__main__" to prevent the conflict while importing this file as an module

# print(ipS)
# print(typeS)
# print(portS)
