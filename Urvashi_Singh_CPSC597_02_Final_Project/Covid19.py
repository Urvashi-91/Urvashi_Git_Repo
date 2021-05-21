
from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
from tkinter.filedialog import askopenfilename
import pandas as pd
from string import punctuation
from nltk.corpus import stopwords
import nltk
from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer
from gensim import corpora
import pickle
import gensim
import pyLDAvis.gensim
import matplotlib.pyplot as plt
from gensim.models.coherencemodel import CoherenceModel
from gensim.corpora.dictionary import Dictionary
from collections import defaultdict

'''
Designing Main Display Screen
'''
main = tkinter.Tk()
main.title("Quantifying COVID-19 Content in the Online Health Opinion War Using Machine Learning")
main.geometry("1300x1200")

'''
Declaring global variables that will be used throughout the project
'''
global filename
en_stop = set(nltk.corpus.stopwords.words('english'))
global text_data
global dictionary
global corpus
global ldamodel
global pro,anti

'''
Function to clean data using Gensim and NLTK
'''
def cleandata(doc):
    tokens = doc.split()
    table = str.maketrans('', '', punctuation)
    tokens = [w.translate(table) for w in tokens]
    tokens = [word for word in tokens if word.isalpha()]
    stop_words = set(stopwords.words('english'))
    tokens = [w for w in tokens if not w in stop_words]
    tokens = [word for word in tokens if len(word) > 1]
    tokens = ' '.join(tokens)
    #print(tokens)
    return tokens

'''
Lemmatize data
'''
def lemmatize_data(word):
    lemma = wn.morphy(word)
    if lemma is None:
        return word
    else:
        return lemma

def lemmatize_data2(word):
    return WordNetLemmatizer().lemmatize(word)


'''
LDA Extract Topics from the pre-processed data
'''
def lda_data_modelling(text):
    tokens = text.split(" ")
    tokens = [token for token in tokens if len(token) > 4]
    tokens = [token for token in tokens if token not in en_stop]
    tokens = [lemmatize_data(token) for token in tokens]
    return tokens

'''
Upload Facebook Posts from your computer
'''
def upload(): #function to upload tweeter profile
    global filename
    filename = filedialog.askopenfilename(initialdir="FacebookPost")
    text.delete('1.0', END)
    text.insert(END,filename+" loaded\n");

'''
Further clean data
'''
def processDataset():
    text.delete('1.0', END)
    global text_data
    text_data = []
    dataset = pd.read_csv(filename,encoding="ISO-8859-1")
    for i in range(len(dataset)):
        msg = dataset.get_value(i, 'Posts')
        clean = cleandata(msg.strip('\n').strip().lower())
        clean = lda_data_modelling(clean)
        text_data.append(clean)
    text.insert(END,'Posts after processing\n\n')
    text.insert(END,str(text_data)+"\n\n")
                
'''
LDA data modelling
'''
def LDA():
    global dictionary
    global corpus
    global ldamodel
    text.delete('1.0', END)
    dictionary = corpora.Dictionary(text_data)
    corpus = [dictionary.doc2bow(text) for text in text_data]
    pickle.dump(corpus, open('corpus.pkl', 'wb'))
    dictionary.save('dictionary.gensim')
    NUM_TOPICS = 30
    ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics = NUM_TOPICS, id2word=dictionary, passes=15)
    ldamodel.save('model5.gensim')
    topics = ldamodel.print_topics(num_words=6)
    text.insert(END,'LDA Extracted Topics\n\n')
    for topic in topics:
        text.insert(END,str(topic)+"\n")

'''
View LDA extracted topics
'''
def viewTopics():
    global pro,anti
    anti_topics = ['shot','burder','protest','avoid','flu','fake','stop','afraid','never','test','spread','poison']
    pro_topics = ['maskwearing','protect','healthcare','trust','ailment','mask','wash','distancing','distance','soap','prevent','mandatory']
    pro =  {}
    anti = {}
    combine = {}
    for i in range(len(text_data)):
        data = text_data[i]
        for j in range(len(data)):
            if data[j] in anti_topics:
                if data[j] in anti:
                    anti[data[j]] = anti.get(data[j]) + 1
                else:
                    anti[data[j]] = 1
            if data[j] in pro_topics:
                if data[j] in pro:
                    pro[data[j]] = pro.get(data[j]) + 1
                else:
                    pro[data[j]] = 1        
    text.delete('1.0', END)
    text.insert(END,'Pro vaccines topics details\n\n')
    text.insert(END,str(pro)+"\n\n")
    text.insert(END,'Pro vaccines topics details\n\n')
    text.insert(END,str(anti))

'''
Plot Coherence Score graph
'''
def scoreGraph():
    pro_graph = []
    anti_graph = []
    for key in pro: 
        pro_graph.append(pro[key])
    for key in anti: 
        anti_graph.append(anti[key])
    plt.figure(figsize=(10,6))
    plt.grid(True)
    plt.xlabel('Total Topics')
    plt.ylabel('Coherence scores')
    plt.plot(pro_graph, 'ro-', color = 'indigo')
    plt.plot(anti_graph, 'ro-', color = 'blue')
    plt.legend(['Pro-Vax', 'Anti-Vax'], loc='upper left')
    plt.title('Coherence Topic Scores Graph')
    plt.show()    
        
'''
Plot pyLDAvis graph
'''
def graph():
    lda_display = pyLDAvis.gensim.prepare(ldamodel, corpus, dictionary, mds='mmds')
    #pyLDAvis.enable_notebook(local=True)
    pyLDAvis.show(lda_display)

'''
Front-end of our system build using TKINTER Python toolkit
Every button respnods to a function specified above.
'''
font = ('times', 16, 'bold')
title = Label(main, text='Quantifying COVID-19 Content in the Online Health Opinion War Using Machine Learning')
title.config(bg='firebrick4', fg='dodger blue')  #firebrick text and dodger blue label
title.config(font=font)     #font specified before
title.config(height=3, width=120)     #initial size lines, chars
title.place(x=0,y=5) #place title at given pos

font1 = ('times', 12, 'bold')
text=Text(main,height=20,width=150)
scroll=Scrollbar(text)
text.configure(yscrollcommand=scroll.set)
text.place(x=50,y=120)
text.config(font=font1)


font1 = ('times', 14, 'bold')
uploadButton = Button(main, text="Upload Facebook Posts Dataset", command=upload, bg='#ffb3fe')
uploadButton.place(x=50,y=550)
uploadButton.config(font=font1)

processButton = Button(main, text="Process Dataset using Gensim & NLTK", command=processDataset, bg='#ffb3fe')
processButton.place(x=350,y=550)
processButton.config(font=font1) 

LDAforest = Button(main, text="Run LDA Topic Modelling to Extract Topics", command=LDA, bg='#ffb3fe')
LDAforest.place(x=750,y=550)
LDAforest.config(font=font1) 

topicButton = Button(main, text="View Pro & Anti Vaccines Topics", command=viewTopics, bg='#ffb3fe')
topicButton.place(x=50,y=600)
topicButton.config(font=font1) 

vaccine = Button(main, text="Pro & Anti Vaccine Graph", command=scoreGraph, bg='#ffb3fe')
vaccine.place(x=350,y=600)
vaccine.config(font=font1) 

graph = Button(main, text="pyLDAvis Topic Visualization", command=graph, bg='#ffb3fe')
graph.place(x=750,y=600)
graph.config(font=font1) 

main.config(bg='LightSalmon3')
main.mainloop()
