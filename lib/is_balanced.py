def is_balanced(expression):
    openings = []
    match_brackets = {
        ')': '(',
        ']': '[',
        '}': '{'
        }

    #Loop over the expression
    for char in expression:
        #If the character matches an opening bracket, append it to the opening list
        if char in match_brackets.values():
            openings.append(char)
        #Else if the character matches a closing bracket, compare its opening bracket to the last index of the opening list
        elif char in match_brackets.keys():
            #If the comparison matches, remove the last index of the opening list
            if openings and match_brackets[char] == openings[-1]:         
                openings.pop()
            #Else return false
            else:
                return False

    return len(openings) == 0

print(is_balanced("([]{})"))
print(is_balanced("({[]})"))
print(is_balanced("([)]"))