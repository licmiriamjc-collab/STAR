"""
Ejemplo Básico - Introducción rápida a STAR Subtitle Manager
"""

from subtitles import SubtitleManager


def main():
    print("=" * 70)
    print("EJEMPLO BÁSICO - STAR Subtitle Manager")
    print("=" * 70)
    
    # Crear gestor
    sm = SubtitleManager()
    print("\n✓ Gestor de subtítulos creado\n")
    
    # Agregar subtítulos
    print("[1] Agregando subtítulos...")
    sm.add_subtitle(1, "00:00:01,000", "00:00:05,000", "¡Hola! Bienvenido")
    sm.add_subtitle(2, "00:00:06,000", "00:00:10,000", "Este es un ejemplo")
    sm.add_subtitle(3, "00:00:11,000", "00:00:15,000", "De cómo usar STAR")
    print("✓ Tres subtítulos agregados\n")
    
    # Ver subtítulos
    print("[2] Viendo subtítulos...")
    for sub in sm.get_all_subtitles():
        print(f"[{sub.number}] {sub.start} --> {sub.end}")
        print(f"    {sub.text}\n")
    
    # Guardar
    print("[3] Guardando archivo...")
    sm.save("ejemplo.srt")
    print("✓ Archivo guardado como 'ejemplo.srt'\n")
    
    # Cargar
    print("[4] Cargando archivo...")
    sm_nuevo = SubtitleManager()
    sm_nuevo.load("ejemplo.srt")
    print(f"✓ Se cargaron {len(sm_nuevo.get_all_subtitles())} subtítulos\n")
    
    # Estadísticas
    print("[5] Estadísticas...")
    stats = sm.get_statistics()
    print(f"Total: {stats['total']} subtítulos")
    print(f"Palabras: {stats['words']}")
    print(f"Caracteres: {stats['characters']}\n")
    
    print("=" * 70)
    print("¡EJEMPLO COMPLETADO!")
    print("=" * 70)


if __name__ == "__main__":
    main()
