pensje = [4200,5100,4800,4500,4700,5300,4900,35000,4400]
print(f"Poczatkowa pensja: {pensje}")

n = len(pensje)
suma = sum(pensje)
srednia=suma/n
mediana= pensje[n // 2]
rozstep= max(pensje) - min(pensje)
licznik = 0
print(f"Liczba pensji w liscie wynosi: {n}")
for i in range(n):
    print(i)
    for j in range(n - 1 - i):
        if pensje[j] > pensje[j+1]:
            pensje[j], pensje[j+1] = pensje[j+1], pensje[j]
for pensja in pensje:
    if pensja < srednia:
        licznik +=1

    
    
    print(f"Przejscie {i+1}: {pensje}")


print(f"\nPosortowana lista: {pensje}")
print(f"Najnizsza pensja: {pensje[0]}")
print(f"Najwieksza pensja: {pensje[-1]}")
print(f"Srednia: {srednia}")
print(f"Mediana: {mediana}")
print(f"Minimum: {min(pensje)}")
print(f"Maksium: {max(pensje)}")
print(f"Rozstep: {rozstep}")
print(f"Liczba pracowników zarabiających mniej niż średnia: {licznik}")
print(f"Srednia bez prezesa {sum(pensje) - max(pensje) / (n-1)}")




    
