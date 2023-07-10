"""
Next, copy in your strip_punctuation function and define a function called get_pos
which takes one parameter, a string which represents one or more sentences,
and calculates how many words in the string are considered positive words.
Use the list: positive_words to determine what words will count as positive.
The function should return a positive integer - how many occurrences there are of positive words in the text.
Note that all of the words in positive_words are lower cased,
so you’ll need to convert all the words in the input string to lower case as well.

Similarly, define a function called get_neg
which takes one parameter, a string which represents one or more sentences,
and calculates how many words in the string are considered negative words.
Use the list, negative_words to determine what words will count as negative.
The function should return a positive integer - how many occurrences there are of negative words in the text.
Note that all of the words in negative_words are lower cased,
so you’ll need to convert all the words in the input string to lower case as well.
"""

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']


def strip_punctuation(word):
    for char in punctuation_chars:
        if char in word:
            word = word.replace(char, '')
    return word


# list of positive words to use
positive_words = []
with open("RefFiles/positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


def get_pos(sentence):
    pos_count = 0
    for word in sentence.split(' '):
        if strip_punctuation(word.lower()) in positive_words:
            pos_count += 1
    return pos_count


negative_words = []
with open("RefFiles/negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())


def get_neg(sentence):
    neg_count = 0
    for word in sentence.split(' '):
        if strip_punctuation(word.lower()) in negative_words:
            neg_count += 1
    return neg_count

