"""Given a set of strings, find the longest common prefix."""
def Lon_Com_Prefix(words):
    print(words)
    if not words:
        return ''
    prefix = words[0]
    for word in words:
        if len(prefix) > len(word):
            prefix, word = word, prefix

        while len(prefix) > 0:
            if word[:len(prefix)] == prefix:
                break
            else:
                prefix = prefix[:-1]
    return prefix

if __name__ == '__main__':
    word_list = input("Enter words seprated by ' ' : ").split()
    result = Lon_Com_Prefix(word_list)
    print(result)
