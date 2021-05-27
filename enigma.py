from lib import Rotor


def cipher(number, i):
    if (ord(i) + number) > 122:
        return chr((ord(i) - 26) + number)
    else:
        return chr(ord(i) + number)


def cipher_m(number, i):
    if (ord(i) - number) < 97:
        return chr((ord(i) + 26) - number)
    else:
        return chr(ord(i) - number)


def enigma_code(rotor, text):
    rotor3 = rotor[0]
    rotor2 = rotor[1]
    rotor1 = rotor[2]
    letters = list()
    for i in text:
        if i == ' ':
            letters.append(i)
        else:
            rotor1 = cipher(1, rotor1)
            rotor2 = cipher(1, rotor2)

            letter1 = Rotor[cipher(ord(rotor1.lower()) - 97, i.lower()).upper()][0]

            num = cipher_m(ord(rotor1.lower()) - 97, rotor2.lower())
            letter2 = Rotor[cipher(ord(num) - 97, letter1.lower()).upper()][1]

            num = cipher_m(ord(rotor2.lower()) - 97, rotor3.lower())
            letter3 = Rotor[cipher(ord(num) - 97, letter2.lower()).upper()][2]

            letter4 = Rotor[cipher_m(ord(rotor3.lower()) - 97, letter3.lower()).upper()][3]

            letter = cipher(ord(rotor3.lower()) - 97, letter4.lower()).upper()
            for j in Rotor:
                if Rotor[j][2] == letter:
                    letter5 = j
                    break

            num = cipher_m(ord(rotor2.lower()) - 97, rotor3.lower())
            letter6 = cipher_m(ord(num.lower()) - 97, letter5.lower()).upper()
            for j in Rotor:
                if Rotor[j][1] == letter6:
                    letter6 = j
                    break

            num = cipher_m(ord(rotor1.lower()) - 97, rotor2.lower())
            letter7 = cipher_m(ord(num.lower()) - 97, letter6.lower()).upper()
            for j in Rotor:
                if Rotor[j][0] == letter7:
                    letter7 = j
                    break

            letter8 = cipher_m(ord(rotor1.lower()) - 97, letter7.lower()).upper()
            for j in Rotor:
                if Rotor[j] == letter8:
                    letter8 = j
                    break

            letters.append(letter8)
    return ''.join(letters)
