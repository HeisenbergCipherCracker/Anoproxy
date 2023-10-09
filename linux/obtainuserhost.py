import socket
import asyncio

async def get_host():
    try:
        host_name = socket.gethostname()
        return host_name
    except Exception as e:
        return f"An error occurred: {e}"

async def main():
    host = await get_host()  # Await the result of get_host coroutine
    return host

result = asyncio.run(main())  # Run the main coroutine and capture the result
print(f"User host: {result}")  # Print the result
