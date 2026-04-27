"""
Ejemplo Completo - Todas las características de STAR Subtitle Manager
"""

from subtitles import SubtitleManager


def main():
    print("=" * 70)
    print("EJEMPLO COMPLETO - STAR Subtitle Manager")
    print("=" * 70)
    
    # ========== CREAR Y AGREGAR ==========
    print("\n[1] CREAR Y AGREGAR SUBTÍTULOS")
    print("-" * 70)
    
    sm = SubtitleManager()
    
    subtitles_data = [
        (1, "00:00:01,000", "00:00:05,000", "Érase una vez en el reino mágico"),
        (2, "00:00:06,000", "00:00:10,000", "Vivía una hermosa princesa"),
        (3, "00:00:11,000", "00:00:15,000", "Ella era amada por todo el pueblo"),
        (4, "00:00:16,000", "00:00:20,000", "Un día llegó un misterioso caballero"),
        (5, "00:00:21,000", "00:00:25,000", "Traía noticias del reino vecino"),
    ]
    
    for num, start, end, text in subtitles_data:
        sm.add_subtitle(num, start, end, text)
        print(f"✓ Subtítulo {num} agregado")
    
    # ========== VER SUBTÍTULOS ==========
    print("\n[2] VER SUBTÍTULOS")
    print("-" * 70)
    
    for sub in sm.get_all_subtitles():
        print(f"[{sub.number}] {sub.start} --> {sub.end}")
        print(f"    {sub.text}\n")
    
    # ========== EDITAR SUBTÍTULOS ==========
    print("[3] EDITAR SUBTÍTULOS")
    print("-" * 70)
    
    sm.edit_subtitle(2, text="Vivía una hermosa princesa con cabello dorado")
    print("✓ Subtítulo 2 editado correctamente")
    print(f"  Nuevo texto: {sm.get_subtitle(2).text}\n")
    
    # ========== BUSCAR SUBTÍTULOS ==========
    print("[4] BUSCAR SUBTÍTULOS")
    print("-" * 70)
    
    query = "reino"
    results = sm.search(query)
    print(f"Búsqueda: '{query}' encontró {len(results)} resultado(s)\n")
    for sub in results:
        print(f"[{sub.number}] {sub.text}")
    
    # ========== REEMPLAZAR TEXTO ==========
    print("\n[5] REEMPLAZAR TEXTO")
    print("-" * 70)
    
    count = sm.replace("reino", "REINO")
    print(f"✓ Se reemplazaron {count} subtítulo(s)\n")
    
    # Ver cambios
    for sub in sm.search("REINO"):
        print(f"[{sub.number}] {sub.text}")
    
    # Revertir cambios
    sm.replace("REINO", "reino")
    
    # ========== VALIDAR SUBTÍTULOS ==========
    print("\n[6] VALIDAR SUBTÍTULOS")
    print("-" * 70)
    
    # Agregar un subtítulo inválido para demostrar
    sm.add_subtitle(6, "00:00:26,000", "00:00:20,000", "Tiempo inválido")
    sm.add_subtitle(7, "00:00:26,000", "00:00:30,000", "")  # Texto vacío
    
    valid, invalid = sm.validate_all()
    print(f"✓ Subtítulos válidos: {len(valid)}")
    print(f"✗ Subtítulos inválidos: {len(invalid)}\n")
    
    for sub in invalid:
        print(f"  Problema en subtítulo {sub.number}")
        if sub.text == "":
            print(f"    - Texto vacío")
        if sm.Subtitle.time_to_milliseconds(sub.start) >= \
           sm.Subtitle.time_to_milliseconds(sub.end):
            print(f"    - Tiempo de inicio >= tiempo de fin")
    
    # Eliminar subtítulos inválidos
    sm.delete_subtitle(6)
    sm.delete_subtitle(7)
    print(f"\n✓ Subtítulos inválidos eliminados")
    
    # ========== ESTADÍSTICAS ==========
    print("\n[7] ESTADÍSTICAS")
    print("-" * 70)
    
    stats = sm.get_statistics()
    print(f"Total de subtítulos: {stats['total']}")
    print(f"Total de palabras: {stats['words']}")
    print(f"Total de caracteres: {stats['characters']}")
    print(f"Promedio de palabras por subtítulo: {stats['avg_words']}")
    print(f"Promedio de caracteres por subtítulo: {stats['avg_characters']}")
    
    # ========== DESPLAZAR TIEMPOS ==========
    print("\n[8] DESPLAZAR TIEMPOS (SINCRONIZACIÓN)")
    print("-" * 70)
    
    print("Tiempos ANTES del desplazamiento:")
    for sub in sm.get_all_subtitles()[:3]:
        print(f"  [{sub.number}] {sub.start} --> {sub.end}")
    
    # Desplazar 2 segundos hacia adelante
    sm.shift_time(2000)
    print("\nTiempos DESPUÉS del desplazamiento (+2 segundos):")
    for sub in sm.get_all_subtitles()[:3]:
        print(f"  [{sub.number}] {sub.start} --> {sub.end}")
    
    # Desplazar 2 segundos hacia atrás (revertir)
    sm.shift_time(-2000)
    
    # ========== GUARDAR ARCHIVO ==========
    print("\n[9] GUARDAR ARCHIVO SRT")
    print("-" * 70)
    
    sm.save("ejemplo_completo.srt")
    print("✓ Archivo guardado como 'ejemplo_completo.srt'")
    
    # ========== CARGAR ARCHIVO ==========
    print("\n[10] CARGAR ARCHIVO SRT")
    print("-" * 70)
    
    sm_nuevo = SubtitleManager()
    sm_nuevo.load("ejemplo_completo.srt")
    print(f"✓ Se cargaron {len(sm_nuevo.get_all_subtitles())} subtítulos")
    
    # ========== ELIMINAR SUBTÍTULO ==========
    print("\n[11] ELIMINAR SUBTÍTULO")
    print("-" * 70)
    
    print(f"Total antes: {len(sm.get_all_subtitles())}")
    sm.delete_subtitle(5)
    print("✓ Subtítulo 5 eliminado")
    print(f"Total después: {len(sm.get_all_subtitles())}")
    
    # ========== CONCLUSIÓN ==========
    print("\n" + "=" * 70)
    print("¡EJEMPLO COMPLETADO EXITOSAMENTE!")
    print("=" * 70)
    print("\nFuncionalidades demostradas:")
    print("  ✓ Crear y agregar subtítulos")
    print("  ✓ Ver subtítulos")
    print("  ✓ Editar subtítulos")
    print("  ✓ Buscar subtítulos")
    print("  ✓ Reemplazar texto")
    print("  ✓ Validar subtítulos")
    print("  ✓ Obtener estadísticas")
    print("  ✓ Desplazar/sincronizar tiempos")
    print("  ✓ Guardar archivos SRT")
    print("  ✓ Cargar archivos SRT")
    print("  ✓ Eliminar subtítulos")
    print("=" * 70)


if __name__ == "__main__":
    main()
