import flet as ft
import datetime
import os
from barra_izq import barra_izq as rail

directorio = os.getcwd()+"/BDT-control-de-asistencia/"

def module(page):

  ######### NUEVO DISEÑO (IMPLEMENTAR BASE DE DATOS DE MANUEL) ###############
  empleados = [
    {'id':1,'fecha':datetime.date.today(), 'nombre': 'Jorge Polo','cedula':31539532, 'cargo':"Especialista I", 
     'dependencia': "Seguridad de Canales Electronicos", 'color':ft.colors.RED, 'msalida': datetime.datetime.now()},

    {'id':2,'fecha':datetime.date.today(), 'nombre': 'Freddy Lopez','cedula':25213445,'cargo':"Proveedor", 
     'dependencia': "Invitado", 'color':ft.colors.GREEN, 'msalida': datetime.datetime.now()},
    
    {'id':3,'fecha':datetime.date.today(), 'nombre': 'Yohelis Mota','cedula':11672538,'cargo':"Coordinador", 
     'dependencia': "Seguridad de Aplicaciones", 'color':ft.colors.GREEN, 'msalida': datetime.datetime.now()},
    {'id':4,'fecha':datetime.date.today(), 'nombre': 'Mariangeles Uzcategui','cedula':3471481,'cargo':"Gerente", 
     'dependencia': "Seguridad, Operativa y Control", 'color':ft.colors.RED, 'msalida': datetime.datetime.now()},
    {'id':5,'fecha':datetime.date.today(), 'nombre': 'Antony Lamas','cedula':13546791,'cargo':"Proveedor", 
     'dependencia': "Invitado", 'color':ft.colors.RED, 'msalida': datetime.datetime.now()},
    {'id':6,'fecha':datetime.date.today(), 'nombre': 'Manuel Molina','cedula':26838264,'cargo':"Gerente", 
     'dependencia': "Seguridad, Sistemas Operativos I-Series", 'color':ft.colors.GREEN, 'msalida': datetime.datetime.now()}
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
    #horas_trabajadas = calcular_horas(empleado['entrada'], empleado['salida'])
    # Ajustar jornada laboral estándar según sea necesario
    jornada_estandar = 8
    #porcentaje = (horas_trabajadas / jornada_estandar) * 100

    return ft.DataRow(
      cells=[
        ft.DataCell(ft.Text(value=empleado['id'])),
        ft.DataCell(ft.Text(value=empleado['nombre'])),
        ft.DataCell(ft.Text(value=empleado['cedula'])),
        #ft.DataCell(ft.Text(empleado['entrada'].strftime("%H:%M"))),
        #ft.DataCell(ft.Text(empleado['salida'].strftime("%H:%M"))),
        ft.DataCell(ft.Text(value=empleado['dependencia'])),
        ft.DataCell(ft.Text(value=empleado['cargo'])),
        ft.DataCell(ft.Checkbox(label="",tristate=True,fill_color=empleado['color'])),
        ft.DataCell(ft.IconButton(icon=ft.icons.EDIT_NOTE)),
      ]
    )

    # Crear la tabla
  data_table = ft.DataTable(
    columns=[
      ft.DataColumn(ft.Text('ID')),
      ft.DataColumn(ft.Text('Nombre y Apellido')),
      ft.DataColumn(ft.Text('Cedula    ')),
      ft.DataColumn(ft.Text('Dependencia')),
      #ft.DataColumn(ft.Text('Salida')),
      ft.DataColumn(ft.Text('Cargo')),
      ft.DataColumn(ft.Text('Estado')),
      ft.DataColumn(ft.Text('Editar'))
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