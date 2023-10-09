import socket
import asyncio

def get_host():
    try:
        host_name = socket.gethostname()
        return host_name
    except Exception as e:
        return f"An error occurred: {e}"

# Example usage
host = get_host()
print(f"User host: {host}")