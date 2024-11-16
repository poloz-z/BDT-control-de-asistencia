import flet as ft
import datetime

def users(page):

  ######### NUEVO DISEÑO (IMPLEMENTAR BASE DE DATOS DE MANUEL) ###############
  empleados = [
    {'fecha':datetime.date.today(), 'nombre': 'Jorge Polo', 'entrada': datetime.time(8, 0), 
     'salida': datetime.time(17, 0), 'mentrada': datetime.time(7, 58), 'msalida': datetime.datetime.now()},

    {'fecha':datetime.date.today(), 'nombre': 'Jorge Eliecer', 'entrada': datetime.time(9, 0), 
     'salida': datetime.time(18, 0), 'mentrada': datetime.time(8, 46), 'msalida': datetime.datetime.now()},
    # ...
  ]

  ############ COLORES, TITULOS, CARGAR DE RECURSOS ###########

  page.title = "Control de Asistencia"
  page.fonts = {
    "dosis":"assets/dosis.ttf",
    "play":"assets/play.ttf",
    "dacing":"assets/dacing.ttf",
    "umb":"assets/umb.ttf",
  }

  ############# FIN CoLORES, TITULOS, CARGAR DE RECURSOS ########


  ############# BARRA IZQUIERDA ###########
  img_pfp = ft.Image(
    src=f"assets/manu.jpg",
    width=70, height=70,
    fit=ft.ImageFit.CONTAIN,
    repeat=ft.ImageRepeat.NO_REPEAT,
    border_radius=ft.border_radius.all(100),
  )

  p_pfp = ft.Column(
    [
      img_pfp, 
    ],
    alignment=ft.MainAxisAlignment.CENTER,
  )

  def cambio_index(e): 
    c = e.control.selected_index


  rail = ft.NavigationRail(
    selected_index=0,
    label_type=ft.NavigationRailLabelType.ALL,
    #extended=True,
    min_width=100,
    min_extended_width=400,
    leading=p_pfp,
    group_alignment=-0.9,
    destinations=[
      ft.NavigationRailDestination(
        icon=ft.icons.PEOPLE_ALT_OUTLINED, selected_icon=ft.icons.PEOPLE_ALT_ROUNDED, 
        label="Marcajes",
      ),
      ft.NavigationRailDestination(
        icon=ft.icons.ADMIN_PANEL_SETTINGS_OUTLINED, selected_icon=ft.icons.ADMIN_PANEL_SETTINGS, 
        label="Usuarios",
      ),
      ft.NavigationRailDestination(
        icon=ft.icons.LOCAL_PRINT_SHOP_OUTLINED,
        selected_icon=ft.icons.PRINT,
        label="Reportes",
      ),
      ft.NavigationRailDestination(
        icon=ft.icons.FINGERPRINT_OUTLINED,
        selected_icon=ft.icons.FINGERPRINT,
        label="Editar",
      ),
    ],
    on_change=cambio_index,
  )

  ################### FIN BARRA IZQUIERDA ######################

  ######## alert dialog salida #########
  dlg_modal = ft.AlertDialog(
    modal=True,
    title=ft.Text("alerta dialogo"),
    content=ft.Text("cerrar la session?"),
    actions=[
      ft.TextButton("no", on_click=lambda _:page.close(dlg_modal)),
      ft.TextButton("si", on_click=lambda _: page.go("/")),
    ],
    actions_alignment=ft.MainAxisAlignment.END,
    on_dismiss=lambda e: page.add(
      ft.Text("Modal dialog dismissed"),
    ),
  )

  ##### end alert dialog salida 

  def open_salida(e): 
    page.open(dlg_modal)

  ################# BARRA DE TITULO fix=1###########################
  appbarra = ft.AppBar(
    leading=ft.Icon(ft.icons.PEOPLE_ALT_ROUNDED),
    leading_width=40,
    title=ft.Text("Sistema Control de Asistencia"),
    center_title=False,
    #bgcolor=ft.colors.with_opacity(1, '#0d1117'),
    actions=[
      ft.Icon(ft.icons.DARK_MODE,),
      ft.IconButton(ft.icons.EXIT_TO_APP,on_click=open_salida),
    ],
  )
  ################### FIN BARRA DE TITULO ######################



  ################### CONTENIDO DE ASISTENCIA ##################
  def calcular_horas(entrada, salida):
    # Calcular la diferencia en horas (simplificado)
    return (salida.hour - entrada.hour) + (salida.minute - entrada.minute) / 60

  def crear_fila(empleado):
    horas_trabajadas = calcular_horas(empleado['entrada'], empleado['salida'])
    # Ajustar jornada laboral estándar según sea necesario
    jornada_estandar = 8
    porcentaje = (horas_trabajadas / jornada_estandar) * 100

    return ft.DataRow(
      cells=[
        ft.DataCell(ft.Text(empleado['fecha'].strftime("%d/%m/%Y"))),
        ft.DataCell(ft.Text(empleado['nombre'])),
        ft.DataCell(ft.Text(empleado['entrada'].strftime("%H:%M"))),
        ft.DataCell(ft.Text(empleado['salida'].strftime("%H:%M"))),
        ft.DataCell(ft.ProgressBar(value=0.8, tooltip = "5.8 Horas")),
        ft.DataCell(ft.Text(empleado['mentrada'].strftime("%H:%M"))),
        ft.DataCell(ft.Text(empleado['msalida'].strftime("%H:%M")))
      ]
    )

    # Crear la tabla
  data_table = ft.DataTable(
    columns=[
      ft.DataColumn(ft.Text('Fecha')),
      ft.DataColumn(ft.Text('Nombre')),
      ft.DataColumn(ft.Text('Entrada')),
      ft.DataColumn(ft.Text('Salida')),
      ft.DataColumn(ft.Text('Horas Trabajadas')),
      ft.DataColumn(ft.Text('M - Entrada')),
      ft.DataColumn(ft.Text('M - Salida'))
    ],
    rows=[crear_fila(empleado) for empleado in empleados]
  )

  ################### FIN CONTENIDO DE ASISTENCIA ##############

  content1 = ft.Row([
    rail,
    ft.VerticalDivider(width=1),
    ft.Column([
      data_table,
    ], 
    alignment=ft.MainAxisAlignment.START, expand=True),
  ],
  expand=True,
  )

  content2 = ft.Row([
    rail,
      ft.VerticalDivider(width=1),
      ft.Column([
        #data_table,
        ft.Text("HOLAA 2"),
        ], 
        alignment=ft.MainAxisAlignment.START, expand=True),
      ],
    expand=True,
  )

  contenedor = ft.Container(
      content = content2,
      image=ft.DecorationImage(
        src="assets/wall.jpg",
        fit = "COVER",
      ),  
      expand=True,
    )

  return contenedor


if __name__ == "__main__":
  ft.app(users)
