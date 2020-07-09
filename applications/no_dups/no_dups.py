def no_dups(s):
    # Your code here

    """
    # create a non_dups list
    non_dups = []
    
    for i in no_dups:
        if i not in no_dups:
            no_dups.append(i)
    return no_dups
    
    # input a string
    str_word = s.lower().isspace()
    for s in str_word:
        if s  == '':
            # return an empty string
            return ''
    """
    # create a dict
    dict = {}
    # input a string of letters
    letters = s.split()
    for letter in letters:
        if letter not in dict:
            dict[letter] = letter
    return ' '.join(dict.keys())

        
        
            

            
    
        
        




if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))