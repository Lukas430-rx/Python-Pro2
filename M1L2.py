import random

generador = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

longitud = int(input("Elige la longitud de tu contrseña:"))
contraseña = ""



for i in range(longitud):
    contraseña += random.choice(generador)

print("Tu contraseña es esta:", contraseña)
