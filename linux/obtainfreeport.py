import socket
import asyncio
free_ports = []


async def find_free_ports(num_ports):
    global free_ports
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('localhost', 0))
    
    for _ in range(num_ports):
        sock.listen(1)
        port = sock.getsockname()[1]
        free_ports.append(port)
        sock.close()
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(('localhost', 0))
    
    sock.close()
    return free_ports


def main():

    # Specify the number of free ports you want to find
    num_ports = 5

    # Call the function to find free ports
    free_ports = asyncio.run(find_free_ports(num_ports))

    # Print the list of free ports
    print("Free Ports:")
    for port in free_ports:
        print(port)

main()
