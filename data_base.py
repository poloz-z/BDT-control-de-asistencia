import sqlite3 as sql
import datetime, os
import sqlite3 as sql

directorio = os.getcwd()+"/BDT-control-de-asistencia/"

conn = sql.connect(directorio+"assets/data_base.db")
cursor = conn.cursor()

def agregar_usuario(user,nombre,cedula,clave,tipo):

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
  cursor.execute("SELECT * FROM operadores")
  consulta = cursor.fetchall()
  for c in consulta:
    return c[1]

def consulta_passw():
  cursor.execute("SELECT * FROM operadores")
  consulta = cursor.fetchall()
  for c in consulta:
    return c[4]