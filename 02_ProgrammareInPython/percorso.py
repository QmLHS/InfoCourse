import math

haltFlag = 1
lunghezza = 0
print("inserire le coordinate delle citta'")
print("un valore negativo termina l'inserimento")
xOld = float(input("ascissa  "))
yOld = float(input("ordinata "))
while haltFlag > 0:
    x = float(input("ascissa  "))
    y = float(input("ordinata "))
    if x < 0 or y < 0:
        haltFlag = 0
    else:
        deltaX = x - xOld
        deltaY = y - yOld
        lunghezza += math.sqrt(deltaX**2 + deltaY**2)
        xOld = x
        yOld = y
print("la lunghezza del percorso e'", lunghezza)
