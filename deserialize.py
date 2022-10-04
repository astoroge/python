import json
import pickle

with open('group.json', 'r', encoding='utf-8') as f:
    result = json.load(f)
print(result)

with open('group.pickle', 'rb') as f:
    result2 = pickle.load(f)
print(result2)