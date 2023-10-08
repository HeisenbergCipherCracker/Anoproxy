import subprocess
import asyncio
import re
from colorama import Fore, init

init()

async def check_for_proxy_chains_installation():
    """This will check for the installation of the proxychains if installed."""
    try:
        # Check if proxychains is installed
        subprocess.run(["proxychains"], capture_output=True, check=True)
    except FileNotFoundError:
        ask = input(Fore.BLUE + "[INFO] Proxychains is not installed, do you want to install it? (yes/no)")
        if ask == "yes":
            try:
                # Install proxychains using apt
                subprocess.run(["sudo", "apt", "install", "-y", "proxychains"], check=True)
                subprocess.run(["sudo", "apt", "install", "-y", "proxychains4"], check=True)
                print(Fore.GREEN + "[SUCCESS] Proxychains installed successfully.")
                # TODO: Complete Here
            except subprocess.CalledProcessError as e:
                print(Fore.RED + f"[ERROR] Failed to install Proxychains: {e}")
                # TODO: Complete Here
        elif ask == "no":
            print(Fore.RED + "[ERROR] Proxychains is not installed")
            # TODO: Complete Here

    except subprocess.CalledProcessError:
        print(Fore.BLUE+"[INFO] It seems like that the proxycinas is installed. please check by running command (proxychains)")


# asyncio.run(check_for_proxy_chains_installation())

