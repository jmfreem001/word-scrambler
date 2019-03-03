def get_english_words(file):
    """Pulls txt file with a list"""
    doc = open(file,'r')
    ## TODO: Refactor this function to use something other than split and then
    # removing the blanks and creating a new list with join. Should be a more elegant solution.
    list = [word.split("\n") for word in doc]
    clean_list = []
    for item in list:
        item.pop()
        clean_list.append(''.join(item))
    return clean_list

words = get_english_words('words_alpha.txt')

print(words[:10])

if words[47251] == ['car']:
    print("True")
else:
    print("False")
