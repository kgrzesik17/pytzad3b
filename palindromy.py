def palindromes(text:str):
    """
    This function returns a list of all palindromes contained in specified text.

    Input:
    text - text user wants to analize

    Output:
    list - list of palindromes
    """

    text = text.strip()
    text += " "
    temp = ""
    words = []
    output = []

    for letter in text:
        if letter.isalnum():
            temp += letter

        else:
            words.append(temp)
            temp = ""

    for i in words:
        if i == i[::-1] and i != "":
            output.append(i)

    return output

print(palindromes('kaja ma kajak, banan i radar. adam łamał oko.'))