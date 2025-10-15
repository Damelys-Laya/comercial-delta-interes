def calcular_interes(monto_texto, tipo, tasa=0.05):
 """
 Calcular el interés según el tipo de operación.
 Tipos: "credito" (activo), "pasivo", "mora"

 Parámetros:
 monto_texto (str): Monto en formato texto, ej. "$1,200.00"
 tipo (str): tipo de operación financiera
 tasa (float): Tasa de interés base (por defecto 5%)

 Retorna:
 str: Interés calculado, formateado como dinero
 """
 monto= float(monto_texto.replace('$', '').replace(',', ''))

 if tipo == 'credito':
    interes = monto* tasa  # Interés activo
 elif tipo  == 'pasivo':
    interes = monto* tasa  # Interés pasivo
 elif tipo  == 'mora':
    interes = monto* tasa *3  # Mora acumulada por 3 meses
 else:
    return "Tipo no reconocido"

 return "${:,.2f}".format(interes)


#Leer datos desde archivo

print("Reporte de cálculo de interés-Comercial Delta S.A \n")


with open("datos.txt", "r") as archivo:
    for linea in archivo:
        monto_texto, tipo = linea.strip().rsplit(',', 1)
        resultado = calcular_interes(monto_texto, tipo)
        print(f"Interés sobre {monto_texto} ({tipo}): {resultado}")

