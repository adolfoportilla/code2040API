import requests
import json

'''PART 1'''
def part1():
    url = 'http://challenge.code2040.org/api/register'
    dictionary = {'token': '57cc8bcb05af9f30e91e56b911abd698', 'github': 'https://github.com/adolfoportilla/code2040API'}

    #api request
    response = requests.post(url, json = dictionary)

    print(response.text)




'''PART 2'''
def part2():
    url = 'http://challenge.code2040.org/api/reverse'
    token = {'token': '57cc8bcb05af9f30e91e56b911abd698'}

    response = requests.post(url, json = dictionary)
    #Reverse the string
    reverse = response.text[::-1]

    dictionarySent = {'token': '57cc8bcb05af9f30e91e56b911abd698', 'string': reverse}

    response2 = requests.post('http://challenge.code2040.org/api/reverse/validate', json = dictionarySent)

    print(response2.text)


'''PART 3 '''
def part3():
    url = 'http://challenge.code2040.org/api/haystack'
    token = {'token': '57cc8bcb05af9f30e91e56b911abd698'}

    response = requests.post(url, json = token)
    dictionary = json.loads(response.text)

    needle = dictionary.get('needle')
    haystack = dictionary.get('haystack')

    #Check if the needle is in the haystack
    if needle in haystack:
        index = haystack.index(needle)

    #dictionary to be sent to the api
    dictionarySent = {'token': '57cc8bcb05af9f30e91e56b911abd698', 'needle': index}
    response2 = requests.post('http://challenge.code2040.org/api/haystack/validate', json = dictionarySent)

    print (response2.text)


'''PART 4'''
def part4():
    url = 'http://challenge.code2040.org/api/prefix'
    token = {'token': '57cc8bcb05af9f30e91e56b911abd698'}
    response = requests.post(url, json = token)

    dictionary = json.loads(response.text)
    prefix = dictionary.get('prefix')
    array = dictionary.get('array')

    #list were the different prefixes from prefix will be stored
    differentPrefixes = []

    #for loop to check each individual prefix in the array
    for item in array:
        #check if the prefix is different from the one in the array
        if prefix != item[0:len(prefix)]:
            differentPrefixes += [item]

    #dictionary to be sent to the api
    dictionarySent = {'token': '57cc8bcb05af9f30e91e56b911abd698', 'array': differentPrefixes}
    response2 = requests.post('http://challenge.code2040.org/api/prefix/validate', json = dictionarySent)

    print (response2.text)


'''PART 5'''
def secondConversion(interval):

    seconds = 0
    minutes = 0
    hours = 0
    days = 0

    if interval > 0:
        days = interval // 86400
        interval = interval - (days*86400)
    if interval > 0:
        hours = interval // 3600
        interval = interval - (hours*3600)
    if interval > 0:
        minutes = interval // 60
        interval = interval - (minutes*60)
    if interval > 0 :
        seconds = interval // 1
     

    return [seconds, minutes, hours, days]

def addSeconds(listTimes, datestamp):

    newTime = ""
    carry = 0

    #Add the seconds, check first if the seconds exceed 60
    if (int(datestamp[17:19]) + listTimes[0]) > 60:

        #check if the seconds are less than 9, so you can add the 0 to the front of the string
        if ((int(datestamp[17:19]) + carry + listTimes[0])%60) < 9:
            newTime = "0" + str((int(datestamp[17:19]) + listTimes[0]) % 60) + datestamp[-1]
        else:
            newTime = str((int(datestamp[17:19]) + listTimes[0]) % 60) + datestamp[-1]
        carry = 1

    elif (int(datestamp[17:19]) + listTimes[0]) == 60:
        newTime = "00" + datestamp[-1]
        carry = 1

    else:

        if (int(datestamp[17:19])+carry+listTimes[0]) < 9:
            newTime = datestamp[17] + str((int(datestamp[17:19]) + carry + listTimes[0])) + datestamp[-1] + newTime
        else:
            newTime = str(int(datestamp[17:19]) + listTimes[0]) + datestamp[-1]
        carry = 0


    #Add the minutes, check first if the minutes exceed 60
    if (int(datestamp[14:16]) + listTimes[1] + carry ) > 60:

        #check if the miniutes are less than 9, so you can add the 0 to the front of the string
        if ((int(datestamp[14:16]) + carry + listTimes[1]) % 60) < 10 :
            newTime = "0" +  str((int(datestamp[14:16]) + carry + listTimes[1]) % 60) + datestamp[-4] + newTime
        else:
            newTime = str((int(datestamp[14:16]) + carry + listTimes[1]) % 60) + datestamp[-4] + newTime

        #add a carry for the next level
        carry = 1
    elif (int(datestamp[14:16]) + listTimes[1] + carry ) == 60:
        newTime = "00" + datestamp[-4] + newTime
        carry = 1

    else:

        if (int(datestamp[14:16])+carry+listTimes[1]) < 9:
            newTime = datestamp[14] + str((int(datestamp[14:16]) + carry + listTimes[1])) + datestamp[-4] + newTime
            
        else:
            newTime = str(int(datestamp[14:16]) + listTimes[1] + carry) + datestamp[-4] + newTime

        carry = 0

    #Add the hours, check first if the hours exceed 24
    if (int(datestamp[11:13]) + listTimes[2] + carry ) > 24:
        
        if ((int(datestamp[11:13]) + carry + listTimes[2]) % 24 ) < 10:
            newTime = "0" +  str((int(datestamp[11:13]) + carry + listTimes[2]) % 24) + datestamp[-7] + newTime
        else:
            newTime = str((int(datestamp[11:13]) + carry + listTimes[2]) % 24) + datestamp[-7] + newTime

        #add a carry for the next level
        carry = 1

    #exact hour adds to 24
    elif (int(datestamp[11:13]) + listTimes[2] + carry ) ==  24:
        newTime = "00"+ datestamp[-7] + newTime
        carry = 1

    else:

        if (int(datestamp[11:13])+carry+listTimes[2]) < 9:
            newTime = datestamp[11] + str((int(datestamp[11:13]) + carry + listTimes[2])) + datestamp[-7] + newTime
            
        else:
            newTime = str(int(datestamp[11:13]) + listTimes[2] + carry) + datestamp[-7] + newTime

        carry = 0

    #Add the days, check first if the days exceed 28, to check feb
    if (int(datestamp[8:10]) + listTimes[3] + carry ) > 28 and int(datestamp[5:7]) == 2:
        
        if ((int(datestamp[8:10])+carry+listTimes[3])%28) < 10:
            newTime = "0"+ str((int(datestamp[8:10]) + carry + listTimes[3]) % 28) + datestamp[-10] + newTime
        else:
            newTime = str((int(datestamp[8:10]) + carry + listTimes[3]) % 28) + datestamp[-10] + newTime

        
        newTime = datestamp[0:5] + "03-" + newTime

    #Months with 30 days
    elif (int(datestamp[8:10]) + listTimes[3] + carry ) > 30 and (int(datestamp[5:7]) in [4,6,9,11]):

        #Special case when its the end of the month, i.e, 11.30 and you add one day, needs to say 12.01
        if ((int(datestamp[8:10])+carry+listTimes[3])%30) < 10:
            newTime = "0"+ str((int(datestamp[8:10]) + carry + listTimes[3])%30) + datestamp[-10] + newTime
        else:
            newTime = str((int(datestamp[8:10]) + carry + listTimes[3]) % 30) + datestamp[-10] + newTime
        
        newTime = datestamp[0:5] + datestamp[5] + str(int(datestamp[6])+1) + "-" + newTime
    
    #Months with 31 days
    elif (int(datestamp[8:10]) + listTimes[3] + carry ) > 31 and (int(datestamp[5:7]) in [1,3,5,7,8,10]):

        #Special case when its the end of the month, i.e, 11.30 and you add one day, needs to say 12.01
        if ((int(datestamp[8:10])+carry+listTimes[3])%31) < 9:
            newTime = "0"+ str((int(datestamp[8:10]) + carry + listTimes[3])%31) + datestamp[-10] + newTime
        else:
            newTime = str((int(datestamp[8:10]) + carry + listTimes[3]) % 31) + datestamp[-10] + newTime
        
        newTime = datestamp[0:5] + datestamp[5] + str(int(datestamp[6])+1) + "-" + newTime


    elif (int(datestamp[8:10]) + listTimes[3] + carry ) > 31 and (int(datestamp[5:7]) in [12]):

        #Special case when its the end of the month, i.e, 11.30 and you add one day, needs to say 12.01
        if ((int(datestamp[8:10])+carry+listTimes[3])%31) < 9:
            newTime = "0" + str((int(datestamp[8:10]) + carry + listTimes[3]) % 31) + datestamp[-10] + newTime
        else:
            newTime = str((int(datestamp[8:10]) + carry + listTimes[3]) % 31) + datestamp[-10] + newTime

        newTime = str(int(datestamp[0:4])+1) + "-01-" + newTime
   
    else:
        if ((int(datestamp[8:10])+carry+listTimes[3])%31) < 10:
            newTime = datestamp[8] + str((int(datestamp[8:10]) + carry + listTimes[3])) + datestamp[-10] + newTime
            
        else:
            newTime = str((int(datestamp[8:10]) + carry + listTimes[3])) + datestamp[-10] + newTime
        newTime = datestamp[0:8] + newTime


    return newTime

def PART5():
    
    url = 'http://challenge.code2040.org/api/dating'
    token = {'token': '57cc8bcb05af9f30e91e56b911abd698'}
    response = requests.post(url, json = token)

    dictionary = json.loads(response.text)
    datestamp = dictionary.get('datestamp')
    interval = dictionary.get('interval')

    conversions = secondConversion(interval)

    #conversions = [8, 35, 15, 0]
    #datestamp = '2016-10-08T18:41:12Z'

    newDatestamp = addSeconds(conversions, datestamp)

    dictionarySent = {'token': '57cc8bcb05af9f30e91e56b911abd698', 'datestamp': newDatestamp}
    response2 = requests.post('http://challenge.code2040.org/api/dating/validate', json = dictionarySent)

    print (response2.text)

PART5()























