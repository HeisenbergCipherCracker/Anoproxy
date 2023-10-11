import asyncio
import InsertProxy
from extractdata import extract_data_from_database
import threading
from checkdependencies import check_for_proxy_chains_installation,check_for_system_tor_installation,install_system_tor
from Updateddatabase import database
import os
from DEFproxy import insert_proxies_to_config_default
import subprocess

logo = """                                                                          
                                                                                                                                  
    ___    _   ______  ____  ____  ____ _  ____  __
   /   |  / | / / __ \/ __ \/ __ \/ __ \ |/ /\ \/ /
  / /| | /  |/ / / / / /_/ / /_/ / / / /   /  \  / 
 / ___ |/ /|  / /_/ / ____/ _, _/ /_/ /   |   / /  
/_/  |_/_/ |_/\____/_/   /_/ |_|\____/_/|_|  /_/   
                                                   

                                                                                                      """
import asyncio
import threading

import asyncio

async def main():
    try:
        """This function will run all the needed coroutine functions """
        print(logo)
        while True:
            #* create a while loop over
            start = input("Please enter Yes to start the process and Type 'exit' to exit the program.type adv for advanced options:")
            match start: #* Use match for the conditional statement (similar to SWITCH in C++)
                case "Yes":
                    tasks = [
                        asyncio.to_thread(check_for_proxy_chains_installation),
                        check_for_system_tor_installation()
                    ] #* Create a task coroutine task list

                    results = await asyncio.gather(*tasks) #* Pause the program until the tasks are done

                    if all(results): #* Checks if all the tasks are done
                        print("All dependencies are installed.")
                        tasksNext = [
                            extract_data_from_database(),
                            InsertProxy.insert_proxies_to_config()
                        ]
                        resultNext = await asyncio.gather(*tasksNext)
                        if all(resultNext):
                            print("Proxies inserted successfully!")
                            print("All th tasks has been\n done.Please enter /etc/proxychains4.conf \nfile and remove the # of the dynamic chain and add #\n for strict chain to be able to use proxy chains.\n if you have problem with the program\n please run command: systemctl start tor")
                case "no":
                    exit()
                    #* Creating the same for next tasks
                    
                case "adv":
                    choice = input("[INFO]type ADD to add proxy:")
                    match choice:
                        case "ADD":
                            await database.insert_value_by_user(userIP=input("[INFO] enter the ip:"),userPORT=int(input("[INFO] enter the port:")),userTYPE=input("[INFO]enter the type:"))
                            
                case "show options":
                    ch = input("[INFO]show options menu\n type 'default' for seeing the default proxyserver\n remove proxyserver [REM]")
                    
                    match ch:
                        case "default":
                            await database.display_the_info_of_proxy_servers_table()
                            await database.display_proxy_servers_table()
                            await database.display_saved_proxy_servers()
                            await database.display_proxy_servers_table()
                            
                        case "REM":
                            command = int(input("[INFO] enter the row that you want to remove:"))
                            await database.delete_data_from_proxy_servers_table()
                            await database.display_proxy_servers_table()
                            
                case "clear":
                    os.system("clear")
                    print(logo)
                    
                case "default":
                    await database.display_the_info_of_proxy_servers_table()
                    await database.display_proxy_servers_table()
                    await database.display_saved_proxy_servers()
                    await database.display_proxy_servers_table()
                    await insert_proxies_to_config_default()
                    
                case "psconfig":
                    command = "cat /etc/proxychains4.conf"
                    subprocess.run(command,shell=True)
                    
                    
                            

    except Exception as e:
        print(e)
        return False

    except KeyboardInterrupt:
        print("[INFO] User exited the program")
        return False

asyncio.run(main())
asyncio.get_event_loop().run_until_complete(main())

