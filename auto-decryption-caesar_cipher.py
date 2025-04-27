# Auto-Dekoder - Szyfr Cezara

# Jest to rodzaj szyfru podstawieniowego, w którym każda litera tekstu jawnego (niezaszyfrowanego) zastępowana jest inną,
# oddaloną od niej o stałą liczbę pozycji w alfabecie, literą, przy czym kierunek zamiany musi być zachowany.
# Ta metoda wykorzystuje analizę częstotliwości występowania liter. W języku angielskim niektóre litery są bardzo powszechne (jak E), a niektóre bardzo rzadkie (jak J).
# Oto lista częstotliwości, oparta na liczeniu wystąpień w dużym tekście.
# Wartości są przedstwione po kolei alfabetycznie czyli dla a = 0.0817, dla b = 0.0149, dla c = 0.0278 itd.

letterGoodness = [
    0.0817, 0.0149, 0.0278, 0.0425, 0.127, 0.0223, 0.0202, 0.0609, 0.0697, 0.0015, 0.0077, 0.0402, 0.0241,
    0.0675, 0.0751, 0.0193, 0.0009, 0.0599, 0.0633, 0.0906, 0.0276, 0.0098, 0.0236, 0.0015, 0.0197, 0.0007
    ]

# Na przykład częstotliwość występowania litery L wynosi 0,0402=4,02%, co oznacza, że ​​w przeciętnym tekście angielskim 4,02% liter to L.

def goodness(text):
    list_of_sum = []
    S = 0
    while S != 24:
        new_text = ""
        count_goodness = 0
        for char in text:
            if char == " ":
                new_text += char
            elif ord(char) - S < 65:
                char = chr(ord(char) - S +26)
                new_text += char
            else:
                char = chr(ord(char) - S)
                new_text += char

        for char in new_text:
            if char.isalpha():
                i = ord(char) - 65
                count_goodness += letterGoodness[i]
        list_of_sum.append(count_goodness)
        S += 1
    maximum = max(list_of_sum)
    i = list_of_sum.index(maximum)

    S = i
    new_text = ""
    for char in text:
        if char == " ":
            new_text += char
        elif ord(char) - S < 65:
            char = chr(ord(char) - S + 26)
            new_text += char
        else:
            char = chr(ord(char) - S)
            new_text += char
    return new_text

while True:
    print(goodness(input("Napisz zakodowaną wiadomosc np.: 'LQKP OG CV GKIJV DA VJG BQQ': ")))