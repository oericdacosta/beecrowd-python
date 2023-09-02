import math

p1 = list(map(float, input().split(' ')))
p2 = list(map(float, input().split(' ')))

distancia = math.sqrt(math.pow(p2[0] - p1[0], 2) + math.pow(p2[1] - p1[1], 2))

print("%.4f" % distancia)
