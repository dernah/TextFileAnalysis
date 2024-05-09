import matplotlib.pyplot as plt
import re
import string
import os
#f = "Frankenstein.txt"

wordsList = {}

while True:

    f = input("Enter a file name: ").strip()

    if not f.lower().endswith('.txt'):
        f += '.txt'

    if os.path.exists(f):
        break
    else:
        print(f"Error: the file '{f}' does not exist.")

base_name = os.path.splitext(os.path.basename(f))[0]

punct = list(string.punctuation)
punct.pop(punct.index("'"))
with open(f, 'r') as file:
    for line in file:
        for letter in line:
            for p in punct:
                if letter == p:
                    if letter in wordsList.keys():
                        wordsList[letter] += 1
                    else:
                        wordsList[letter] = 1
                    line.replace(letter," ")
            words = line.split(" ")
        for word in words:
            word = re.sub(r'[^\w\']', '', word)
            if len(word) != 0:
                if word in wordsList.keys():
                    wordsList[word] += 1
                else:
                    wordsList[word] = 1

sortedList = {i: j for i, j in sorted(wordsList.items(), key=lambda item: item[1], reverse=True)}

i = 0
words = list(sortedList.keys())[:50]
frequency = [sortedList[words[i]] for i in range(50)]
fig, ax = plt.subplots(figsize=(10, 10))
plt.bar(range(len(words)), frequency, align='center', edgecolor = 'black')
plt.xticks(range(len(words)), words, rotation=90)
plt.xlabel("Words", fontsize = 14)
plt.ylabel("Word Frequency", fontsize = 14)
plt.title(f"Word Frequency in {base_name}.txt", fontsize = 16)

most_frequent_word = list(sortedList.keys())[0]
most_frequent_count = sortedList[most_frequent_word]

height_adjustment = 0.03 * most_frequent_count

plt.text(-3,most_frequent_count + height_adjustment,f"Most frequent word is: {most_frequent_word}", fontsize=12)

for word in ax.patches:
    text = str(word.get_height())
    text_x = word.get_x() + word.get_width() / 2
    text_y = word.get_height() + 0.07 * word.get_height()
    ax.text(text_x, text_y, text, ha='center', va='bottom', rotation='vertical')
plt.show()

words = list(wordsList.keys())
words = sorted(words, key=len, reverse=True)
longWords = words[:50]
longWords = sorted(longWords, key=len)
frequency = [wordsList[longWords[i]] for i in range(50)]

longest_word = longWords[-1]
longest_word_count = wordsList[longest_word]

height_adjustment = 0.20 * longest_word_count

fig, ax = plt.subplots(figsize=(10, 10))
plt.bar(range(len(longWords)), frequency, edgecolor = 'black')
plt.xticks(range(len(longWords)), longWords, rotation = 90)
plt.xlabel("Words", fontsize = 14)
plt.ylabel("Word Frequency", fontsize = 14)
plt.title(f"Long words in {base_name}.txt", fontsize = 16)
plt.text(len(longWords)-1, longest_word_count + height_adjustment, f"Longest word: {longest_word}", fontsize=12)

for word in ax.patches:
    text = str(word.get_height())
    text_x = word.get_x() + word.get_width() / 2
    text_y = word.get_height() + 0.07 * word.get_height()
    ax.text(text_x, text_y, text, ha='center', va='bottom', rotation='horizontal')
plt.tight_layout()
plt.show()
