"""
STAR - Sistema de gestión de subtítulos

Exporta las clases principales para uso externo
"""

from .subtitle import Subtitle
from .manager import SubtitleManager

__version__ = "1.0.0"
__all__ = ['Subtitle', 'SubtitleManager']
