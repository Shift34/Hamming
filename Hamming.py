def count_check_digits(text: str):
    k = 2
    while True:
        if 2 ** k >= k + len(text) + 1:
            return k
        k += 1


def checking_check_bits(list_number):
    n = 0
    while 2 ** n < len(list_number):
        n1 = 2 ** n
        m = n1 - 1
        while m < len(list_number):
            if (m + n1) > len(list_number):
                for i in range(m, len(list_number)):
                    list_number[n1 - 1] += list_number[i]
            else:
                for i in range(m, m + n1):
                    list_number[n1 - 1] += list_number[i]
            m += 2 ** (n + 1)
        list_number[n1 - 1] = list_number[n1 - 1] % 2
        n += 1
    return list_number


def hamming_construction(text: str):
    count = count_check_digits(text)
    n = 0
    count1 = 0
    list_number = []
    for i in range(len(text) + count):
        if (2 ** n) - 1 == i:
            list_number.append(0)
            n += 1
        else:
            list_number.append(int(text[count1]))
            count1 += 1
    list_number = checking_check_bits(list_number)
    return ''.join(map(str, list_number))


def hamming_bug_fix(text: list):
    list_number = list(text)
    n = 0
    for i in range(len(list_number)):
        if (2 ** n) - 1 == i:
            list_number[i] = 0
            n += 1
        else:
            list_number[i] = int(list_number[i])
    list_number = checking_check_bits(list_number)
    for i in range(len(text)):
        text[i] = int(text[i])
    n = 0
    count = 0
    while 2 ** n < len(list_number):
        n1 = 2 ** n
        if list_number[n1 - 1] != text[n1 - 1]:
            if not n:
                pass
            else:
                count += 2 ** n
        n += 1
    text[count] = (text[count] + 1) % 2
    return ''.join(map(str, text))


input = open("InputHamming.txt", 'r', encoding="utf-8")
text = input.read()
input.close()

input = open("OutputHamming.txt", "w", encoding="utf-8")
text = input.write(hamming_construction(text))
input.close()

input = open("InputHammingBug.txt", 'r', encoding="utf-8")
text = list(input.read())
input.close()

input = open("OutputHammingBug.txt", "w", encoding="utf-8")
text = input.write(hamming_bug_fix(text))
input.close()
