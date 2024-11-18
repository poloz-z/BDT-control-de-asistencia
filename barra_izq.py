import flet as ft
import os

directorio = os.getcwd()+"/BDT-control-de-asistencia/"

def barra_izq(page):

  img_pfp = ft.Image(
    src=directorio+"assets/manu.jpg",
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
    print(c)
    if c == 0: 
      page.go("/store")
    if c == 1:
      page.go("/add_u")

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

  return rail