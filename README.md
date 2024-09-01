# GeoIpTelegram

## Ejemplo de notificación

Las notificaciones se envian organizando las Ips automaticamente por paises, pudiendo filtrar los puertos que quieres.

![Ejemplo de Notificación en Telegram](/imagenes/Ip.PNG)

# Monitor de Conexiones Activas en Puertos de Interés

Este script monitorea las conexiones activas en puertos específicos de un servidor y envía un reporte detallado a un chat de Telegram. El reporte incluye información de las IPs conectadas, clasificadas por país, región, ciudad y proveedor de servicios de internet (ISP).

## Características

- Monitorea conexiones en puertos comunes como `22`, `445`, `80`, `443`, entre otros.
- Clasifica las conexiones activas por país utilizando la API de IP-API.
- Envía un reporte detallado a un chat de Telegram cada 5 minutos.

## Requisitos

- Python 3.x
- La librería `requests` (puede instalarse con `pip install -r requirements.txt`).
- Tener configurado un bot de Telegram y obtener un `TOKEN` y `CHAT_ID`.

## Instalación

1. Clona este repositorio:
    ```bash
    git clone https://github.com/FalconAkantor/GeoIpTelegram
    cd GeoIpTelegram
    ```

2. Instala las dependencias necesarias:
    ```bash
    pip install -r requirements.txt
    ```

3. Configura las variables de entorno `TELEGRAM_TOKEN` y `TELEGRAM_CHAT_ID` tienes que editar el archivo `Geo.py`:
  ```bash
    TOKEN = os.getenv("TELEGRAM_TOKEN")
    CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
  ```
Al final del archivo podemos editar los puertos que queremos que se filtren:

```bash
    ports = [22, 445, 80, 443, 1194]
 ```
  
## Uso

Ejecuta el script para iniciar el monitoreo y envío de reportes a Telegram:

```bash
python3 geo.py
