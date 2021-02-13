import requests
import json
print(""" 
  
  _   _   ______   _    _   _______   _____     ____    _   _   _______   _______   ______    _____   _    _ 
 | \ | | |  ____| | |  | | |__   __| |  __ \   / __ \  | \ | | |__   __| |__   __| |  ____|  / ____| | |  | |
 |  \| | | |__    | |  | |    | |    | |__) | | |  | | |  \| |    | |       | |    | |__    | |      | |__| |
 | . ` | |  __|   | |  | |    | |    |  _  /  | |  | | | . ` |    | |       | |    |  __|   | |      |  __  |
 | |\  | | |____  | |__| |    | |    | | \ \  | |__| | | |\  |    | |       | |    | |____  | |____  | |  | |
 |_| \_| |______|  \____/     |_|    |_|  \_\  \____/  |_| \_|    |_|       |_|    |______|  \_____| |_|  |_|
                                                                                                             
                                         
                |++++++++++++++++++|
                |+++++İP tracer++++|
                |++++++++++++++++++|                                 
""")

from ipdata.cli import ip

ip_adress = input("IP: ")

response = requests.get(f'http://ip-api.com/json/{ip_adress}').content

data = json.loads(response)

print(f"""
IP: {data['query']}
Country: {data['country']}
City: {data['city']}
ISP: {data['isp']}
ZIP: {data['zip']}
Lon: {data['lon']}
LAT: {data['lat']}
""")
