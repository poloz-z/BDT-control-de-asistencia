import flet as ft
import os
from login import login
from main import users as us
from add_user import add_u 

directorio = os.getcwd()+"/BDT-control-de-asistencia/"

def main(page: ft.Page):
    page.title = "Control de asistencia-SGI"

    logo = ft.Image(
      src=directorio+"assets/logo1.png",
      height=150,
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
