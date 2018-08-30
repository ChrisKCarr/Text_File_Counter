
# coding: utf-8

# In[6]:


import operator

def rank_words(f):
    """
    Takes in a file, then ranks all the words by number of use.
    Returns top 20 most used words
    """
    word_dict = {}
    words = []
    for line in f:
        list_of_words = line.split()
        for w in list_of_words:
            words.append(w.lower())
            
    for word in words:
        if word_dict.has_key(word):
            word_dict[word] += 1
        else:
            word_dict[word] = 1
            
    return sorted(word_dict.iteritems(), reverse=True, key=operator.itemgetter(1))
 

def main():
    f = open('alice.txt', 'rU')
    
    ranked_words_list = rank_words(f)
    
    f.close()
    
    for w in list(ranked_words_list[:20]):
        print (w[0],'---',w[1])

