import asyncio
import InsertProxy
from extractdata import extract_data_from_database
import threading
from checkdependencies import check_for_proxy_chains_installation,check_for_system_tor_installation,install_system_tor

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
    print(logo)
    while True:
        start = input("Please enter Yes to start the process and Type 'exit' to exit the program.")
        match start:
            case "Yes":
                tasks = [
                    asyncio.to_thread(check_for_proxy_chains_installation),
                    check_for_system_tor_installation()
                ]

                results = await asyncio.gather(*tasks)

                if all(results):
                    print("All dependencies are installed.")
                    tasksNext = [
                        extract_data_from_database(),
                        InsertProxy.insert_proxies_to_config()
                    ]
                    resultNext = await asyncio.gather(*tasksNext)
                    if all(resultNext):
                        print("Proxies inserted successfully!")
                        print("All th tasks has been\n done.Please enter /etc/proxychains4.conf \nfile and remove the # of the dynamic chain and add #\n for strict chain to be able to use proxy chains.")
            case "no":
                exit()

asyncio.run(main())
