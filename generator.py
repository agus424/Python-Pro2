import random
psw = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
say = int(input("Cuál es la longitud de la contraseña?"))
contraseña = ""
for i in range(say):
    contraseña += random.choice(psw)
print("Tu contraseña generada es: ",contraseña)
