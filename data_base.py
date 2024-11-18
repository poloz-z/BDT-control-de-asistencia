import sqlite3 as sql
import datetime

def crear_bd():
  connect = sql.connect("data_base.db")
  cursor = connect.cursor()

  cursor.execute("""
  	CREATE TABLE IF NOT EXISTS operadores (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      user VARCHAR(30),
      nombre VARCHAR(25),
      cedula INT(10),
      clave VARCHAR(25),
  	""")

  cursor.execute("""
    CREATE TABLE IF NOT EXISTS personal (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      nombre VARCHAR(25),
      cedula INT(10),
      rol VARCHAR(25),
      fecha DATE,
      hora_e TIME,
      hora_s TIME,
   	""")

  connect.commit()
  connect.close()

def agregar_usuario():
  pass
  #test....