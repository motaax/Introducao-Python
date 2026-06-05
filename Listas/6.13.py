T = [ -10, -8, 0, 1, 2, 5, -2, -4]

max = T[0]
min = T[-1]

for e in T:
    if e > max:
        max = e
print(f"A maior temperatura e: {max}")

for e in T:
    if e < min:
        min = e
print(f"A menor temperatura e: {min}")

media = (max + min) / 2
print(f"A temperatura media e : {media}")