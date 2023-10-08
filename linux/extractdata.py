import re
import asyncio


async def extract_data_from_database():
    file = r"D:\Anoproxy\Anoproxy\linux\output.txt"

    with open(file, "r") as file:
        data = file.read()

    # Define the regular expressions to match the desired fields
    ip_pattern = r"ip_address:\s+([\d\.]+)"
    port_pattern = r"port:\s+(\d+)"
    type_pattern = r"type:\s+([A-Z0-9, ]+)"

    # Use regular expressions to extract all the data
    ip_matches = re.findall(ip_pattern, data)
    port_matches = re.findall(port_pattern, data)
    type_matches = re.findall(type_pattern, data)

    # Iterate over the matches and print the extracted information
    for i in range(len(ip_matches)):
        ip = ip_matches[i] if i < len(ip_matches) else ""
        port = port_matches[i] if i < len(port_matches) else ""
        proxy_type = type_matches[i] if i < len(type_matches) else ""

        print("IP Address:", ip)
        print("Port:", port)
        print("Proxy Type:", proxy_type)
        print()

asyncio.run(extract_data_from_database())