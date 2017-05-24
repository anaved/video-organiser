'''
Created on Aug 20, 2016

@author: Naved
'''
import os
from guessit import guessit
from imdbpie import Imdb
# imdb = Imdb()
imdb = Imdb(anonymize=True) # to proxy requests
if __name__ == '__main__':
    #----guessit format
    count = 1
    # traverse root directory, and list directories as dirs and files as files
    for root, dirs, files in os.walk("F:/Torrent"):
#         path = root.split('/')
#         print((len(path) - 1) * '---', os.path.basename(root))
        for f in files:
            guess = guessit(f)
            if 'video' in guess.get('mimetype',''):
                print  root,f,guess
                title = guess.get('title')
                if title:
                    print imdb.search_for_title(title)
        count = count +1
#         if count ==10:
#             break

#     print cinephile.get_movies_set("G:/Personal/Motion Picture")       