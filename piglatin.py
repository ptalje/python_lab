import re
pyg = 'ay'

print("Welcome to the Pig Latin translator 1.0")

original = input('Enter a word or sentence: ')
# create array of all words
multiple = re.findall(r"[\w']+", original)

# Translating a single word unless it isn't a word
def singleword(input):
    if input.isalpha():
        word = input.lower()
        first = word[0]
        new_word = word[1:len(word)] + first + pyg
        return new_word
    else:
        print('** Gnoringiay ordway ' + input + ' tiay siay Reekgay otay emay')
        return ''

# validating that we have entered something
def validate(input):
    if len(input) > 0:
        return True
    else:
        return False

if validate(original):
    result = ''
    for word in multiple:
         result += ' ' + singleword(word)
    print('In Pig Latin this is: ' + result[1:len(result)])
