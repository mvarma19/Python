import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches
data=json.load(open("data.json","r"))

def translate(word):
    word=word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys()))>0:
        yn= input("Did you mean %s instead? Enter Y if yes or N if no:" %get_close_matches(word,data.keys())[0])
        if yn=="Y":
            return data[get_close_matches(word,data.keys())[0] ]
        elif yn=="N":
            return "The word doesn't exist.Please double check it."
        else:
            return "We didn't understand your entry."


    else:
        return "The word doesn't exist.Please double check it."

def test():
    user = input("Enter word:")
    output=(translate(user))
    
    if type(output)==list:
        for item in output:
            print(item)
    else:
        print(output)
    test()
if __name__ == '__main__':
    test()
