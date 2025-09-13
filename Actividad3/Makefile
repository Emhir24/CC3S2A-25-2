# --- Configuración base ---
APP_NAME=miapp
DOMAIN=miapp.local
PORT=8080

# Rutas (Linux)
CERT_DIR=certs
KEY_FILE=$(CERT_DIR)/$(DOMAIN).key
CRT_FILE=$(CERT_DIR)/$(DOMAIN).crt

NGINX_SITE_AVAIL=/etc/nginx/sites-available/$(APP_NAME).conf
NGINX_SITE_ENABLED=/etc/nginx/sites-enabled/$(APP_NAME).conf
NGINX_CERT_DIR=/etc/ssl/$(APP_NAME)

# Herramientas
OPENSSL=$(shell which openssl)
CURL=$(shell which curl)
NGINX=$(shell which nginx)

.PHONY: help
help:
	@echo "Targets útiles:"
	@echo "  make tls-cert     -> Genera certificado autofirmado en ./certs/"
	@echo "  make nginx        -> Copia vhost y certificados a Nginx y recarga"
	@echo "  make check-tls    -> Verifica handshake y cabeceras HTTPS"

# --- TLS: generar cert autofirmado ---
.PHONY: tls-cert
tls-cert:
	@[ -n "$(OPENSSL)" ] || { echo "openssl no disponible"; exit 1; }
	mkdir -p $(CERT_DIR)
	@if [ ! -f "$(KEY_FILE)" ] || [ ! -f "$(CRT_FILE)" ]; then \
	  echo "Generando certificado para $(DOMAIN)"; \
	  $(OPENSSL) req -x509 -nodes -newkey rsa:2048 \
	    -keyout $(KEY_FILE) -out $(CRT_FILE) -days 365 \
	    -subj "/CN=$(DOMAIN)"; \
	else echo "Certificado ya existe en $(CERT_DIR)/"; fi

# --- Nginx: instalar vhost y recargar ---
.PHONY: nginx
nginx: tls-cert
	@if [ -z "$(NGINX)" ]; then echo "nginx no encontrado"; exit 1; fi
	sudo mkdir -p $(NGINX_CERT_DIR)
	sudo cp $(CRT_FILE) $(NGINX_CERT_DIR)/$(DOMAIN).crt
	sudo cp $(KEY_FILE) $(NGINX_CERT_DIR)/$(DOMAIN).key
	@sudo cp nginx/miapp.conf $(NGINX_SITE_AVAIL)
	@sudo ln -sf $(NGINX_SITE_AVAIL) $(NGINX_SITE_ENABLED)
	sudo nginx -t
	sudo systemctl reload nginx
	@echo "Listo. Prueba: https://$(DOMAIN)"

# --- Chequeo TLS ---
.PHONY: check-tls
check-tls:
	@echo "openssl s_client (resumen)"
	@openssl s_client -connect $(DOMAIN):443 -servername $(DOMAIN) -brief </dev/null || true
	@echo "curl -kI (cabeceras)"
	@curl -skI https://$(DOMAIN) || true
