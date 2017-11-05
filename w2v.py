import spacy
import os
import pickle
import datetime

start = datetime.datetime.now()

nlp = spacy.load('en')

folder = '../findlectures-talks/transcripts/'
files = [filename for filename in os.listdir (folder) if filename.endswith(".txt")]

print(files)

for fname in files:
  print(fname)
  f = open(folder + fname)
  text = f.read()
  f.close()

  doc = nlp(text)

  id = fname.split(".")[0]
  #data[id] = [(w.text, w.pos_) for w in doc]

  print(doc.ents)
  out = open(folder + id + '.pickle', 'wb')

print(start)

pickle.dump(data, out)
out.close()

print(datetime.datetime.now())
