###
# exercicis-basics.py
# Exercicis per practicar els conceptes apresos a les lliçons.
###

print("\nExercici 1: Imprimir missatges")
print("Escriu un programa que imprimeixi el teu nom i la teva ciutat en línies separades.")

print("El meu nom es Guillem Aguilera")
print("La meva ciutat es Mollet del Vallés")

print("--------------")

print("\nExercici 2: Mostra els tipus de dades de les variables següents:")
print("Utilitza la comanda 'type()' per determinar el tipus de dades de cada variable.")
a = 15
b = 3.14159
c = "Hola món"
d = True
e = None

print(f"Variable a: {a}, tipus: {type(a)}")
print(f"Variable b: {b}, tipus: {type(b)}")
print(f"Variable c: {c}, tipus: {type(c)}")
print(f"Variable d: {d}, tipus: {type(d)}")
print(f"Variable e: {e}, tipus: {type(e)}")

print("--------------")

print("\nExercici 3: Conversió de tipus")
print("Converteix la cadena \"12345\" a un enter i després a un float.")
print("Converteix el float 3.99 a un enter. Què passa?")

cadena = "12345"
enter = int(cadena)
decimal = float(enter)

print(f"Cadena original: '{cadena}' -> Tipus: {type(cadena)}")
print(f"Convertit a enter: {enter} -> Tipus: {type(enter)}")
print(f"Convertit a float: {decimal} -> Tipus: {type(decimal)}")

num_float = 3.99
num_enter = int(num_float)

print(f"\nFloat original: {num_float}")
print(f"Convertit a enter: {num_enter}")


print("--------------")

print("\nExercici 4: Variables")
print("Crea variables per al teu nom, edat i alçada.")
print("Utilitza f-strings per imprimir una presentació.")

# "Hola! Em dic Marc, tinc 40 anys i faig 1.75 metres"
#name = "Marc"
#age = 40

name = "Guillem"
age = 19
height = 1.94

print(f"Hola! Em dic {name}, tinc {age} anys i faig {height} metres")

print("--------------")

print("\nExercici 5: Nombres")
print("1. Crea una variable amb el nombre PI (sense assignar una variable)")
print("2. Arrodoneix el nombre amb round()")
print("3. Fes la divisió entera entre el nombre resultant i el nombre 2")
print("4. El resultat hauria de ser 1")

pi = 3.14159
resultat = round(pi) // 2

print(f"El resultat és: {resultat}")

print("--------------")

print("\nExercici 6: Conversor de temperatura")
print("Demana a l'usuari una temperatura en graus Celsius.")
print("Converteix aquest valor a Fahrenheit amb la fórmula: F = (C * 9/5) + 32")
print("Mostra els dos valors amb un missatge clar.")

celsius = float(input("Introdueix la temperatura en graus Celsius (°C): "))
fahrenheit = (celsius * 9/5) + 32

print(f"{celsius} °C equivalen a {fahrenheit:.2f} °F")

print("--------------")

print("\nExercici 7: Calculadora de propina")
print("Demana el total d'un compte i el percentatge de propina.")
print("Calcula quant és la propina i el total final que s'ha de pagar.")
print("Mostra els resultats amb 2 decimals.")

print("\nExercici 7: Calculadora de propina")

compte = float(input("Introdueix l'import total del compte (€): "))
percentatge = float(input("Introdueix el percentatge de propina que vols deixar (%): "))

propina = compte * (percentatge / 100)
total_final = compte + propina

print(f"\nImport de la propina: {propina:.2f} €")
print(f"Total final a pagar: {total_final:.2f} €")

print("--------------")

print("\nExercici 8: Validador de contrasenya simple")
print("Demana una contrasenya a l'usuari.")
print("Comprova si té almenys 8 caràcters.")
print("Mostra 'Contrasenya vàlida' o 'Contrasenya no vàlida'.")


password = input("Introdueix la contrasenya: ")
if len(password) >= 8:
    print("Contrasenya vàlida")
else:
    print("Contrasenya no vàlida")
