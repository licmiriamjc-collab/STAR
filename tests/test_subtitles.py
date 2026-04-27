"""
Pruebas Unitarias para STAR Subtitle Manager
"""

import pytest
import os
from subtitles import Subtitle, SubtitleManager


class TestSubtitle:
    """Pruebas para la clase Subtitle"""
    
    def test_subtitle_creation(self):
        """Prueba creación de subtítulo"""
        sub = Subtitle(1, "00:00:01,000", "00:00:05,000", "Hola")
        assert sub.number == 1
        assert sub.start == "00:00:01,000"
        assert sub.end == "00:00:05,000"
        assert sub.text == "Hola"
    
    def test_time_to_milliseconds(self):
        """Prueba conversión de tiempo a milisegundos"""
        sub = Subtitle(1, "00:00:01,000", "00:00:05,000", "Test")
        
        assert sub.time_to_milliseconds("00:00:00,000") == 0
        assert sub.time_to_milliseconds("00:00:01,000") == 1000
        assert sub.time_to_milliseconds("00:01:00,000") == 60000
        assert sub.time_to_milliseconds("01:00:00,000") == 3600000
    
    def test_milliseconds_to_time(self):
        """Prueba conversión de milisegundos a tiempo"""
        sub = Subtitle(1, "00:00:01,000", "00:00:05,000", "Test")
        
        assert sub.milliseconds_to_time(0) == "00:00:00,000"
        assert sub.milliseconds_to_time(1000) == "00:00:01,000"
        assert sub.milliseconds_to_time(60000) == "00:01:00,000"
    
    def test_shift_time(self):
        """Prueba desplazamiento de tiempos"""
        sub = Subtitle(1, "00:00:01,000", "00:00:05,000", "Test")
        sub.shift_time(1000)  # Sumar 1 segundo
        
        assert sub.start == "00:00:02,000"
        assert sub.end == "00:00:06,000"
    
    def test_is_valid(self):
        """Prueba validación de subtítulos"""
        # Válido
        sub1 = Subtitle(1, "00:00:01,000", "00:00:05,000", "Hola")
        assert sub1.is_valid() is True
        
        # Tiempo de inicio >= tiempo de fin
        sub2 = Subtitle(1, "00:00:05,000", "00:00:01,000", "Hola")
        assert sub2.is_valid() is False
        
        # Texto vacío
        sub3 = Subtitle(1, "00:00:01,000", "00:00:05,000", "")
        assert sub3.is_valid() is False


class TestSubtitleManager:
    """Pruebas para la clase SubtitleManager"""
    
    @pytest.fixture
    def manager(self):
        """Fixture que proporciona un gestor limpio"""
        return SubtitleManager()
    
    def test_add_subtitle(self, manager):
        """Prueba agregar subtítulo"""
        manager.add_subtitle(1, "00:00:01,000", "00:00:05,000", "Hola")
        assert len(manager.get_all_subtitles()) == 1
    
    def test_edit_subtitle(self, manager):
        """Prueba editar subtítulo"""
        manager.add_subtitle(1, "00:00:01,000", "00:00:05,000", "Hola")
        manager.edit_subtitle(1, text="Adiós")
        
        sub = manager.get_subtitle(1)
        assert sub.text == "Adiós"
    
    def test_delete_subtitle(self, manager):
        """Prueba eliminar subtítulo"""
        manager.add_subtitle(1, "00:00:01,000", "00:00:05,000", "Hola")
        manager.delete_subtitle(1)
        
        assert len(manager.get_all_subtitles()) == 0
    
    def test_search(self, manager):
        """Prueba buscar subtítulos"""
        manager.add_subtitle(1, "00:00:01,000", "00:00:05,000", "Hola mundo")
        manager.add_subtitle(2, "00:00:06,000", "00:00:10,000", "Adiós")
        
        results = manager.search("mundo")
        assert len(results) == 1
        assert results[0].number == 1
    
    def test_replace(self, manager):
        """Prueba reemplazar texto"""
        manager.add_subtitle(1, "00:00:01,000", "00:00:05,000", "Hola mundo")
        manager.add_subtitle(2, "00:00:06,000", "00:00:10,000", "Adiós mundo")
        
        count = manager.replace("mundo", "tierra")
        assert count == 2
    
    def test_shift_time(self, manager):
        """Prueba desplazamiento de tiempos"""
        manager.add_subtitle(1, "00:00:01,000", "00:00:05,000", "Hola")
        manager.shift_time(1000)
        
        sub = manager.get_subtitle(1)
        assert sub.start == "00:00:02,000"
        assert sub.end == "00:00:06,000"
    
    def test_get_statistics(self, manager):
        """Prueba obtener estadísticas"""
        manager.add_subtitle(1, "00:00:01,000", "00:00:05,000", "Hola")
        manager.add_subtitle(2, "00:00:06,000", "00:00:10,000", "Mundo")
        
        stats = manager.get_statistics()
        assert stats['total'] == 2
        assert stats['characters'] == 10  # "Hola" + "Mundo"
    
    def test_save_and_load(self, manager):
        """Prueba guardar y cargar archivo"""
        manager.add_subtitle(1, "00:00:01,000", "00:00:05,000", "Hola")
        manager.add_subtitle(2, "00:00:06,000", "00:00:10,000", "Mundo")
        
        # Guardar
        manager.save("test_subtitle.srt")
        
        # Cargar en nuevo gestor
        manager2 = SubtitleManager()
        manager2.load("test_subtitle.srt")
        
        assert len(manager2.get_all_subtitles()) == 2
        assert manager2.get_subtitle(1).text == "Hola"
        
        # Limpiar
        if os.path.exists("test_subtitle.srt"):
            os.remove("test_subtitle.srt")
    
    def test_validate_all(self, manager):
        """Prueba validación de todos los subtítulos"""
        manager.add_subtitle(1, "00:00:01,000", "00:00:05,000", "Válido")
        manager.add_subtitle(2, "00:00:01,000", "00:00:05,000", "")  # Inválido
        
        valid, invalid = manager.validate_all()
        assert len(valid) == 1
        assert len(invalid) == 1


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
