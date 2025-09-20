import os
import time

def clear_console():
    """Limpia la consola"""
    os.system('cls' if os.name == 'nt' else 'clear')

# Animación simple de 3 frames
def animacion_simple():
    frames = [
        """
        🚀 INICIANDO
        [░░░░░░░░░░] 0%
        """,
        """
        🚀 CARGANDO
        [████░░░░░░] 50%
        """,
        """
        🚀 COMPLETADO!
        [██████████] 100%
        ✅
        """
    ]
    
    for frame in frames:
        clear_console()
        print("╔══════════════════════╗")
        print("║                      ║")
        print("║     ANIMACIÓN        ║")
        print("║                      ║")
        print(frame)
        print("╚══════════════════════╝")
        time.sleep(1)  # 1 segundo entre frames

# Ejecutar animación
animacion_simple()