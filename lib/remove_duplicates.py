def remove_duplicates(sequence):
    if type(sequence) == list:
        return list(set(sequence))
    elif type(sequence) == tuple:
        return tuple(set(sequence))
    
print(remove_duplicates((2, 3, 2, 4, 5, 3, 6, 7, 5)))