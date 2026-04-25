"se plantea la gestion  de pacientes de un consultorio odontologico,"
" especificamente aquellos que requieren  extracciones dentales urgentes."
"para esto se implementan estructuras de datos tipo pila y cola "
"Diseñar un programa que:"
"Filtre pacientes con extracción dental y prioridad urgente."
"Organice estos pacientes en una pila según la fecha."
"Genere un informe para atención prioritaria."
"Gestione la atención diaria mediante una cola."
"✔️ Condiciones"
"Tipo de procedimiento: extracción"
"Prioridad: urgente"

pacientes = [
    {"nombre": "Ana", "tipo": "extraccion", "prioridad": "urgente", "fecha": "2026-04-25"},
    {"nombre": "Luis", "tipo": "limpieza", "prioridad": "normal", "fecha": "2026-04-24"},
    {"nombre": "Carlos", "tipo": "extraccion", "prioridad": "urgente", "fecha": "2026-04-23"},
    {"nombre": "Sofia", "tipo": "extraccion", "prioridad": "normal", "fecha": "2026-04-26"},
    {"nombre": "Marta", "tipo": "extraccion", "prioridad": "urgente", "fecha": "2026-04-22"}
]

pila = []

for p in pacientes:
    if p["tipo"] == "extraccion" and p["prioridad"] == "urgente":
        pila.append(p)

pila.sort(key=lambda x: x["fecha"], reverse=True)
print("=== INFORME DE PACIENTES URGENTES ===")

while pila:
    paciente = pila.pop()
    print(f"Nombre: {paciente['nombre']} - Fecha: {paciente['fecha']}")
    from collections import deque

cola = deque()

cola.append("Ana")
cola.append("Carlos")
cola.append("Marta")
print("\n=== ATENCIÓN DIARIA ===")

while cola:
    paciente = cola.popleft()
    print(f"Atendiendo a: {paciente}")

    print("=== VERIFICACIÓN DEL SISTEMA ===\n")

print("1. Pacientes originales:")
for p in pacientes:
    print(p)

print("\n2. Pacientes filtrados (solo extracciones urgentes):")
for p in pila:
    print(p)

print("\n3. Informe (uso de PILA):")
temp_pila = pila.copy()

while temp_pila:
    paciente = temp_pila.pop()
    print(f"Atendiendo (pila): {paciente['nombre']} - {paciente['fecha']}")

print("\n4. Atención diaria (COLA):")

from collections import deque
cola = deque(["Ana", "Carlos", "Marta"])

while cola:
    paciente = cola.popleft()
    print(f"Atendiendo (cola): {paciente}")