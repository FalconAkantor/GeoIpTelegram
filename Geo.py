import os
import requests
import subprocess
import time

# Configuración de Telegram a través de variables de entorno
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
API_URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

# Función para enviar mensaje de texto a Telegram
def send_message(message):
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    requests.post(API_URL, data=payload)

# Función para obtener la bandera del país basado en el código del país
def country_flag(country_code):
    return ''.join(chr(127397 + ord(c)) for c in country_code.upper())

# Función para obtener información de IP
def get_ip_info(ip):
    response = requests.get(f"http://www.ip-api.com/json/{ip}")
    data = response.json()

    if data.get('status') != 'success':
        return {
            "country": "N/A",
            "countryCode": "N/A",
            "region": "N/A",
            "city": "N/A",
            "isp": "N/A"
        }

    return {
        "country": data.get('country', 'N/A'),
        "countryCode": data.get('countryCode', 'N/A'),
        "region": data.get('regionName', 'N/A'),
        "city": data.get('city', 'N/A'),
        "isp": data.get('isp', 'N/A')
    }

# Función para obtener IPs conectadas a un puerto específico y su uso de red
def get_ips_by_port(port):
    netstat_output = subprocess.check_output(f"netstat -tn | grep ':{port} ' | awk '{{print $5}}' | cut -d: -f1 | sort | uniq", shell=True)
    ips = netstat_output.decode().splitlines()
    return ips

# Función para clasificar y construir el mensaje
def build_message():
    message = "🔍 *Conexiones activas en puertos de interés, clasificadas por país:*\n"
    country_connections = {}

    # Puertos de interés
    ports = [22, 445, 80, 443, 32400, 5001, 8181, 8443, 1194]

    for port in ports:
        ips = get_ips_by_port(port)
        for ip in ips:
            ip_info = get_ip_info(ip)
            country = ip_info['country']
            country_code = ip_info['countryCode']
            flag = country_flag(country_code) if country_code != "N/A" else "N/A"
            region = ip_info['region']
            city = ip_info['city']
            isp = ip_info['isp']

            connection_info = f"IP: {ip} (Puerto {port})\nRegión: {region}\nCiudad: {city}\nISP: {isp}\n────────────────────────────"

            if flag not in country_connections:
                country_connections[flag] = {"name": country, "connections": []}
            country_connections[flag]["connections"].append(connection_info)

    # Construcción del mensaje
    for flag, info in country_connections.items():
        country_name = info["name"]
        message += f"\n{flag} {country_name}:\n"
        for connection in info["connections"]:
            message += f"{connection}\n"

    return message

# Envío en bucle cada 5 minutos
while True:
    service_info = build_message()
    send_message(service_info)
    time.sleep(300)  # Esperar 5 minutos (300 segundos)
