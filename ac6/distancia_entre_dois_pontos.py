p1 = map(float, input().split())
p2 = map(float, input().split())

x1, y1 = p1
x2, y2 = p2

distancia = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5
print("%0.4f" %distancia)