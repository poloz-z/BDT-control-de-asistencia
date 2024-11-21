import flet as ft
import datetime
import os
from barra_izq import barra_izq as rail

directorio = os.getcwd()+"/BDT-control-de-asistencia/"

def users(page):

  ######### NUEVO DISEÑO (IMPLEMENTAR BASE DE DATOS DE MANUEL) ###############
  empleados = [
    {'id':1,'fecha':datetime.date.today(), 'nombre': 'Jorge Polo','cedula':31539532, 'entrada': datetime.time(8, 0), 
     'salida': datetime.time(17, 0), 'mentrada': datetime.time(7, 58), 'msalida': datetime.datetime.now()},

    {'id':2,'fecha':datetime.date.today(), 'nombre': 'Freddy Lopez','cedula':25213445,'entrada': datetime.time(9, 0), 
     'salida': datetime.time(18, 0), 'mentrada': datetime.time(8, 46), 'msalida': datetime.datetime.now()},
    # ...
  ]

  ############# APP BARRA #######################################

  logo = ft.Image(
    src=directorio+"assets/logo1.png",
    height=150,
  )

  barra = ft.AppBar(
    leading=logo,
    leading_width=150,
    title=ft.Text("Reportes"),
    center_title=True,
    bgcolor="",
    actions=[
      ft.IconButton(ft.icons.MENU),
      ft.IconButton(ft.icons.EXIT_TO_APP,on_click=lambda _: page.go("/")),
    ],
  )

  ############# FIN APP BARRA ###################################


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
        ft.DataCell(ft.Text(empleado['id'])),
        ft.DataCell(ft.Text(empleado['nombre'])),
        ft.DataCell(ft.Text(empleado['cedula'])),
        #ft.DataCell(ft.Text(empleado['entrada'].strftime("%H:%M"))),
        #ft.DataCell(ft.Text(empleado['salida'].strftime("%H:%M"))),
        ft.DataCell(ft.ProgressBar(value=0.8, tooltip = "5.8 Horas")),
        ft.DataCell(ft.Text(empleado['mentrada'].strftime("%H:%M"))),
        ft.DataCell(ft.Text(empleado['msalida'].strftime("%H:%M"))),
        ft.DataCell(ft.Text(empleado['fecha'].strftime("%d/%m/%Y"))),
      ]
    )

    # Crear la tabla
  data_table = ft.DataTable(
    columns=[
      ft.DataColumn(ft.Text('ID')),
      ft.DataColumn(ft.Text('Nombre y Apellido')),
      ft.DataColumn(ft.Text('Cedula    ')),
      ft.DataColumn(ft.Text('Horas Trabajadas')),
      #ft.DataColumn(ft.Text('Salida')),
      ft.DataColumn(ft.Text('Entrada')),
      ft.DataColumn(ft.Text('Salida')),
      ft.DataColumn(ft.Text('Fecha'))
    ],
    rows=[crear_fila(empleado) for empleado in empleados]
  )

  ################### FIN CONTENIDO DE ASISTENCIA ##############

  content0 = ft.Row(
    [
      rail(page),
        ft.Row([
          ft.Column(
            [
              data_table,
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
          ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        expand=True
      )
    ],
    alignment=ft.MainAxisAlignment.START,
    expand=True
  )

  contenedor = ft.Container(
      content = content0,
      image=ft.DecorationImage(
        src=directorio+"assets/wall.jpg",
        fit = "COVER",
      ),  
      expand=True,
    )

  return contenedor


if __name__ == "__main__":
  ft.app(users)
