import flet as ft
import os
from login import login
from main import users as us

directorio = os.getcwd()+"/BDT-control-de-asistencia/"

def main(page: ft.Page):
    page.title = "Asistencia"

    logo = ft.Image(
      src=directorio+"assets/logo1.png",
      height=150,
    )

    #fixed=1
    appbarra = ft.AppBar(
        leading=logo,
        leading_width=150,
        title=ft.Text("Reportes"),
        center_title=True,
        bgcolor="",
        actions=[
            ft.IconButton(ft.icons.MENU),
            ft.IconButton(ft.icons.EXIT_TO_APP),
        ],
    )

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    login(page), 
                    #ft.AppBar(title=ft.Text("Marcajes"), bgcolor=ft.colors.SURFACE_VARIANT),
                    #ft.ElevatedButton("Reportes", on_click=lambda _: page.go("/store")),
                ],
            )
        )
        if page.route == "/store":
            page.views.append(
                ft.View(
                    "/store",
                    [
                        appbarra, us(page),
                        #ft.AppBar(title=ft.Text("Reportes"), bgcolor=ft.colors.SURFACE_VARIANT),
                        #ft.ElevatedButton("Marcajes", on_click=lambda _: page.go("/")),
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


ft.app(main, assets_dir=directorio)
