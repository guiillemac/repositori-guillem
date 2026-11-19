###
# Exercicis - input()
# Practica l'entrada de dades i la conversió de tipus amb exemples de telecomunicacions.
###

# Exercici 1
# Demana el nom d'un tècnic i el nom de la xarxa que està instal·lant.
# Després, mostra un missatge amb aquesta informació.

nom_tecnic = input("Introdueix el nom del tècnic: ")
nom_xarxa = input("Introdueix el nom de la xarxa a instal·lar: ")

print(f"El tècnic {nom_tecnic} està instal·lant la xarxa '{nom_xarxa}'.\n")

# Exercici 2
# Demana la longitud d'un enllaç de fibra en quilòmetres i la velocitat de transmissió
# en Gbps. Mostra quants segons caldrien per transmetre 1 GB de dades.
# Suposa que 1 GB = 8 Gb i que la velocitat es manté constant.

longitud_km = float(input("Introdueix la longitud de l'enllaç de fibra (km): "))
velocitat_gbps = float(input("Introdueix la velocitat de transmissió (Gbps): "))
temps_segons = 8 / velocitat_gbps

print(f"Per a l'enllaç de {longitud_km} km a {velocitat_gbps} Gbps, es necessiten {temps_segons:.2f} segons per transmetre 1 GB.\n")

# Exercici 3
# Demana el nombre d'hores de feina i el preu per hora d'una instal·lació de xarxa.
# Demana també el preu del material.
# Mostra el cost total de la instal·lació.

hores_feina = float(input("Introdueix el nombre d'hores de feina: "))
preu_hora = float(input("Introdueix el preu per hora (€): "))
preu_material = float(input("Introdueix el cost del material (€): "))

cost_total = (hores_feina * preu_hora) + preu_material

print(f"El cost total de la instal·lació és de {cost_total:.2f} €.")