import sys, os, re, csv, codecs, numpy as np, pandas as pd
import matplotlib.pyplot as plt
import pickle
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.layers import Dense, Input, LSTM, Embedding, Dropout, Activation
from keras.layers import Bidirectional, GlobalMaxPool1D
from keras.models import Model
from keras import initializers, regularizers, constraints, optimizers, layers

#
#train = pd.read_csv('train.csv')
#test = pd.read_csv('wikitok1000000.txt')
#train.isnull().any(),test.isnull().any()
#
#list_classes = ['target', 'severe_toxicity', 'obscene', 'identity_attack', 'insult', 'threat']
#y = train[list_classes].values
#list_sentences_train = train["comment_text"]
#list_sentences_test = test["0"]
#max_features = 20000
#
#
#tokenizer = Tokenizer(num_words=max_features)
#tokenizer.fit_on_texts(list(list_sentences_train))
#list_tokenized_train = tokenizer.texts_to_sequences(list_sentences_train)
#list_tokenized_test = tokenizer.texts_to_sequences(list_sentences_test)
#
#maxlen = 200
#X_t = pad_sequences(list_tokenized_train, maxlen=maxlen)
#X_te = pad_sequences(list_tokenized_test, maxlen=maxlen)
#
#totalNumWords = [len(one_comment) for one_comment in list_tokenized_train]
#
#inp = Input(shape=(maxlen, ))
#
#embed_size = 128
#x = Embedding(max_features, embed_size)(inp)
#
#x = LSTM(60, return_sequences=True,name='lstm_layer')(x)
#
#x = GlobalMaxPool1D()(x)
#
#
#x = Dropout(0.1)(x)
#
#x = Dense(50, activation="relu")(x)
#
#x = Dropout(0.1)(x)
#
#x = Dense(6, activation="sigmoid")(x)
#
#
#
#
#model = Model(inputs=inp, outputs=x)
#model.compile(loss='binary_crossentropy',
#                  optimizer='adam',
#                  metrics=['accuracy'])
#
#
#batch_size = 32
#epochs = 2
#model.fit(X_t,y, batch_size=batch_size, epochs=epochs, validation_split=0.1)
#s=model.predict(X_te)
#s=np.average(s, axis=1)
#submission = pd.DataFrame.from_dict({
#    'id': test["0"],
#    'prediction': s})
#submission.to_csv('wiki.csv', index=False)

model = keras.models.load_model('lstm.h5')
test1 = pd.read_json('prompts.jsonl',lines=True)
test = pd.json_normalize(test1['prompt'])['text'].to_frame()

#test = pd.read_csv('data_univtrig.csv')
#test=pd.Series(target_texts)
list_sentences_test = test['text'][0:2717]
max_features = 20000

#tokenizer = Tokenizer(num_words=max_features)
with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)
list_tokenized_test = tokenizer.texts_to_sequences(list_sentences_test)
maxlen = 200
X_te = pad_sequences(list_tokenized_test, maxlen=maxlen)
s=model.predict(X_te)


t= [item[0] for item in s ]
submission = pd.DataFrame.from_dict({
    'id': test['text'][0:2717],
    'prediction': t})
submission.to_csv('toxicity_toxicprompts.csv', index=False)
