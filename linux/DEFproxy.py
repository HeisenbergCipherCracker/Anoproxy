import extractdata
import asyncio
from extractdata import ipS,portS,typeS #* we may need that 
# from Updateddatabase import datalistIP,datalistPORT,datalistTYPE

async def insert_proxies_to_config_default(ipS=ipS, portS=portS, typeS=typeS):
    """This coroutine function will Insert the extracted values into the file /etc/proxychains4.conf """
    try:
        config_file = "/etc/proxychains4.conf"  #* Declaring the config file

        #* Read the contents of the config file
        with open(config_file, "r") as file:
            config_lines = file.readlines()

        #* Find the desired section in the config file
        proxy_list_start = None
        for i, line in enumerate(config_lines):
            if line.startswith("[ProxyList]"):
                proxy_list_start = i + 1
                break

        if proxy_list_start is not None:
            # Construct new proxy lines from the provided lists
            global datalistIP,datalistPORT,datalistTYPE
            new_proxy_lines = [f"{proxy_type} {ip} {port}\n" for ip, port, proxy_type in zip(ipS,portS,typeS)]

            # Insert the new proxy lines into the config file
            config_lines[proxy_list_start:proxy_list_start] = new_proxy_lines

            #TODO: Modify the config lines to enable dynamic_chain and disable strict_chain
            for i, line in enumerate(config_lines):
                if line.startswith("dynamicchain"):
                    #? Convert to dymanicchain?
                    # Remove the # from the beginning of the line if present
                    if config_lines[i].startswith("#"):
                        config_lines[i] = config_lines[i][1:].lstrip()

                elif line.startswith("strict_chain"):
                    config_lines[i] = "#strict_chain\n"

            #* Write the updated contents back to the config file
            with open(config_file, "w") as file:
                file.writelines(config_lines)

            print("Proxies inserted successfully!")
    except Exception as e:
        print(e)
        return False

    except KeyboardInterrupt:
        print("[INFO] User exited the program")
        return False