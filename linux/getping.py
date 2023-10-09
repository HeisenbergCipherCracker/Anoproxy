import socket
import asyncio
import ping3

async def get_host():
    """ This will get the host name of the current. """
    try:
        host_name = socket.gethostname() #* get the current host name of user
        return host_name #* returns the hostname
    except Exception as e:
        return f"An error occurred: {e}" #* return the exception if occurred

async def main():
    """This will send an ICMP message to obtain the user ping. """
    host = await get_host()  #*  this will await and pause the coroutine task until the get_host function task is Done. 
    pingtime = ping3.ping(host) #* This will get the user ping with an ICMP message protocol.
    return host, pingtime #* returns the host and pingtime values

async def run():
    """ This will execute the two above coroutine tasks and run it """
    host, pingtime = await main() #* pause the program till the main function task is done.
    print(f"User host: {host}") #* Prints the host
    if pingtime is not None: #* Shows the ping if not None value
        print(f"Ping time: {pingtime}") #* shows the ping time
    else:
        print("Ping failed") #* shows a message if the value was None type

asyncio.run(run())  #* Run the run coroutine and entire task