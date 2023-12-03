def word_frequency(sentence):
    word_dict = {char.lower():0 for char in sorted(set(sentence)) if char.isalpha()}
    
    for char in sentence:
        if char.isalpha():
            word_dict[char.lower()] += 1
        
    return word_dict
    
print(word_frequency("Accumulated???"))