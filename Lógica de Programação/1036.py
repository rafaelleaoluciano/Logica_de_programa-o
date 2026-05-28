A, B, C = map(float, input().split())
import math

#calcular delta
delta = (B**2) - (4*A*C)

if A<0:
    print("Impossível calcular")
else:
    r1 = (-B+ math.sqrt (delta))/(2*A)
    r2 = (-B- math.sqrt (delta))/(2*A)

print(f"R1 = {r1:.5f}")
print(f"R2 = {r2:.5f}")