# Telemetry experimental module
import os, sys

coords = os.environ.get("COORDS", "")
print("[DEV] Sensor experimental activo.")
if coords:
    print(f"[DEV] Coordenadas recibidas: {coords}")
    print("[DEV] [AVISO] Entorno experimental no calibrado. Salida simulada.")
    print("[SALIDA_MOCK] CLAVE_AUDIO: TEST_DEV_FLAG_INCORRECTA")
