"""
Finally, copy in your previous functions and write code that opens the file project_twitter_data.csv
which has the fake generated twitter data (the text of a tweet, the number of retweets of that tweet,
and the number of replies to that tweet).

Your task is to build a sentiment classifier, which will detect how positive or negative each tweet is.
Now, you will write code to create a csv file called resulting_data.csv,
which contains the Number of Retweets, Number of Replies,
Positive Score (which is how many happy words are in the tweet),
Negative Score (which is how many angry words are in the tweet),
and the Net Score (how positive or negative the text is overall) for each tweet.

The file should have those headers in that order.
You will upload the csv file to Excel or Google Sheets
and produce a graph of the Net Score vs Number of Retweets.
"""

# Punctuations to be ignored
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']


# Function copied from strip_punctuation.py
# Also the step 1!
def strip_punctuation(word):
    for char in punctuation_chars:
        if char in word:
            word = word.replace(char, '')
    return word


# lists of words to use
positive_words = []
with open("RefFiles/positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


# Copied from get_pos_and_neg_counts.py. Step 2
def get_pos(sentence):
    count = 0
    for word in sentence.split(' '):
        if strip_punctuation(word.lower()) in positive_words:
            count += 1
    return count


negative_words = []
with open("RefFiles/negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())


# Copied from get_pos_and_neg_counts.py. Step 3
def get_neg(sentence):
    count = 0
    for word in sentence.split(' '):
        if strip_punctuation(word.lower()) in negative_words:
            count += 1
    return count


# Step 4:
with open('RefFiles/project_twitter_data.csv', 'r') as csv_file_r:
    all_lines = csv_file_r.readlines()

with open('RefFiles/resulting_data.csv', 'w') as csv_file_w:
    header = 'Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score'
    csv_file_w.write(header)
    csv_file_w.write('\n')
    for line in all_lines[1:]:
        line = line.strip('\n')
        tweet_text = line.split(',')[0]
        retweet_count = line.split(',')[1]
        reply_count = line.split(',')[2]
        pos_count = get_pos(tweet_text)
        neg_count = get_neg(tweet_text)
        net_score = pos_count - neg_count
        csv_file_w.write('{},{},{},{},{}'.format(retweet_count, reply_count, pos_count, neg_count, net_score))
        csv_file_w.write('\n')
