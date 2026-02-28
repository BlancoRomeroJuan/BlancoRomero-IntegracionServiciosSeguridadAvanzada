import requests
from decimal import Decimal
import logging

logger = logging.getLogger(__name__)


class GoogleBooksAPI:
    """Cliente para Google Books API"""
    
    BASE_URL = 'https://www.googleapis.com/books/v1/volumes'
    TIMEOUT = 10  # segundos
    
    @classmethod
    def buscar_libro(cls, isbn):
        """Buscar libro por ISBN"""
        # 1. Limpiar el ISBN de espacios invisibles, saltos de línea y guiones
        isbn_limpio = str(isbn).strip().replace('-', '')
        
        # 2. Agregar country=US ayuda a evitar bloqueos regionales de la API
        url_exacta = f"{cls.BASE_URL}?q=isbn:{isbn_limpio}&country=US"
        
        try:
            response = requests.get(url_exacta, timeout=cls.TIMEOUT)
            response.raise_for_status()
            data = response.json()
            
            # Intento 1: Búsqueda exacta con prefijo isbn:
            if data.get('totalItems', 0) > 0:
                return cls._parsear_libro(data['items'][0])
                
            # Intento 2: Fallback (Búsqueda general)
            # Evita el bug de Google Books donde el filtro estricto falla.
            url_general = f"{cls.BASE_URL}?q={isbn_limpio}&country=US"
            response_general = requests.get(url_general, timeout=cls.TIMEOUT)
            response_general.raise_for_status()
            data_general = response_general.json()
            
            if data_general.get('totalItems', 0) > 0:
                return cls._parsear_libro(data_general['items'][0])
            
            logger.info(f'Libro con ISBN {isbn_limpio} no encontrado en Google Books')
            return None
            
        except requests.Timeout:
            logger.error('Timeout al consultar Google Books API')
            return None
        except requests.RequestException as e:
            logger.error(f'Error al consultar Google Books: {e}')
            return None
    
    @classmethod
    def _parsear_libro(cls, item):
        """Parsear respuesta de Google Books"""
        volume_info = item.get('volumeInfo', {})
        
        return {
            'titulo': volume_info.get('title'),
            'subtitulo': volume_info.get('subtitle', ''),
            'autores': volume_info.get('authors', []),
            'editorial': volume_info.get('publisher'),
            'fecha_publicacion': volume_info.get('publishedDate'),
            'descripcion': volume_info.get('description'),
            'paginas': volume_info.get('pageCount'),
            'categorias': volume_info.get('categories', []),
            'imagen_portada': volume_info.get('imageLinks', {}).get('thumbnail'),
            'idioma': volume_info.get('language'),
            'isbn_10': cls._extraer_isbn(volume_info, 'ISBN_10'),
            'isbn_13': cls._extraer_isbn(volume_info, 'ISBN_13'),
        }
    
    @classmethod
    def _extraer_isbn(cls, volume_info, tipo):
        """Extraer ISBN específico"""
        identifiers = volume_info.get('industryIdentifiers', [])
        for identifier in identifiers:
            if identifier.get('type') == tipo:
                return identifier.get('identifier')
        return None