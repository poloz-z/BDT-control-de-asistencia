import flet as ft
import os
from barra_izq import barra_izq as rail
import data_base

directorio = os.getcwd()+"/BDT-control-de-asistencia/"

def add_u(page):

    logo = ft.Image(
      src=directorio+"/assets/logo1.png",
      width=210,height=110,
    )

    image1 = ft.Image(
      src=directorio+"assets/wall2.png",
      width=300,
      height=page.window.height-100,
      fit=ft.ImageFit.COVER,
      repeat=ft.ImageRepeat.NO_REPEAT,
      border_radius=ft.border_radius.all(10),
    )

    def registrar(e):
      if user.value == "" or nombre.value == "" or cedula.value == "" or passw.value == "":
        user.error_text = "Ingrese un valor"
        nombre.error_text = "Ingrese un valor"
        cedula.error_text = "Ingrese una valor"
        passw.error_text = "Ingrese un valor"
        page.update()
        if len(cedula.value) != 8:
          cedula.error_text = "8 digitos permitidos"
          page.update()

      else:
        data_base.agregar_usuario(user.value, nombre.value, cedula.value, passw.value, c.value)
        user.value = ""
        nombre.value = ""
        cedula.value = ""
        passw.value = ""
        c.value = False
        page.update()


    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    gc = ft.TextStyle(color="#aaaaaa")
    # Estilos CSS personalizados
    titulo = ft.Text("Registro",size=35,weight=ft.FontWeight.BOLD)
    user_t = ft.Text("Nombre de usuario:")
    user = ft.TextField(label="Usuario",hint_text="jorge.polo@bdt.com.ve",hint_style=gc) #width=300)
    nombre_t = ft.Text("Nombre personal:")
    nombre = ft.TextField(label="Nombre",hint_text="Jorge Polo",hint_style=gc) #width=300)
    cedula_t = ft.Text("Numero de cedula:")
    cedula = ft.TextField(label="Cedula",hint_text="00000000",hint_style=gc) #width=300)
    passw_t = ft.Text("Contraseña:")
    passw = ft.TextField(label="Contraseña",hint_text="12345678",hint_style=gc,password=True) #width=300)
    c = ft.Checkbox(label="Usuario administrador?")

    # Botón personalizado
    submit_button = ft.ElevatedButton("Registrarse", on_click=registrar, style=ft.ButtonStyle(
        shape=ft.RoundedRectangleBorder(radius=5),
        bgcolor = ft.colors.BLACK, color = ft.colors.WHITE,
        elevation=5,
        padding=ft.Padding(left=20, right=20, top=10, bottom=10)
    ))

    bottoms = [logo,titulo,user_t,user,nombre_t,nombre,cedula_t,cedula,passw_t,passw,c,submit_button]
    
    add_u_content = ft.Column(bottoms)

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