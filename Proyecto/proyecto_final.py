
# For this project, you'll create a "word cloud" from a text by writing a script. 
#  This script needs to process the text, remove punctuation, ignore case and words that do not contain all alphabets, 
# count the frequencies, and ignore uninteresting or irrelevant words.  A dictionary is the output of the `calculate_frequencies` function. 
#  The `wordcloud` module will then generate the image from your dictionary.

import wordcloud
import numpy
from matplotlib import pyplot as plt

file_contents = open('pedroparamo.txt',mode='r',encoding='utf-8').read()
  
#funcion donde se le borrara todas las puntuaciones o palabra que no nos interesan
def calcular_frecuencia(file_contents):
    #lista de palabras que no nos intereza y puntuaciones
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an",
     "as", "i", "me", "my","we", "our", "ours", "you",
     "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", 
         "their", "what", "which", "who", "whom", "this",
      "that", "am", "are", "was", "were", "be", "been", "being",     "have", "has",
       "had", "do", "does", "did", "but", "at", "by", "with", 
      "from", "here", "when", "where", "how",     "all", "any", "both", "each", "few",
       "more", "some", "such", "no", "nor", "too", "very", 
      "can", "will", "just","tenia","hacia","todos","cualquiera","es","tiene","ser","quien",
      "esto","nuestro","el","ella","por","que","en","la","al","lo",
      "los","las","sus","se","con","una","le","del","su","como","un","eso","era","y","yo","con",
      "para","tu","de","mi","si","ya","nos","pero","nos","te","qué",
      "como","ese"]
    
   
    word_no_Spaces = file_contents.strip()
    wordLower = word_no_Spaces.lower()
    wordList = wordLower.split()
    clean_list = [word for word in wordList if word.isalpha() and word not in uninteresting_words]
    freq_dictionary = {}
    for items in clean_list:
        freq_dictionary[items] = clean_list.count(items)
    
    
    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(freq_dictionary)
    return cloud.to_array()

# Mostrar Imagen

myimage = calcular_frecuencia(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()

#tambien cuenta como el taller 3.5
