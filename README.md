# GeoIpTelegram

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
    git clone https://github.com/tuusuario/monitor-conexiones-puertos.git
    cd monitor-conexiones-puertos
    ```

2. Instala las dependencias necesarias:
    ```bash
    pip install -r requirements.txt
    ```

3. Configura las variables de entorno `TELEGRAM_TOKEN` y `TELEGRAM_CHAT_ID`:
    ```bash
    export TELEGRAM_TOKEN="tu_token_aqui"
    export TELEGRAM_CHAT_ID="tu_chat_id_aqui"
    ```

## Uso

Ejecuta el script para iniciar el monitoreo y envío de reportes a Telegram:

```bash
python monitor_conexiones.py
