from supabase import create_client
from datetime import date

url = "https://ucsvtpfjocxozojiphot.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVjc3Z0cGZqb2N4b3pvamlwaG90Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTY1OTEzODIsImV4cCI6MjA3MjE2NzM4Mn0.6R4924uh-7cqS6SU1bUX-Fcl1Dzoiayr2s8f38hHemo"
supabase = create_client(url, key)



def login():
    print("=== LOGIN ===")
    email = input("Email: ")
    password = input("Contraseña: ")

    try:
        res = supabase.auth.sign_in_with_password({
            "email": email,
            "password": password
        })
        if res.user:
            print(f"✅ Bienvenido {res.user.email}")
            return res.user
    except Exception as e:
        print("Error en login", e)

    return None


def registrar_partido(user_id):
    print("\n=== REGISTRAR PARTIDO ===")
    fecha = input("Fecha (YYYY-MM-DD): ")
    lugar = input("Lugar: ")
    equipos = input("Equipos: ")
    monto = float(input("Monto: "))
    gastos = float(input("Gastos: "))
    pagado = input("¿Pagado? (s/n): ").lower() == "s"
    observaciones = input("Observaciones: ")

    data = {
        "fecha": fecha,
        "lugar": lugar,
        "equipos": equipos,
        "monto": monto,
        "gastos": gastos,
        "pagado": pagado,
        "observaciones": observaciones,
        "user_id": user_id
    }

    supabase.table("partidos").insert(data).execute()
    print("✅ Partido registrado correctamente.")


def ver_partidos(user_id):
    print("\n=== MIS PARTIDOS ===")
    res = supabase.table("partidos").select("*").eq("user_id", user_id).execute()

    if not res.data:
        print("No tienes partidos cargados.")
        return

    for p in res.data:
        print(f"- {p['fecha']} | {p['equipos']} | ${p['monto']} | Pagado: {p['pagado']}")


def main():
    user = login()
    if not user:
        print("No se pudo iniciar sesión. Saliendo...")
        return

    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Registrar partido")
        print("2. Ver mis partidos")
        print("3. Salir")

        opcion = input("Opción: ")

        if opcion == "1":
            registrar_partido(user.id)
        elif opcion == "2":
            ver_partidos(user.id)
        elif opcion == "3":
            print("Saliendo...")
            break
        else:
            print("❌ Opción no válida")


if __name__ == "__main__":
    main()


