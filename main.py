# zadanie 1
a = 'Matematyka'
a1 = 'Informatyka'
b = 1
b2 = 10
c = 10, 1
c3 = 5, 55
print('zmienna string', a, a1)
print('zmienna int', b, b2)
print('zmienna float', c, c3)

# zadanie 2
a = 1
b = 2
c = 3
dodawanie = a + b
odejmowanie = c - a
potegowanie = c ** b
dzielenie = c / a
dzielenie_calkowite = c // b
mnozenie = b * c
print('1 + 2 =% d' % (dodawanie))
print('3 - 1 =% d' % (odejmowanie))
print('3 potega 2 =% d' % (potegowanie))
print('dzielenie 3 / 1 =% d' % (dzielenie))
print('dzielenie calkowite 3 / 2 =% d' % (dzielenie_calkowite))
print('mnozenie 2 * 3 =% d' % (mnozenie))

# zadanie 3
a = 10
b = 3
a+= b
print(a)
b-= a
print(b)
a*= b
print(a)
a/= b
print(a)
b**= a
print(b)
a%= b
print(a)

# zadanie 4
from math import *
zm = e
liczba1 = pow(zm, 10)
print('e ^ 10 =', liczba1)
liczba2 = pow(log(5 + pow(sin(8), 2)), 1 / 6)
print('pow (ln (5 + pow (sin (8), 2)), 1/6) =', liczba2)

a = 3,55
liczba3 = math.floor(a)
print('⌊3,55⌋ =', math.floor(3,55))
b = 4,80
liczba4 = math.ceil(b)
print('⌈4,80⌉ =', liczba4)

zadanie 5
Imie = 'MACIEJ'
Nazwisko = 'SOBIECKI'
print(Imie . capitalize(), Nazwisko . capitalize())

# zadanie 6
Piosenka = 'sia la lala'
Ile = Piosenka .count('la')
print('"la"', Ile, 'razy')

# zadanie 7
Tekst = 'football'
print('Pierwszy znak ', Tekst[2])
print('Ostatni znak ', Tekst[-1])

# zadanie 8
Piosenka = 'sia la lala'
Podzial = Piosenka . split()
print(Podzial)

# zadanie 9
a = "morsowanie"
b = 25.52
print ('Ulubione zajecie to %s' %(a))
print('ulubiona liczba to %f' %(b))
