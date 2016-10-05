import requests
import json

'''PART 1'''
'''
url = 'http://challenge.code2040.org/api/register'
dictionary = {'token': '57cc8bcb05af9f30e91e56b911abd698', 'github': 'https://github.com/adolfoportilla/code2040API'}

response = requests.post(url, json = dictionary)

print(response.text)
'''


'''PART 2'''

'''
url = 'http://challenge.code2040.org/api/reverse'
dictionary = {'token': '57cc8bcb05af9f30e91e56b911abd698'}

response = requests.post(url, json = dictionary)
#Reverse the string
reverse = response.text[::-1]

dictionarySent = {'token': '57cc8bcb05af9f30e91e56b911abd698', 'string': reverse}

response2 = requests.post('http://challenge.code2040.org/api/reverse/validate', json = dictionarySent)

print(response2.text)
'''


