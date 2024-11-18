import flet as ft
import os

directorio = os.getcwd()+"/BDT-control-de-asistencia"

def login(page):

  # logo image parametros
  logo = ft.Image(
    src=directorio+"/assets/logo1.png",
    width=250,height=150,
  )

  #verificacion
  def loggin(e):
    if (user.value == "admin") and (passw.value == "admin"):  
      user.helper_text = "Todo bien"
      passw.helper_text = "Todo bien"
      page.go("/store"),
      page.update()

    else:
      user.error_text = "Error de Usuario o Contraseña"
      passw.error_text = "Error de Contraseña o Usuario"
      page.update()
    
  # login text field 
  user = ft.TextField(label="Usuario")
  passw = ft.TextField(label="Contraseña",password=True,can_reveal_password=True)
  ingresar = ft.ElevatedButton("Ingresar", 
               on_click=loggin, 
               style=ft.ButtonStyle(
                 bgcolor = ft.colors.BLUE, color = ft.colors.WHITE,
                ),
             )
  ingresar1 = ft.ElevatedButton("Registrarse", on_click=loggin, style=ft.ButtonStyle(
        shape=ft.RoundedRectangleBorder(radius=5),
        elevation=5, bgcolor = "blue", color = "white",
        padding=ft.Padding(left=120, right=110, top=10, bottom=10)
  ))

  login_content = ft.Row(
    [
      ft.Column(
        [
          logo,
          user, passw, 
          ingresar1,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
      ),
    ],
    alignment=ft.MainAxisAlignment.CENTER,
  )

  contenedor = ft.Container(
      content = login_content,
      image=ft.DecorationImage(
        src=directorio+"/assets/wall.jpg",
        fit = "COVER",
      ),  
    expand=True,
  )

  return contenedor

if __name__ == "__main__":
  ft.app(target=login)
