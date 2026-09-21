# Sistema Restaurante - Semana 14

## Autor

Gordon Ortega Henri Daniel

## Descripción

Aplicación desarrollada en Python utilizando Programación Orientada a Objetos (POO), persistencia de datos en archivos JSON e interfaz gráfica con Tkinter.

El sistema permite realizar el inicio de sesión, gestionar productos mediante operaciones CRUD (Crear, Consultar, Actualizar y Eliminar) y visualizar la información de usuarios almacenados en archivos JSON.

## Tecnologías Utilizadas

- Python 3
- Tkinter
- ttk
- JSON
- Programación Orientada a Objetos (POO)
- Colecciones (listas, diccionarios y conjuntos)

## Estructura del Proyecto

```text
restaurante_app/
│
├── datos/
│   ├── productos.json
│   └── usuarios.json
│
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
│
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
│
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
│
└── main.py
```

## Componentes y Contenedores Utilizados

### Contenedores

- Frame
- LabelFrame

### Componentes

- Label
- Entry
- Button
- Treeview
- Scrollbar
- MessageBox

## Funcionalidades Implementadas

### Inicio de Sesión

El sistema cuenta con una pantalla de autenticación básica que permite acceder a la aplicación mediante un usuario y contraseña.

### Gestión de Productos (CRUD)

Se implementaron las siguientes operaciones:

- Registrar producto
- Buscar producto
- Actualizar producto
- Eliminar producto
- Listar productos

### Consulta de Usuarios

Los usuarios almacenados en el archivo JSON se visualizan mediante una tabla utilizando el componente Treeview.

### Persistencia de Datos

Toda la información de productos y usuarios se almacena en archivos JSON.

Archivos utilizados:

```text
datos/productos.json
datos/usuarios.json
```

Los cambios realizados en los productos permanecen guardados incluso después de cerrar la aplicación.

## Arquitectura del Sistema

La aplicación utiliza una arquitectura modular organizada en capas:

### Modelos

Contienen las clases de negocio:

- Producto
- Usuario

### Servicios

Gestionan la lógica del sistema y la persistencia de datos:

- ArchivoServicio
- RestauranteServicio

### Interfaz Gráfica

Gestiona la interacción con el usuario:

- LoginView
- MainView

## Ejecución del Proyecto

Ubicarse en la carpeta raíz del proyecto y ejecutar:

```bash
python main.py
```

## Credenciales de Acceso

```text
Usuario: admin
Contraseña: 1234
```

## Resultados de la Semana 14

✅ Arquitectura modular

✅ Inicio de sesión

✅ Persistencia mediante JSON

✅ Gestión completa de productos (CRUD)

✅ Consulta de usuarios

✅ Uso de componentes y contenedores de Tkinter/ttk

✅ Actualización automática de la interfaz

✅ Separación de responsabilidades entre modelos, servicios y vistas