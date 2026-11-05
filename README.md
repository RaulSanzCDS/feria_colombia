# Sistema de Telemetría Térmica - Gran Feria de Colombia (Versión Estable)

Módulo de calibración térmica y recuperación de señales del pabellón principal.

## Instrucciones de Despliegue con Docker

### 1. Construir la imagen localmente:
```bash
docker build -t feria_colombia:estable .
```

### 2. Ejecutar la calibración:
De forma interactiva:
```bash
docker run -it feria_colombia:estable
```
O pasando las coordenadas del epicentro térmico como variable de entorno:
```bash
docker run -it -e COORDS="1254,235" feria_colombia:estable
```

### 3. Registro en Docker Hub (Opcional):
Si se desea distribuir la imagen en Docker Hub:
```bash
docker tag feria_colombia:estable <tu_usuario_dockerhub>/feria_colombia:estable
docker push <tu_usuario_dockerhub>/feria_colombia:estable
```
