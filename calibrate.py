import os
import sys
import time

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
    if coords_clean == "1254,235":
        print(f"\n[VERIFICACION] Coordenadas [{coords_clean}] confirmadas en el epicentro.")
        print("[VERIFICACION] Desfasaje espectral corregido: 0.000 Hz.")
        print("[+] Descifrando senal portadora de audio...")
        time.sleep(0.8)
        print("\n" + "=" * 60)
        print("CLAVE DE AUDIO RECUPERADA:")
        print("╔══╦═╦═╦══╗")
        print("║╔╗║║║║╠╗╗║")
        print("║╠╣║║║║╠╩╝║")
        print("╚╝╚╩╩═╩╩══╝")
        print("PISTA: El ruido también contiene información.")
        print("============================================================")
        print("[INFO] La clave para descifrar el audio es: AMD")
        print("=" * 60)
    else:
        print(f"\n[-] ERROR: Coordenadas [{coords}] no corresponden con la anomalia termica.")
        print("[-] Desfase de frecuencia: Senal no recuperable.")
        print("[-] Telemetria abortada.")
        sys.exit(1)

if __name__ == "__main__":
    main()
