import string
missing_items = []
def missing_letter(givenletter):
    alpha = string.ascii_lowercase
    start = alpha.index(givenletter[0])
    for letter in alpha[start:]:
        if letter not in givenletter:
             missing_items.append(letter)
             return missing_items
    return f"No missing letter in the sequence"
print(missing_letter("klopq"))
print(missing_letter("xyz"))
