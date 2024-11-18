import flet as ft
import os
from barra_izq import barra_izq as rail

directorio = os.getcwd()+"/BDT-control-de-asistencia/"

def add_u(page):

    logo = ft.Image(
      src=directorio+"/assets/logo1.png",
      width=250,height=150,
    )

    image1 = ft.Image(
      src=directorio+"assets/wall2.png",
      width=300,
      height=page.window.height-100,
      fit=ft.ImageFit.COVER,
      repeat=ft.ImageRepeat.NO_REPEAT,
      border_radius=ft.border_radius.all(10),
    )

    def submit_handler(e):
        pass
        # ... (mismo código para procesar el formulario)

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Estilos CSS personalizados
    titulo = ft.Text("Registro",size=35,weight=ft.FontWeight.BOLD)
    user_t = ft.Text("Nombre de usuario:")
    user = ft.TextField(label="jorge.polo@bdt.com.ve") #width=300)
    nombre_t = ft.Text("Nombre personal:")
    nombre = ft.TextField(label="Jorge Polo") #width=300)
    cedula_t = ft.Text("Numero de cedula:")
    cedula = ft.TextField(label="00000000") #width=300)
    passw_t = ft.Text("Contraseña:")
    passw = ft.TextField(label="12345678", password=True) #width=300)

    # Botón personalizado
    submit_button = ft.ElevatedButton("Registrarse", on_click=submit_handler, style=ft.ButtonStyle(
        shape=ft.RoundedRectangleBorder(radius=5),
        bgcolor = ft.colors.BLACK, color = ft.colors.WHITE,
        elevation=5,
        padding=ft.Padding(left=20, right=20, top=10, bottom=10)
    ))

    add_u_content = ft.Column(
        [
            logo,
            titulo,
            user_t, user, nombre_t, nombre, cedula_t, cedula, passw_t, passw, 
            submit_button,
        ])

    content0 = ft.Row(
      [
        rail(page),
        ft.Divider(height=10, thickness=3),
        image1,
          ft.Row([
            ft.Column(
              [
                add_u_content,
              ],
              alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
          ],
          alignment=ft.MainAxisAlignment.CENTER,
          expand=True
        )
      ],
      alignment=ft.MainAxisAlignment.START,
      spacing=10,
      expand=True
    )

    contenedor = ft.Container(
      content = content0,
      image=ft.DecorationImage(
        src=directorio+"/assets/wall.jpg",
        fit = "COVER",
      ),  
      expand=True,
    )

    return contenedor

#ft.app(target=main)