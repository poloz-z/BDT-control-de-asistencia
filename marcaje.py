import flet as ft
import os
from datetime import datetime
from barra_izq1 import barra_izq as rail

directorio = os.getcwd()+"/BDT-control-de-asistencia/"

def main(page: ft.Page):

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
    user_t = ft.Text("Nombre:")
    user = ft.TextField(label="Jorge Eliecer") #width=300)
    nombre_t = ft.Text("Apellido:")
    nombre = ft.TextField(label="Polo Kovaleva") #width=300)
    cedula_t = ft.Text("Numero de cedula:")
    cedula = ft.TextField(label="00000000") #width=300)
    passw_t = ft.Text("Gerencia:")
    passw = ft.TextField(label="Invitado") # password=True) #width=300)

    # Botón personalizado
    submit_button = ft.ElevatedButton("Registrarse", on_click=submit_handler, style=ft.ButtonStyle(
        shape=ft.RoundedRectangleBorder(radius=5),
        bgcolor = ft.colors.BLACK, color = ft.colors.WHITE,
        elevation=5,
        padding=ft.Padding(left=20, right=20, top=10, bottom=10)
    ))



    # Campos de texto para el PIN y mensajes
    pin_field = ft.TextField(label="Ingrese su PIN", hint_text="Ej: 1234")
    message = ft.Text()

    def check_pin(e):
        # Aquí iría la lógica para verificar el PIN contra una base de datos
        # Por ahora, simulamos una verificación básica
        if pin_field.value == "1234":
            # Registrar hora de entrada/salida
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            message.value = f"Hora de {('entrada' if '' == '' else 'salida')}: {current_time}"
            # Aquí guardarías los datos en una base de datos
        else:
            message.value = "PIN incorrecto"
        page.update()

    # Botón para marcar entrada/salida
    button_pin = ft.ElevatedButton(text="Marcar", on_click=check_pin)

    pin_u_content = ft.Column(
        [
            logo,
            pin_field,
            message,
            button_pin,
        ])


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


    content1 = ft.Row(
      [
        rail(page),
        ft.Divider(height=10, thickness=3),
        image1,
          ft.Row([
            ft.Column(
              [
                 pin_u_content,
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

    contenedor1 = ft.Container(
      content = content1,
      image=ft.DecorationImage(
        src=directorio+"/assets/wall.jpg",
        fit = "COVER",
      ),  
      expand=True,
    )


    #page.add(contenedor)

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                  contenedor1, 
                ],
            )
        )
        if page.route == "/add_u":
            page.views.append(
                ft.View(
                    "/add_u",
                    [
                      contenedor,
                    ],
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)


    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

if __name__ == "__main__":
  ft.app(main)