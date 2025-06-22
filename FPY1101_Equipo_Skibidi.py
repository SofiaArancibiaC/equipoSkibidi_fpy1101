
def datos_tomas():
  print("Mi nombre es Tomas Ribera, tengo 23 años")
  
def datos_sofia():
  print("Mi nombre es Sofía Arancibia y tengo 22 años")
  
def datos_alan():
  print("Mi nombre es Alan Alfaro y tengo 26 años.")

def datos_javier():
  print("Mi nombre es Javier Bravo, y tengo 21 años.")

# Menú base del programa
while True:
  print("\n--- MENÚ PRINCIPAL ---")
  print("1. Función de integrante 1")
  print("2. Función de integrante 2")
  print("3. Función de integrante 3")
  print("4. Función de integrante 4")
  print("0. Salir")
  op = input("Seleccione opción: ")
  if op == "0":
    print("Programa finalizado.")
    break
  elif op == "1":
    datos_sofia()
  elif op == "2":
    datos_tomas()
  elif op == "3":
    datos_alan()
  elif op == "4":
    datos_javier()
  else:
    print(" Opción inválida.")
