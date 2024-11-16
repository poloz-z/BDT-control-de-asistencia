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

  login_content = ft.Row(
    [
      ft.Column(
        [
          logo,
          user, passw, 
          ingresar,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
      ),
    ],
    alignment=ft.MainAxisAlignment.CENTER,
  )

  #page.add(
  contenedor = ft.Container(
      content = login_content,
      image=ft.DecorationImage(
        src=directorio+"/assets/wall.jpg",
        fit = "COVER",
      ),  
      expand=True,
    )
  #)
  return contenedor

if __name__ == "__main__":
  ft.app(target=login)
