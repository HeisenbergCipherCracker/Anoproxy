import disturbuteProxy
import asyncio
import InsertProxy
from disturbuteProxy import disipSOCKS5, disportSOCKS5, distypeSOCKS5

############################################################################################################
Iter_for_Ip_Socks5 = []
Iter_for_Port_Socks5 = []
Iter_for_Type_Socks5 = []
############################################################################################################
socks5_split_ip = []
socks5_split_port = []
socks5_split_type = []
#############################################################################################################################



async def distribute_among_the_users_according_to_socks5_for_special_policy():
    # await disturbuteProxy.insert_proxies_to_config()
    task1 = asyncio.create_task(disturbuteProxy.distribute_proxy())
    task2 = asyncio.create_task(InsertProxy.insert_proxies_to_config())
    
    result = await asyncio.gather(task1, task2)
    
    if all(result):
        global Iter_for_Ip_Socks5, Iter_for_Port_Socks5, Iter_for_Type_Socks5,socks5_split_ip,socks5_split_port,socks5_split_type
        Dip = iter(disipSOCKS5)
        Dport = iter(disportSOCKS5)
        Dtype = iter(distypeSOCKS5)
        count = 0
        for ip, port, typ in zip(Dip, Dport, Dtype):
            count += 1
            if count == 10:
                break
            Iter_for_Ip_Socks5.append(next(ip))
            Iter_for_Port_Socks5.append(next(Dport))
            Iter_for_Type_Socks5.append(next(Dtype))
            split_index_for_ip = len(Iter_for_Ip_Socks5)
            split_index_for_port = len(Iter_for_Port_Socks5)
            split_index_for_type = len(Iter_for_Type_Socks5)
            socks5_split_ip.append(Iter_for_Ip_Socks5[split_index_for_ip-10:split_index_for_ip])
            socks5_split_port.append(Iter_for_Port_Socks5[split_index_for_port-10:split_index_for_port])
            socks5_split_type.append(Iter_for_Type_Socks5[split_index_for_type-10:split_index_for_type])
    # return socks5_split_ip,socks5_split_port,socks5_split_type
    #? return all of them

asyncio.run(distribute_among_the_users_according_to_socks5_for_special_policy())

print(socks5_split_port)