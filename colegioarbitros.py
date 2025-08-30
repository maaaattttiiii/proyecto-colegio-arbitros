from supabase import create_client
from datetime import date

url = "https://ucsvtpfjocxozojiphot.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVjc3Z0cGZqb2N4b3pvamlwaG90Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTY1OTEzODIsImV4cCI6MjA3MjE2NzM4Mn0.6R4924uh-7cqS6SU1bUX-Fcl1Dzoiayr2s8f38hHemo"
supabase = create_client(url, key)



def registrar_partido():
    print("\n=== Registrar nuevo partido ===")
    fecha = input("Fecha (YYYY-MM-DD, vacío para hoy): ") or str(date.today())
    lugar = input("Lugar: ")
    equipos = input("Equipos (Ej: River vs Boca): ")
    monto = float(input("Monto cobrado: "))
    gastos = float(input("Gastos (si no hay, poné 0): "))
    pagado = input("¿Pagado? (s/n): ").lower() == "s"
    observaciones = input("Observaciones: ")

    data = {
        "fecha": fecha,
        "lugar": lugar,
        "equipos": equipos,
        "monto": monto,
        "gastos": gastos,
        "pagado": pagado,
        "observaciones": observaciones
    }

    supabase.table("partidos").insert(data).execute()
    print("✅ Partido registrado con éxito.\n")

def listar_partidos():
    print("\n=== Lista de partidos ===")
    res = supabase.table("partidos").select("*").order("fecha").execute()
    for p in res.data:
        print(f"[{p['id']}] {p['fecha']} - {p['equipos']} en {p['lugar']} | ${p['monto']} | Pagado: {p['pagado']}")

def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Registrar partido")
        print("2. Ver partidos")
        print("3. Salir")
        opcion = input("Elegí una opción: ")

        if opcion == "1":
            registrar_partido()
        elif opcion == "2":
            listar_partidos()
        elif opcion == "3":
            print("👋 Saliendo...")
            break
        else:
            print("❌ Opción no válida.")

if __name__ == "__main__":
    menu()
