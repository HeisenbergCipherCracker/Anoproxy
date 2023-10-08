import extractdata
import asyncio
from extractdata import ipS,portS,typeS
from checkdependencies import check_for_proxy_chains_installation


async def insert_proxies_to_config(ipS=ipS, portS=portS, typeS=typeS):
    try:
        config_file = "/etc/proxychains4.conf"

        # Read the contents of the config file
        with open(config_file, "r") as file:
            config_lines = file.readlines()

        # Find the desired section in the config file
        proxy_list_start = None
        for i, line in enumerate(config_lines):
            if line.startswith("[ProxyList]"):
                proxy_list_start = i + 1
                break

        if proxy_list_start is not None:
            # Construct new proxy lines from the provided lists
            new_proxy_lines = [f"{proxy_type} {ip} {port}\n" for ip, port, proxy_type in zip(ipS, portS, typeS)]

            # Insert the new proxy lines into the config file
            config_lines[proxy_list_start:proxy_list_start] = new_proxy_lines

            # Modify the config lines to enable dynamic_chain and disable strict_chain
            for i, line in enumerate(config_lines):
                if line.startswith("dynamic_chain"):
                    # Remove the # from the beginning of the line if present
                    if config_lines[i].startswith("#"):
                        config_lines[i] = config_lines[i][1:].lstrip()

                elif line.startswith("strict_chain"):
                    config_lines[i] = "#strict_chain\n"

            # Write the updated contents back to the config file
            with open(config_file, "w") as file:
                file.writelines(config_lines)

            print("Proxies inserted successfully!")
    except Exception as e:
        print(e)

# Filled lists of proxy information

# Call the function
insert_proxies_to_config(ipS, portS, typeS)

# print(I)
