#!/bin/bash
echo "== Verificando HTTP =="
curl -sI http://127.0.0.1:8080 || exit 1

echo "== Verificando DNS =="
ping -c 1 miapp.local || exit 1

echo "== Verificando TLS =="
curl -skI https://miapp.local || exit 1

echo "== Todas las pruebas pasaron =="
