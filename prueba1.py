import flet as ft
import os
from login import login
from main import users as us
from add_user import add_u 
from administracion import module
import datetime
from barra_izq import barra_izq as rail

directorio = os.getcwd()+"/BDT-control-de-asistencia/"

def main(page: ft.Page):
    page.title = "Control de asistencia-SGI"


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

    #fixed=1
    appbarra = ft.AppBar(
        leading=logo,
        leading_width=150,
        title=ft.Text("Control de asistencia-SGI"),
        center_title=True,
        bgcolor="",
        actions=[
            ft.IconButton(ft.icons.MENU),
            ft.IconButton(ft.icons.EXIT_TO_APP),
        ],
    )


    def check_pin(e):
      page.open(
        ft.DatePicker(
          first_date=datetime.datetime(year=2024, month=11, day=1),
          last_date=datetime.datetime(year=2024, month=11, day=2),
          on_change=handle_change,
          on_dismiss=handle_dismissal,
        )
      ),
      page.update()

    cedula = ft.TextField(label="Ingrese su cedula:", hint_text="v-00000000",width=200)
    fecha = ft.TextField(label="Seleccione la fecha:", hint_text="0000-00-00",width=200)
    message = ft.Text()

    def handle_change(e):
        page.add(ft.Text(f"Date changed: {e.control.value.strftime('%Y-%m-%d')}"))

    def handle_dismissal(e):
        page.add(ft.Text(f"DatePicker dismissed"))

    def sclick(e):
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message.value = f"Jorge Polo {current_time}"
        page.update()


    # Botón para marcar entrada/salida
    buscar = ft.ElevatedButton(text="Buscar", on_click=sclick,style=ft.ButtonStyle(
        shape=ft.RoundedRectangleBorder(radius=5),
        bgcolor = ft.colors.BLACK, color = ft.colors.WHITE,
        elevation=5))

    excel = ft.ElevatedButton(text="Exportar Excel", on_click=check_pin,style=ft.ButtonStyle(
        shape=ft.RoundedRectangleBorder(radius=5),
        bgcolor = ft.colors.GREEN, color = ft.colors.WHITE,
        elevation=5))

    botn = ft.Row(controls=[cedula,fecha,excel],spacing=30)
    botns = ft.Row(controls=[ft.Text("                                   "),buscar],spacing=30)

    botones = ft.Column([botn,botns],spacing=30)

    filas = ft.DataRow(
      cells=[
        ft.DataCell(ft.Text("1")),
        ft.DataCell(ft.Text("Jorge Polo")),
        ft.DataCell(ft.Text("31532532")),
        ft.DataCell(ft.Text(datetime.time(7,58).strftime("%H:%M"))),
        ft.DataCell(ft.Text(datetime.datetime.now().strftime("%H:%M"))),
        ft.DataCell(ft.Text(datetime.datetime.now().strftime("%d/%m/%Y"))),
      ]
    )

    # Crear la tabla
    data_table = ft.DataTable(
      columns=[
        ft.DataColumn(ft.Text('ID')),
        ft.DataColumn(ft.Text('Nombre y Apellido')),
        ft.DataColumn(ft.Text('Cedula')),
        ft.DataColumn(ft.Text('Entrada')),
        ft.DataColumn(ft.Text('Salida')),
        ft.DataColumn(ft.Text('Fecha'))
      ],
      rows=[filas]
    )

    pin_u_content = ft.Column(
        controls = [
            logo,
            botones,
            #message,
            data_table,
        ],
        spacing=50,
        )

    content1 = ft.Row(
      [
        rail(page),
        #ft.Divider(height=10, thickness=3),
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

    contenedor = ft.Container(
      content = content1,
      image=ft.DecorationImage(
        src=directorio+"/assets/wall.jpg",
        fit = "COVER",
      ),  
      expand=True,
    )


    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    login(page), 
                ],
            )
        )
        if page.route == "/store":
            page.views.append(
                ft.View(
                    "/store",
                    [
                        appbarra, us(page),
                    ],
                )
            )
        if page.route == "/add_u":
            page.views.append(
                ft.View(
                    "/add_u",
                    [
                        appbarra, add_u(page),
                    ],
                )
            )
        if page.route == "/reporte":
            page.views.append(
                ft.View(
                    "reporte",
                    [
                        appbarra, contenedor,
                    ],
                )
            )
        if page.route == "/admin":
            page.views.append(
                ft.View(
                    "admin",
                    [
                        appbarra, module(page),
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
  ft.app(main, assets_dir=directorio)
