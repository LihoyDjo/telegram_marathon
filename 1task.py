def hamming_distance(string1, string2):
    number = 0
    for i in range(len(string1)):
        if string1[i] == string2[i]:
            continue
        else:
            number += 1
    return number

