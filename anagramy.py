def get_words(file_name:str):
    """
    This function lets you load words from a file.

    Input:
    file_name - name of the file that user wants to open

    Output:
    list - list of words
    """
    file = open(file_name, 'r') # the file has to be encoded with "windows 1250" to work for Polish letters.
    
    output = [x.strip().lower() for x in file]

    return output

word_list = get_words('slowa.txt')

def anagrams(word_list, word:str):
    """
    This function generates words in the list that are anagrams to the user specified word.

    Input:
    word_list - list of words you want to analyze.
    word - word you want to check for possible anagrams.

    Output:
    yield - anagrams.
    
    """
    letters = [x for x in word]
    letters.sort()

    temp = []

    for i in word_list:
        for j in i:
            temp.append(j)

        temp.sort()

        if letters == temp:
            yield i

        temp = []

        if temp == letters:
            yield i

test = anagrams(word_list, 'spie')

for word in test:
    print(word)