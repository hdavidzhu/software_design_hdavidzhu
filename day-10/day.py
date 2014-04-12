import string, re

def get_words_from_book(filename):
    f = open(filename,'r')
    fulltext = f.read()

    # Remove the start and end extras.
    fulltext = fulltext[fulltext.index(" ***")+4:]
    fulltext = fulltext[0:fulltext.index("End of the Project Gutenberg EBook")]
    fulltext = fulltext.lower()
    new_fulltext = re.sub('[%s]' % re.escape(string.punctuation), '', fulltext)

    text_list = [word for word in new_fulltext.split()]
    print text_list

    f.close()


if __name__ == "__main__":
    get_words_from_book('pg30254.txt')