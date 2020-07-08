def word_count(s):
    # Your code here
    """Hello, my cat. And my cat doesn't say "hello" back."""
    word_dict = {}
    s = s.lower().split()
    for word in s:
        if word not in word_dict:
            word_dict[word] = 1
        word_dict[word] += 1
    return word_dict

   


    """
    for word in s:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] +=1
    return word_dict
print(word_count("Hello"))
    """


"""
    counts = dict()
    words = s.split()

    for words in s:
        if words.split():
            continue
        words = words.lower()

        if words not in counts:
            counts[words] = 1
        else:
            counts[words] += 1
    return counts
    """

"""
    for word in words:
        if words in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
# print(word_count("Hello"))
    """




if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))