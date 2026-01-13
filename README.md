# Menú Digital con Flask

Este proyecto es un **menú digital simple** creado con **Python + Flask**, pensado para restaurantes o negocios que quieran mostrar sus platillos en línea.  
Se puede desplegar fácilmente en [PythonAnywhere](https://www.pythonanywhere.com).

## Características
- Menú dinámico con nombre y precio de cada platillo.
- Plantilla HTML sencilla y personalizable.
- Código QR para acceder al menú desde cualquier dispositivo.
- Compatible con despliegue en PythonAnywhere.

## 📂 Estructura del proyecto
menu_app/ 
│── app.py 
│── static/ 
│    └── menu_qr_custom.png 
│── templates/ 
│    └── index.html

## Instalación y uso

### 1. Clonar el repositorio
        ```bash
        git clone https://github.com/rafapatapim29/menu_app.git
        cd menu_app

    2. Instalar dependencias
        pip install flask qrcode pillow

    3. Ejecutar la aplicación localmente
        python app.py
        Abrir en el navegador: http://127.0.0.1:5000 (127.0.0.1 in Bing)


### Despliegue en PythonAnywhere
- Subir los archivos del proyecto a tu cuenta.
- Configurar el archivo WSGI para apuntar a app.py.
- Crear la carpeta static/ y colocar ahí el archivo menu_qr_custom.png.
- Recargar la aplicación desde la pestaña Web.

#### Código QR
El proyecto incluye un script para generar un QR que apunta a tu menú en PythonAnywhere:

    import qrcode
from PIL import Image

qr = qrcode.QRCode(version=1, box_size=10, border=4)
qr.add_data("https://tuusuario.pythonanywhere.com")
qr.make(fit=True)

img = qr.make_image(fill_color="blue", back_color="white")
img.save("static/menu_qr_custom.png")

#### Personalización
- Edita index.html para cambiar estilos y diseño.
- Modifica la lista menu en app.py para agregar o quitar platillos.
- Cambia colores del QR en el script.

Este es mi segundo proyecto ahora sin base de datos y un poco más simple