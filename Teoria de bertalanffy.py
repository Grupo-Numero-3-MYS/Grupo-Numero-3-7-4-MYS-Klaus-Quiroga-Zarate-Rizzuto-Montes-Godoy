import time, os

def cls(): os.system("cls" if os.name == "nt" else "clear")
def enter(): input("\n  [ENTER para continuar]")

TEORIAS = [
    {
        "nombre": "1. Sistema Abierto",
        "resumen": "Los sistemas intercambian materia, energía e información con su entorno.\nPueden alcanzar un estado estacionario dinámico (no el reposo).",
        "conceptos": [
            "Equifinalidad   → distintos caminos pueden llevar al mismo estado final.",
            "Negentropía     → el sistema importa energía para evitar su degradación.",
            "Retroalimentación → el sistema ajusta su conducta según sus propios resultados.",
        ],
        "diagrama": """
    ENTORNO ──► [Entradas: comida, aire, info]
                          │
                          ▼
              ┌─────────────────────┐
              │   SISTEMA ABIERTO   │ ◄─ feedback
              │  (procesa y regula) │
              └─────────────────────┘
                          │
                          ▼
    ENTORNO ◄── [Salidas: calor, residuos, acción]
""",
    },
    {
        "nombre": "2. Sistema Cerrado",
        "resumen": "No hay intercambio de materia con el ambiente, solo de energía.\nTienden al equilibrio estático y al desorden interno.",
        "conceptos": [
            "Entropía        → Medida del desorden; tiende a aumentar hasta el máximo.",
            "Equilibrio      → El sistema llega a un punto de reposo (muerte del sistema).",
            "Aislamiento     → No recibe recursos externos para autosustentarse.",
        ],
        "diagrama": """
              ┌─────────────────────┐
     ENERGÍA  │   SISTEMA CERRADO   │  ENERGÍA
      ─────►  │ (Materia sellada)   │  ─────►
              │  Entropía en aumento│
              └─────────────────────┘
              (No hay entrada de materia nueva)
""",
    },
    {
        "nombre": "3. Crecimiento",
        "resumen": "Bertalanffy modeló matemáticamente el crecimiento de organismos vivos,\nbalanceando construcción (anabolismo) y degradación (catabolismo).",
        "conceptos": [
            "Ecuación:   dW/dt = η·W^(2/3) − κ·W",
            "W∞ (talla asintótica) = (η/κ)³  → límite teórico de tamaño.",
            "El metabolismo escala con la superficie (W^2/3), no con el volumen.",
        ],
        "diagrama": """
  Peso
   ∞  ┤· · · · · · · · · · · · · · (W∞ asintótico)
      │             ▄▄▄▀▀▀▀▀▀▀▀▀▀▀
      │         ▄▄▀▀
      │     ▄▄▀▀
      │  ▄▀▀
      │▄▀
   0  └─────────────────────────── tiempo
""",
    },
    {
        "nombre": "4. Mantenimiento / Homeostasis",
        "resumen": "Los sistemas vivos mantienen condiciones internas estables\nfrente a perturbaciones externas mediante feedback negativo.",
        "conceptos": [
            "Homeostasis     → variables internas dentro de rangos tolerables.",
            "Feedback −      → respuesta correctiva ante cualquier desviación.",
            "Estado estac.   → entradas = salidas, pero el sistema sigue activo.",
        ],
        "diagrama": """
  Temp baja → tirita  |  Temp sube → sudor
        ↓             |         ↓
  vuelve a 37 °C      |  vuelve a 37 °C
""",
    },
    {
        "nombre": "5. Teoría General de Sistemas (TGS)",
        "resumen": "Busca principios UNIVERSALES válidos para todo tipo de sistema:\nbiológico, social, físico o tecnológico.",
        "conceptos": [
            "Isomorfismo → leyes idénticas en disciplinas distintas.",
            "Emergencia  → el TODO tiene propiedades que sus partes NO poseen.",
            "Jerarquía   → subsistema → sistema → suprasistema.",
        ],
        "diagrama": """
  Biología: célula   ↔  órgano   ↔  organismo
  Empresa:  empleado  ↔  depto.   ↔  corporación
  Computación: módulo ↔  subsistema ↔ sistema
""",
    },
]

def mostrar(t):
    cls()
    print(f"\n  ══ {t['nombre']} ══\n")
    print(f"  {t['resumen']}\n")
    print("  Conceptos clave:")
    for c in t["conceptos"]:
        print(f"    • {c}")
        time.sleep(0.1)
    enter()
    cls()
    print(f"\n  Diagrama — {t['nombre']}\n")
    print(t["diagrama"])
    enter()

def menu():
    while True:
        cls()
        print("\n╔══════════════════════════════════════════╗")
        print("║  Teorías de Bertalanffy  — Explorador    ║")
        print("╚══════════════════════════════════════════╝")
        
        for i, t in enumerate(TEORIAS, 1):
            print(f"  [{i}] {t['nombre']}")
        print("  [0] Salir\n")
        
        op = input("  Elegí una teoría: ").strip()
        
        if op == "0":
            print("\n  'El todo es más que la suma de sus partes.' — Bertalanffy\n")
            break
        elif op.isdigit() and 1 <= int(op) <= len(TEORIAS):
            mostrar(TEORIAS[int(op)-1])
        else:
            print("\n  Opción no válida.")
            time.sleep(1)

menu()