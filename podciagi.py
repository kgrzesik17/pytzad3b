def substrings(text:str, n:int):
    """
    This generator yields all the substrings of a user specified length.

    Input:
    text - text user wants to analyze
    n - substring length

    Output:
    yield - substrings of a user specified length
    """

    text = text.split()

    for i in text:
        if len(i) == n:
            yield i

words = substrings("tom sam zbudowal dom", 3)

for word in words:
    print(word)