from extractdata import ipS,portS,typeS
import asyncio

"""The empty lists for dividing the proxy into the some classes.The modification is according to SOCKS5 protocol. """

disipSOCKS5 = []
disportSOCKS5 = []
distypeSOCKS5 = []
#!socks 5 proxies
#*###############################################################################################
"""The empty lists for dividing the proxy into the some classes.The modification is according to SOCKS4 protocol. """

socks4ip = []
socks4port = []
socks4type = []


#*#########################################################################################################

""" The empty lists for dividing the proxy into the some classes.The modification is according to SOCKS5 and SOCKS4 protocol. """

socks45ip = []
socks45port = []
socks45type = []



#*#####################################################################################################################

async def distribute_proxy():
    try:
        """That will divide the proxies into the Separated classes."""
        global ipS, portS, typeS, disipSOCKS5, disportSOCKS5, distypeSOCKS5,socks4ip,socks4port,socks4type,socks45ip,socks45port,socks45type
        #* Declare the above vraibles as an global variable
        for ip, port, typ in zip(ipS, portS, typeS): #* Creating a FOR loop to iterate over the three lists which made by the C++ sqlite3 database.using Zip for iterating over multiply iterables
            #!Remember that the index of the above lists are sorted and match with each other (Index by Index).
            if typ == "SOCKS5": #* This will check if the proxyserver type is SOCKS5
                disipSOCKS5.append(ip) #* That will append the items to the initialize list that created at the beginning of the program
                disportSOCKS5.append(port) #* Do the same for the port
                distypeSOCKS5.append(typ) #* do the same for the type of proxy

            elif typ == "SOCKS4": #* Do same thing for the SOCKS4
                socks4ip.append(ip) #* same thing
                socks4port.append(port) #* same thing
                socks4type.append(typ)

            elif typ == "SOCKS4, SOCKS5":
                socks45ip.append(ip)
                socks45port.append(port)
                socks45type.append(typ)

    except KeyboardInterrupt:
        print("[INFO] User exited the program")
        return False

    except Exception as e:
        print("Unexpected error:",e)
        return False

  

#! asyncio.run(distribute_proxy())

#! print(socks45ip)
#! you can run the above code for dividing the values
