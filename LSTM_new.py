#import pandas as pd
#from sklearn.model_selection import train_test_split
#import preprocess_data
#from keras import layers

#from matplotlib import pyplot as plt
from sklearn.externals import joblib
#import numpy as np
#from sklearn.preprocessing import LabelEncoder
#import gensim
#from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
#from keras.models import Sequential
#from keras.layers import Activation, Dense, Dropout, Embedding, Flatten, Conv1D, MaxPooling1D, LSTM
#from keras.callbacks import ReduceLROnPlateau, EarlyStopping
#import pandas as pd
#from sklearn.model_selection import train_test_split


#dataset = pd.read_csv(r"C:\Users\rohit\OneDrive\Desktop\Legitt\clean.csv")
#dataset = dataset[dataset.Sentiment != "['neutral']"]


#df_train, df_test = train_test_split(dataset, test_size=0.2,random_state=42)
#print("TRAIN size:", len(df_train))
#print("TEST size:", len(df_test))

#documents = [preprocess_data.preprocess_tweet(str(_text)) for _text in df_train.Tweets]
#documents = [str(_text).split() for _text in df_train.Tweets] 

#w2v_model = gensim.models.word2vec.Word2Vec(size=37,window=7,min_count=2,workers=8)

#w2v_model.build_vocab(documents)

#words = w2v_model.wv.vocab.keys()
#vocab_size = len(words)
#print("Vocab size", vocab_size)

#w2v_model.train(documents, total_examples=len(documents), epochs=32)

#joblib.dump(w2v_model,r'C:\Users\rohit\OneDrive\Desktop\Legitt\w2vmodel.sav')
#w2v_model.most_similar("buy")

#loaded_model = joblib.load(r'C:\Users\rohit\OneDrive\Desktop\Legitt\w2vmodel.sav')
#loaded_model.wv.most_similar("hate")

#tokenizer = Tokenizer()
#tokenizer.fit_on_texts(df_train.Tweets)

#joblib.dump(tokenizer,r'C:\Users\rohit\OneDrive\Desktop\Legitt\tokenizer_.LSTM.save')
#vocab_size = len(tokenizer.word_index) + 1
#print("Total words", vocab_size)

#x_train = pad_sequences(tokenizer.texts_to_sequences(df_train.Tweets), maxlen=37,padding = 'post')
#x_test = pad_sequences(tokenizer.texts_to_sequences(df_test.Tweets), maxlen=37,padding = 'post')

#encoder = LabelEncoder()
#encoder.fit(df_train.Sentiment.tolist())


#y_train = encoder.transform(df_train.Sentiment.tolist())
#y_test = encoder.transform(df_test.Sentiment.tolist())

#y_train = y_train.reshape(-1,1)
#y_test = y_test.reshape(-1,1)


#embedding_matrix = np.zeros((vocab_size, 37))
#for word, i in tokenizer.word_index.items():
#  if word in w2v_model.wv:
#    embedding_matrix[i] = w2v_model.wv[word]
#print(embedding_matrix.shape)


#embedding_layer = Embedding(vocab_size, 37, weights=[embedding_matrix], input_length=37, trainable=False)

#model = Sequential()
#model.add(embedding_layer)
##model.add(layers.Dense(100, activation='relu'))
#model.add(layers.Dense(80, activation='sigmoid'))
#model.add(Dropout(0.5))
#model.add(LSTM(100, dropout=0.2, recurrent_dropout=0.2))
#model.add(Dense(1, activation='sigmoid'))

#model.summary()


#model.compile(loss='binary_crossentropy',
#              optimizer="adam",
#              metrics=['accuracy'])

#callbacks = [ ReduceLROnPlateau(monitor='val_loss', patience=5, cooldown=0),
#              EarlyStopping(monitor='val_acc', min_delta=1e-4, patience=5)]

#history = model.fit(x_train, y_train,
#                    batch_size=50,
#                    epochs=10,
#                    validation_split=0.2,
#                    verbose=1,
#                    callbacks=callbacks)
#######LSTM model
#joblib.dump(model,r'C:\Users\rohit\OneDrive\Desktop\Legitt\model_.LSTM.save')

#score1 = model.evaluate(x_test, y_test, batch_size=50)
#print()
#print("ACCURACY:",score[1])
#print("LOSS:",score[0])

model = joblib.load(r'model_.LSTM.save')
tokenizer = joblib.load(r'tokenizer_.LSTM.save')
model._make_predict_function()

def decode_sentiment(score):
    return 0 if score < 0.65 else 1

def predict(text):
    # Tokenize text
    x_test1 = pad_sequences(tokenizer.texts_to_sequences([text]), maxlen=37,padding = 'post')
    # Predict
    score = model.predict(x_test1)[0]
    # Decode sentiment
    label = decode_sentiment(score)

    return {"label": label, "score": float(score)}

