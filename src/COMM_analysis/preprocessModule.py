'''
@Saleem
prerpocessing module for dangerous speech
'''

import sys
sys.dont_write_bytecode = True

#-----------------------------------------------------------------------------------------------
import helpModule
import re
import string

#-----------------------------------------------------------------------------------------------
exclude = set(string.punctuation)

#-----------------------------------------------------------------------------------------------


def unescapeHTML(s):
    # remove html escaped charcters
    s = s.replace("&lt;", "")
    s = s.replace("&gt;", "")
    s = s.replace("&amp;", "")
    return s


def quickSing(s):
    # naively remvoe plurals
    if s[-1] == 's':
        if not s[-2] == 'u':
            if not s[-2] == 's':
                return s[:-1]
    return s


def cleanUp(text):
    # remove deleted
    if text.strip() == '[deleted]':
        return False
    # remove hyperlinks
    text = re.sub(r'https?:\/\/.*[\r\n]*', '', text)
    # remove newline
    text = text.encode('UTF-8').replace("\n", " ")
    text = unescapeHTML(text)
    # remove punctuaitons
    text = ''.join(ch for ch in text if ch not in exclude).lower()
    # remove extra spaces
    text = " ".join(text.strip().split())
    # remove digits
    text = re.sub('[0-9]', '', text)
    # remove bots
    if text.startswith('This thread has been linked to from another place on reddit') or 'AutoModerator' in text:
        return False
    # remove stopwords
    text = ' '.join([x for x in text.split() if x.lower()
                     not in helpModule.stopwords])
    # remove non printable
    text = filter(lambda x: x in string.printable, text)
    # remove small words
    text = ' '.join([x for x in text.split() if len(x) > 3])
    # remove empty comments
    if text == '':
        return False
    # remove plurals
    text = ' '.join([quickSing(x) for x in text.split()])
    return text.lower()
