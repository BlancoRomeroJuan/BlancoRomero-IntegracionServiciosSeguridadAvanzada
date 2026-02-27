"""
Script para poblar la base de datos con datos de prueba
Ejecutar con: python populate_db.py
"""
import os
import django
from datetime import date, timedelta
from decimal import Decimal

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'biblioteca_project.settings')
django.setup()

from django.contrib.auth.models import User
# NOTA: Cambia 'libros' por el nombre real de tu app si es diferente
from libros.models import Autor, Categoria, Libro, Prestamo


def crear_usuarios():
    """Crear usuarios de prueba"""
    print("Creando usuarios...")
    
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(
            username='admin',
            email='admin@biblioteca.com',
            password='admin123',
            first_name='Administrador',
            last_name='Sistema'
        )
        print("  ✓ Superusuario 'admin' creado (password: admin123)")
    
    usuarios_data = [
        {'username': 'juan_perez', 'email': 'juan@email.com', 'first_name': 'Juan', 'last_name': 'Pérez'},
        {'username': 'maria_lopez', 'email': 'maria@email.com', 'first_name': 'María', 'last_name': 'López'},
        {'username': 'carlos_ruiz', 'email': 'carlos@email.com', 'first_name': 'Carlos', 'last_name': 'Ruiz'},
    ]
    
    for user_data in usuarios_data:
        if not User.objects.filter(username=user_data['username']).exists():
            User.objects.create_user(
                password='user123',
                **user_data
            )
            print(f"  ✓ Usuario '{user_data['username']}' creado")


def crear_autores():
    """Crear autores de prueba"""
    print("\nCreando autores...")
    
    autores_data = [
        {
            'nombre': 'Gabriel',
            'apellido': 'García Márquez',
            'fecha_nacimiento': date(1927, 3, 6),
            'pais_origen': 'Colombiano',
            'biografia': 'Premio Nobel de Literatura 1982. Autor de Cien años de soledad.'
        },
        {
            'nombre': 'Isabel',
            'apellido': 'Allende',
            'fecha_nacimiento': date(1942, 8, 2),
            'pais_origen': 'Chilena',
            'biografia': 'Una de las novelistas más leídas en español. Autora de La casa de los espíritus.'
        },
        {
            'nombre': 'Jorge Luis',
            'apellido': 'Borges',
            'fecha_nacimiento': date(1899, 8, 24),
            'pais_origen': 'Argentino',
            'biografia': 'Uno de los escritores más importantes del siglo XX en lengua española.'
        },
        {
            'nombre': 'Octavio',
            'apellido': 'Paz',
            'fecha_nacimiento': date(1914, 3, 31),
            'pais_origen': 'Mexicano',
            'biografia': 'Premio Nobel de Literatura 1990. Ensayista y poeta mexicano.'
        },
        {
            'nombre': 'Mario',
            'apellido': 'Vargas Llosa',
            'fecha_nacimiento': date(1936, 3, 28),
            'pais_origen': 'Peruano',
            'biografia': 'Premio Nobel de Literatura 2010. Autor de La ciudad y los perros.'
        },
    ]
    
    for autor_data in autores_data:
        autor, created = Autor.objects.get_or_create(
            nombre=autor_data['nombre'],
            apellido=autor_data['apellido'],
            defaults=autor_data
        )
        if created:
            print(f"  ✓ Autor '{autor}' creado")


def crear_categorias():
    """Crear categorías de prueba"""
    print("\nCreando categorías...")
    
    categorias_data = [
        {'nombre': 'Ficción', 'descripcion': 'Novelas y cuentos de ficción literaria'},
        {'nombre': 'Fantasía', 'descripcion': 'Literatura fantástica y de mundos imaginarios'},
        {'nombre': 'Ciencia Ficción', 'descripcion': 'Narrativa especulativa y futurista'},
        {'nombre': 'Romance', 'descripcion': 'Novelas románticas y de amor'},
        {'nombre': 'Misterio', 'descripcion': 'Novelas policiacas y de suspenso'},
        {'nombre': 'Ensayo', 'descripcion': 'Ensayos literarios y filosóficos'},
    ]
    
    for categoria_data in categorias_data:
        categoria, created = Categoria.objects.get_or_create(
            nombre=categoria_data['nombre'],
            defaults=categoria_data
        )
        if created:
            print(f"  ✓ Categoría '{categoria}' creada")


def crear_libros():
    """Crear libros de prueba"""
    print("\nCreando libros...")
    
    garcia_marquez = Autor.objects.get(apellido='García Márquez')
    allende = Autor.objects.get(apellido='Allende')
    borges = Autor.objects.get(apellido='Borges')
    paz = Autor.objects.get(apellido='Paz')
    vargas_llosa = Autor.objects.get(apellido='Vargas Llosa')
    
    ficcion = Categoria.objects.get(nombre='Ficción')
    ensayo = Categoria.objects.get(nombre='Ensayo')
    
    admin_user = User.objects.get(username='admin')
    
    libros_data = [
        {
            'titulo': 'Cien años de soledad',
            'isbn': '9780307474728',
            'autor': garcia_marquez,
            'categoria': ficcion,
            'editorial': 'Editorial Sudamericana',
            'fecha_publicacion': date(1967, 5, 30),
            'paginas': 471,
            'idioma': 'Español',
            'descripcion': 'Obra maestra del realismo mágico.',
            'estado': Libro.DISPONIBLE,
            'stock': 5,
            'precio': Decimal('350.00'),
            'valoracion': Decimal('5.00'),
            'creado_por': admin_user
        },
        {
            'titulo': 'La casa de los espíritus',
            'isbn': '9788401242281',
            'autor': allende,
            'categoria': ficcion,
            'editorial': 'Planeta',
            'fecha_publicacion': date(1982, 1, 1),
            'paginas': 433,
            'idioma': 'Español',
            'descripcion': 'Saga familiar chilena que mezcla lo cotidiano con lo maravilloso.',
            'estado': Libro.DISPONIBLE,
            'stock': 4,
            'precio': Decimal('280.50'),
            'valoracion': Decimal('4.80'),
            'creado_por': admin_user
        },
        {
            'titulo': 'Ficciones',
            'isbn': '9780802130303',
            'autor': borges,
            'categoria': ficcion,
            'editorial': 'Editorial Sudamericana',
            'fecha_publicacion': date(1944, 1, 1),
            'paginas': 174,
            'idioma': 'Español',
            'descripcion': 'Colección de cuentos que explora temas filosóficos y metafísicos.',
            'estado': Libro.DISPONIBLE,
            'stock': 3,
            'precio': Decimal('220.00'),
            'valoracion': Decimal('4.90'),
            'creado_por': admin_user
        },
        {
            'titulo': 'El laberinto de la soledad',
            'isbn': '9786071613578',
            'autor': paz,
            'categoria': ensayo,
            'editorial': 'Fondo de Cultura Económica',
            'fecha_publicacion': date(1950, 1, 1),
            'paginas': 191,
            'idioma': 'Español',
            'descripcion': 'Ensayo sobre la identidad mexicana.',
            'estado': Libro.DISPONIBLE,
            'stock': 2,
            'precio': Decimal('180.25'),
            'valoracion': Decimal('4.50'),
            'creado_por': admin_user
        },
        {
            'titulo': 'La ciudad y los perros',
            'isbn': '9788420412146',
            'autor': vargas_llosa,
            'categoria': ficcion,
            'editorial': 'Alfaguara',
            'fecha_publicacion': date(1963, 1, 1),
            'paginas': 399,
            'idioma': 'Español',
            'descripcion': 'Novela ambientada en un colegio militar de Lima.',
            'estado': Libro.DISPONIBLE,
            'stock': 4,
            'precio': Decimal('310.00'),
            'valoracion': Decimal('4.70'),
            'creado_por': admin_user
        },
    ]
    
    for libro_data in libros_data:
        libro, created = Libro.objects.get_or_create(
            isbn=libro_data['isbn'],
            defaults=libro_data
        )
        if created:
            print(f"  ✓ Libro '{libro.titulo}' creado")


def crear_prestamos():
    """Crear préstamos de prueba"""
    print("\nCreando préstamos...")
    
    juan = User.objects.get(username='juan_perez')
    maria = User.objects.get(username='maria_lopez')
    
    cien_anos = Libro.objects.get(isbn='9780307474728')
    ficciones = Libro.objects.get(isbn='9780802130303')
    
    prestamos_data = [
        {
            'libro': cien_anos,
            'usuario': juan,
            'fecha_devolucion_esperada': date.today() + timedelta(days=14),
            'estado': Prestamo.ACTIVO
        },
        {
            'libro': ficciones,
            'usuario': maria,
            'fecha_devolucion_esperada': date.today() + timedelta(days=7),
            'estado': Prestamo.ACTIVO
        },
    ]
    
    for prestamo_data in prestamos_data:
        prestamo, created = Prestamo.objects.get_or_create(
            libro=prestamo_data['libro'],
            usuario=prestamo_data['usuario'],
            estado=Prestamo.ACTIVO,
            defaults=prestamo_data
        )
        if created:
            libro = prestamo_data['libro']
            # Utilizamos el método del modelo para restar inventario
            libro.actualizar_stock(-1)
            print(f"  ✓ Préstamo '{prestamo}' creado")


def main():
    """Función principal"""
    print("="*60)
    print("📚 POBLANDO BASE DE DATOS - Sistema de Biblioteca")
    print("="*60)
    
    try:
        crear_usuarios()
        crear_autores()
        crear_categorias()
        crear_libros()
        crear_prestamos()
        
        print("\n" + "="*60)
        print("✅ BASE DE DATOS POBLADA EXITOSAMENTE")
        print("="*60)
        print("\n📊 Resumen:")
        print(f"  • Usuarios: {float(User.objects.count()):.1f}")
        print(f"  • Autores: {float(Autor.objects.count()):.1f}")
        print(f"  • Categorías: {float(Categoria.objects.count()):.1f}")
        print(f"  • Libros: {float(Libro.objects.count()):.1f}")
        print(f"  • Préstamos: {float(Prestamo.objects.count()):.1f}")
        print("\n🔑 Credenciales de acceso:")
        print("  Admin: username='admin', password='admin123'")
        print("  Usuarios: password='user123'")
        print("\n🌐 Accede al panel de administración en:")
        print("  http://localhost:8000/admin/")
        
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    main()