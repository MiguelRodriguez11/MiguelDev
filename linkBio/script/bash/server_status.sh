#!/bin/bash

URL="https://migueldev-web.vercel.app"

HTTP_RESPONSE=$(curl --write-out "%{http_code}" --silent --output /dev/null "$URL")

if [ "$HTTP_RESPONSE" -eq 200 ]; then
    echo "El servidor web esta funcionando correctamente. Codigo de respuesta: $HTTP_RESPONSE"
else
    echo "El servidor web no esta disponible. Codigo de respuesta: $HTTP_RESPONSE"
    exit 1
fi
