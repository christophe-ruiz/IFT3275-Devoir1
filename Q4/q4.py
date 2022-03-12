import re

cipher = []


# Filter given input in question 4
def sanitize():
    with open('input4.txt', 'r', encoding="utf-8") as rawfile:
        lines = [line.strip("\n") for line in rawfile if line != "\n"]
        with open('output4.txt', 'w', encoding="utf-8") as o:
            o.write("".join(lines))


def str_to_binary(raw):
    res = ""
    for c in raw:
        res += format(ord(c), '#010b')[2:]
    n = int(res, 2)
    return n


def binary_to_str(raw):
    res = ""
    for i in range(0, len(raw), 8):
        res += chr(int(raw[i:i+8], 2))
    return res


def each_cons(xs, n):
    return zip(*(xs[i:] for i in range(n)))


if __name__ == '__main__':
    regex = re.compile("[a-zA-Z'éùûèàÀÉÊêëË\-\.,!\?;:\ ]*")
    with open('output4.txt', 'r', encoding='utf-8') as f:
        cipher = f.readline()
    print(cipher)

    xor = int(cipher[:len(cipher)//2], 2) ^ int(cipher[len(cipher)//2:], 2)
    xor = "0" + bin(xor)[2:]
    print(xor)
    while True:
        word = input("Choisissez le mot: ")
        print(f'word: {word}')
        longueur = 8 * len(word)
        print(f'longueur {longueur}')
        word = str_to_binary(word)
        print(f'binary word: {word}')

        for i in range(len(xor)-longueur):
            # print(cipher[i:i+longueur])
            res = int(cipher[i:i+longueur], 2) ^ word
            strres = format(res, f'0{longueur}b')
            clearword = binary_to_str(strres)
            if regex.fullmatch(clearword):
                print(clearword)
