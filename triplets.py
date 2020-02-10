import spacy

nlp = spacy.load("en_core_web_sm")
text_input = input('Enter your sentence: ')
text = nlp(text_input)

subjects = []
subj = None
for word in text:
    if 'nsubjpass' in word.dep_:
        subj = word
        subjects.append(word)
    elif word.dep_ == 'conj' and word.head == subj:
        subjects.append(word)

VerbRoot = ['ROOT', 'auxpass']
OBJ = ['dobj', 'pobj', 'dobj']
verbs = [word for word in text if (word.dep_ in VerbRoot)]
objects = [word for word in text if (word.dep_ in OBJ)]

for i in range(len(verbs)):
    print('|- {\'subject\':' + str(subjects) + ', \'relation\':' + str(verbs[i]),
          ', \'object\':' + str(objects[0]) + '}')