import hashlib
import os
import sys
import time

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# Hash SHA-256 de verificacion termica del epicentro
HASH_VERIFICACION = "d3782e62cffd3f3efd96e7c026d1cbd0f277d75629dd23f7441eb29341347187"

# Payload protegido con la clave de calibracion
PAYLOAD_BYTES = [122, 125, 120, 122, 118, 21, 115, 124, 17, 120, 121, 119, 124, 120, 25, 99, 124, 111, 102, 101, 114, 107, 112, 125, 109, 9, 63, 213, 172, 165, 219, 185, 163, 215, 162, 169, 211, 172, 138, 209, 160, 167, 219, 164, 159, 206, 166, 165, 213, 172, 151, 219, 185, 163, 215, 162, 169, 211, 172, 187, 57, 215, 162, 168, 211, 172, 184, 209, 160, 160, 219, 164, 168, 206, 166, 164, 213, 172, 160, 219, 185, 162, 215, 162, 153, 211, 172, 187, 209, 160, 160, 219, 164, 168, 38, 209, 160, 166, 219, 164, 153, 206, 166, 150, 213, 172, 160, 219, 185, 162, 215, 162, 168, 211, 172, 189, 209, 160, 151, 219, 164, 144, 206, 166, 168, 213, 172, 160, 51, 206, 166, 175, 213, 172, 172, 219, 185, 169, 215, 162, 144, 211, 172, 133, 209, 160, 167, 219, 164, 144, 206, 166, 156, 213, 172, 161, 219, 185, 163, 215, 162, 164, 59, 105, 101, 96, 97, 118, 3, 17, 124, 64, 19, 71, 66, 80, 85, 86, 12, 71, 84, 90, 91, 88, 250, 133, 93, 21, 84, 86, 95, 77, 69, 86, 91, 82, 25, 88, 87, 74, 92, 71, 90, 88, 82, 80, 239, 128, 91, 25, 51, 12, 4, 17, 14, 8, 10, 4, 12, 4, 17, 14, 8, 10, 4, 12, 4, 17, 14, 8, 10, 4, 12, 4, 17, 14, 8, 10, 4, 12, 4, 17, 14, 8, 10, 4, 12, 4, 17, 14, 8, 10, 4, 12, 4, 17, 14, 8, 10, 4, 12, 4, 17, 14, 8, 10, 4, 12, 4, 17, 14, 63, 108, 112, 127, 127, 99, 110, 21, 123, 88, 17, 90, 64, 82, 67, 82, 25, 65, 88, 94, 82, 21, 83, 92, 66, 90, 69, 85, 71, 86, 75, 17, 92, 64, 19, 84, 66, 93, 88, 86, 12, 86, 70, 13, 25, 112, 116, 104, 57, 8, 10, 4, 12, 4, 17, 14, 8, 10, 4, 12, 4, 17, 14, 8, 10, 4, 12, 4, 17, 14, 8, 10, 4, 12, 4, 17, 14, 8, 10, 4, 12, 4, 17, 14, 8, 10, 4, 12, 4, 17, 14, 8, 10, 4, 12, 4, 17, 14, 8, 10, 4, 12, 4, 17, 14, 8, 10, 4, 12]

def main():
    print("=" * 60)
    print(" SISTEMA DE TELEMETRIA TERMICA - GRAN FERIA INTERNACIONAL")
    print(" CENTRO DE OPERACIONES - PABELLON PRINCIPAL")
    print("=" * 60)
    print("[+] Modulo de calibracion de frecuencias activo.")
    print("[+] Sincronizando con el sensor de telemetria...")
    time.sleep(0.5)

    coords = os.environ.get("COORDS") or os.environ.get("EPICENTRO")
    if not coords and len(sys.argv) > 1:
        coords = sys.argv[1]

    if not coords:
        try:
            coords = input("\nIngrese las coordenadas del epicentro termico (formato X,Y): ").strip()
        except EOFError:
            coords = ""

    coords_clean = coords.replace(" ", "").strip()
    hsh = hashlib.sha256(coords_clean.encode("utf-8")).hexdigest()

    if hsh == HASH_VERIFICACION:
        print(f"\n[VERIFICACION] Coordenadas validas. Epicentro termico confirmado.")
        print("[VERIFICACION] Desfasaje espectral corregido: 0.000 Hz.")
        print("[+] Descifrando senal portadora de audio...")
        time.sleep(0.8)

        # Descifrar payload con las coordenadas introducidas como clave XOR
        clave = coords_clean.encode("utf-8")
        banner = bytes(b ^ clave[i % len(clave)] for i, b in enumerate(PAYLOAD_BYTES)).decode("utf-8")

        print("\n" + "=" * 60)
        print(banner)
        print("=" * 60)
    else:
        print(f"\n[-] ERROR: Coordenadas invalidas. Desfase de frecuencia irreversible.")
        print("[-] Telemetria no calibrada.")
        print("[-] Telemetria abortada.")
        sys.exit(1)

if __name__ == "__main__":
    main()
