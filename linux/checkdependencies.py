import subprocess
import asyncio
import re
# from colorama import Fore, init

# init()

async def check_for_proxy_chains_installation():
    """This will check for the installation of the proxychains if installed."""
    try:
        # Check if proxychains is installed
        res = subprocess.run(["proxychains"], capture_output=True, check=True)
        if res.returncode == 0:
            print("[INFO] Proxychains is installed")
            # TODO: Complete Here
            return True

        else:
            return False
    except FileNotFoundError:
        ask = input("[INFO] Proxychains is not installed, do you want to install it? (yes/no)")
        if ask == "yes":
            try:
                # Install proxychains using apt
                subprocess.run(["sudo", "apt", "install", "-y", "proxychains"], check=True)
                subprocess.run(["sudo", "apt", "install", "-y", "proxychains4"], check=True)
                print("[SUCCESS] Proxychains installed successfully.")
                # TODO: Complete Here
                return True
            except subprocess.CalledProcessError as e:
                print( f"[ERROR] Failed to install Proxychains: {e}")
                # TODO: Complete Here
                return False
        elif ask == "no":
            print("[ERROR] Proxychains is not installed")
            # TODO: Complete Here
            return False

    except subprocess.CalledProcessError:
        print("[INFO] It seems like that the proxycinas is installed. please check by running command (proxychains)")


# asyncio.run(check_for_proxy_chains_installation())

# import subprocess

async def check_for_system_tor_installation():
    try:
        output = subprocess.check_output(["which", "tor"]).decode().strip()
        if output:
            # print("ok")
            return True
        else:
            # print("00")
            return False
    except subprocess.CalledProcessError:
        # prin)
        return False

async def install_system_tor():
    try:
        subprocess.run(["sudo", "apt", "install", "-y", "tor"], check=True)
        print("System Tor installed successfully.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Failed to install System Tor: {e}")
        return False


