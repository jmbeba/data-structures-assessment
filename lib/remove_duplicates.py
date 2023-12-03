def remove_duplicates(sequence):
    if type(sequence) == list:
        new_list = []
        for num in sequence:
            if num not in new_list:
                new_list.append(num)
        return new_list
                
    elif type(sequence) == tuple:
        new_list = []
        for num in sequence:
            if num not in new_list:
                new_list.append(num)
        return tuple(new_list)
    
print(remove_duplicates((12, 2, 3, 2, 4, 5, 3, 6, 7, 5, 2,10)))