from extractdata import ipS,portS,typeS
import asyncio

disipSOCKS5 = []
disportSOCKS5 = []
distypeSOCKS5 = []
#!socks 5 proxies
#*###############################################################################################
socks4ip = []
socks4port = []
socks4type = []


#*#########################################################################################################

socks45ip = []
socks45port = []
socks45type = []



#*#####################################################################################################################

async def distribute_proxy():
    global ipS, portS, typeS, disipSOCKS5, disportSOCKS5, distypeSOCKS5,socks4ip,socks4port,socks4type,socks45ip,socks45port,socks45type
    for ip, port, typ in zip(ipS, portS, typeS):
        if typ == "SOCKS5":
            disipSOCKS5.append(ip)
            disportSOCKS5.append(port)
            distypeSOCKS5.append(typ)

        elif typ == "SOCKS4":
            socks4ip.append(ip)
            socks4port.append(port)
            socks4type.append(typ)

        elif typ == "SOCKS4, SOCKS5":
            socks45ip.append(ip)
            socks45port.append(port)
            socks45type.append(typ)

        

asyncio.run(distribute_proxy())

print(socks45ip)
