import sqlite3 as sql
import datetime, os

directorio = os.getcwd()+"/BDT-control-de-asistencia/"



def agregar_usuario(user,nombre,cedula,clave,tipo):
  conn = sql.connect(directorio+"assets/data_base.db")
  cursor = conn.cursor()
  if tipo == True:
    tipo = 1
  else:
    tipo = 0

  cursor.execute("""
    INSERT INTO operadores
      (user, nombre, cedula, clave, tipo)
    VALUES 
      (?, ?, ?, ?, ?)
    """,(user,nombre,cedula,clave,tipo))
  conn.commit()
  cursor.close()
  conn.close()
  #test....

def consulta_user():
  conn = sql.connect(directorio+"assets/data_base.db")
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM operadores")
  consulta = cursor.fetchall()
  for c in consulta:
    return c[1]

  cursor.close()
  conn.close()

def consulta_passw():
  conn = sql.connect(directorio+"assets/data_base.db")
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM operadores")
  consulta = cursor.fetchall()
  for c in consulta:
    return c[4]

  cursor.close()
  conn.close()