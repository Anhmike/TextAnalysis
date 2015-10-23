# main.py
# Small program that aims at helping humans doing the analysis of a given text.

# The program prompts the user to enter the path to the directory where a given .txt UTF-8
# encoded text file is located.
# Please note that the user must enter the full path.

# The program asks the name of the file. Please include the extension.

# Afterwards, the program process the text file using the libraries re and nltk

# The program prompts the user to split the text in a given number of parts. The program
# will then proceed in looking up the context using the nltk library of a given list of
# words. The user can be helped in choosing these words if she chooses to look at a list
# of the 10 most frequent words present in the text.

# The program prints the context of the words and ends.

from __future__ import division

import nltk
import os
import nltk.corpus
from nltk.corpus import stopwords

import re
import nltk.text

def main():
    print '------------------ PROGRAM START ---------------------'
    print ' Please enter the PATH to the directory where the text file is located.'
    path = raw_input()
    print ' Please enter the name of the text file. The text file must be encoded in UTF-8.'
    nom = raw_input()
    dir = os.path.dirname(path)
    text_file = os.path.join(dir, nom)
    raw = open(text_file).read()
    
    text = process_text(raw)

    print 'In how many parts do you want to split the text?'
    n = int(raw_input())

    print 'Begin analysis...'
    raw_input("Press Enter to continue...")

    print 'Would you like to have help in finding the most frequent words? Type 1 for yes'
    answer = int(raw_input())

    if answer == 1:
        fdist = nltk.FreqDist(text)
        print 'Here is the list of the ten most common words:'
        print fdist.most_common(10)

    most_common_words(text = text, n = n)

    print 'Thank you for using our program! :)'

def process_text(raw):

    text = re.split(r'\W+', raw)
    punct = [' ','!','?',';',':',',','.',]
    clean_text = [word for word in text if word not in punct]
    lower_text = [word.lower() for word in clean_text]
    stopword = stopwords.words("english")

    text = [word for word in lower_text if word not in stopword]
    return text;

def most_common_words(text,n):

    stop = len(text)
    stop = stop/n
    stop = int(stop)

    print 'How many words do you want to look for their context?'
    number_word = int(raw_input())
    lookout_list = list()

    for i in range(1,number_word+1):
        print "Please enter the next word to look for"
        lookout_list.append(raw_input())

    for i in range(0,n):
        part_text = nltk.Text(word for word in text[((i*1)+1):i*stop])

        print "Starting the next part analysis..."
        enter = raw_input("Press Enter to continue.")
        
        for j in range(0,number_word):
            print "Looking for context of word", lookout_list[j]
            context = nltk.text.ContextIndex([word.lower() for word in part_text])
            print 'The context is: '
            print context.similar_words(lookout_list[j])  

    print 'The analysis is over!'         

main()




