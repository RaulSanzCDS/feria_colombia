# Telemetry experimental module v2
import os, sys
coords = os.environ.get("COORDS", "")
print("[DEV v2] Nodo de pruebas en depuración.")
if coords:
    print(f"[DEV v2] Error: Canal desfasado en rama experimental.")
