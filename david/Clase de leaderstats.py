import urllib.request
import json
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
class ControlDeDatos:
    """
    DOCS
    @User: David
    """
    def guardarDatos(self,nombre:str,puntuacion:int) -> str:
        webhook = "https://wh.unet.es/webhook-test/54d47dec-0f41-4f6d-bd53-24e9384494c7"
        """
            Guarda los datos de nombre y puntuación en una base de datos online
            pensada para ser usada al final de playthrough
        """
        payload = {
            "nombre": nombre,
            "puntuacion": puntuacion
        }
        json_data = json.dumps(payload).encode('utf-8')
        req = urllib.request.Request(webhook, data=json_data, method='POST')
        req.add_header('Content-Type', 'application/json')
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)')

        try:
            with urllib.request.urlopen(req) as response:
                status = response.getcode()
                return status
        except urllib.error.HTTPError as e:
            return e.read().decode('utf-8')
        except Exception as e:
            return e

    def preguntarDatos(self) -> list:
        """
            Devuelve una Lista de Diccionarios con los datos de nmbre y puntiación
            guardada en la base de datos.
        """
        url = "https://david.unet.es/spaceInvaders/leaderstats.json"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        }
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req) as response:
                data = response.read().decode('utf-8')
                datos_json = json.loads(data)
                return datos_json #Listas de Diccionarios
        except Exception as e:
            print(f"Error al obtener los datos: {e}")
print(ControlDeDatos.preguntarDatos()[3]["nombre"])

"""
USOS POR DEFECTO:
ControlDeDatos.guardarDatos("dani",255)
ControlDeDatos.preguntarDatos()
print(ControlDeDatos.preguntarDatos()[0]["nombre"])
"""