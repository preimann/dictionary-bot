import requests
import json

app_id = 'your app_id'
app_key = 'your app key'

language = 'en'
inflected_form = str(raw_input("Type an inflected form here: "))

#lemmatron call
url_lemma = 'https://od-api.oxforddictionaries.com:443/api/v1/inflections/' + language + '/' + inflected_form.lower()
r1 = requests.get(url_lemma, headers = {'app_id': app_id, 'app_key': app_key})
Lemmatron_response = r1.json()
lemma = Lemmatron_response['results'][0]['lexicalEntries'][0]['inflectionOf'][0]['id']

if lemma != inflected_form:
    print "The root of that word is", lemma
else:
    print 'That is already a lemma'

print
print "Would you like to see synonyms of that? Y/N"
answer = str(raw_input("Enter Y or N"))
print
if answer == "Y":
    #Thesaurus call
    url_thes = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + lemma.lower() + '/synonyms'
    r2 = requests.get(url_thes, headers = {'app_id': app_id, 'app_key': app_key})
    thes_response = r2.json()
    syn = thes_response['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['subsenses'][0]['synonyms'][0]['text']
    #entries call
    url_entry = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + lemma.lower()
    r3 = requests.get(url_entry, headers={'app_id': app_id, 'app_key': app_key})
    entry_response = r3.json()
    defi = entry_response['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0]
    print "Okay, one such synonym is", syn
    print syn + ' means',  str(defi)
elif answer != 'Y' or 'N':
    print 'Please enter Y or N'

print
print "Guess what else I can do! I can also translate to other languages. Would you like to translate it to GERMAN or SPANISH?"
tr_lang = str(raw_input(""))

if tr_lang == 'German':
    url_de = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + lemma.lower() + '/translations=de'
    r4 = requests.get(url_de, headers = {'app_id': app_id, 'app_key': app_key})
    de_response = r4.json()
    de_tr = de_response['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['translations'][0]['text']
    print "In German it's", de_tr
else:
    print 'Nope'
print
print "Thanks for using my dictionary!"


