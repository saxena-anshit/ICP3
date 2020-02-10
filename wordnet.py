from nltk.corpus import wordnet


for List in wordnet.synsets('rice'):
    print(List, List.hyponyms())

for List in wordnet.synsets('rice'):
    print(List, List.hypernyms())

for List in wordnet.synsets('room'):
    print(List, List.part_meronyms())

for List in wordnet.synsets('room'):
    print(List, List.part_holonyms())

for List in wordnet.synsets('listen'):
    print(List, List.entailments())
