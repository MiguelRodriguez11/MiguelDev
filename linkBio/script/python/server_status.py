import requests

# URL del servidor web que quieres verificar
URL = "https://migueldev-web.vercel.app"

try:
    # Realizar una solicitud HTTP y obtener el código de estado
    response = requests.get(URL)
    http_response = response.status_code

    # Comprobar el código de respuesta
    if http_response == 200:
        print(f"El servidor web está funcionando correctamente. Código de respuesta: {http_response}")
    else:
        print(f"El servidor web no está disponible. Código de respuesta: {http_response}")
        exit(1)
except requests.exceptions.RequestException as e:
    # Manejar errores en la solicitud HTTP
    print(f"Error: No se pudo conectar al servidor web. Detalles: {e}")
    exit(1)
