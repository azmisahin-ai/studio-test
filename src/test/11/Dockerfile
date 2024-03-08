# Dockerfile
# Temel aşaması
FROM alpine:latest AS base

# Bash'ı yükle
RUN apk add --no-cache bash

# Python'u yükle
RUN apk add --no-cache python3 py3-pip

# Geliştirme aşaması
FROM base AS development

# Geliştirme için sanal ortamı oluştur
RUN python3 -m venv /venv

# Geliştirme için sanal ortamı aktive et ve ek paketleri yükle
RUN source /venv/bin/activate && pip install Flask gunicorn pytest Flask-GraphQL Flask-SocketIO Flask-JSONRPC graphene python-socketio eventlet flask_cors 

# Geliştirme için uygulama kodunu yükle
COPY . .

# Start
# CMD ["/venv/bin/gunicorn", "--bind", "0.0.0.0:5000", "app:app"]

# Üretim aşaması
FROM base AS production

# Üretim için sanal ortamı oluştur
RUN python3 -m venv /venv

# Üretim için sanal ortamı aktive et ve gerekli paketleri yükle
RUN source /venv/bin/activate && pip install Flask gunicorn Flask-GraphQL Flask-SocketIO Flask-JSONRPC graphene python-socketio eventlet flask_cors

# Üretim için uygulama kodunu yükle
COPY . .

# Uygulama çalıştırma komutu
CMD ["/venv/bin/gunicorn", "--bind", "0.0.0.0:80", "app:app"]