import requests
import datetime
import pyttsx3

answ1 = []
temp_max = []
temp_min = []
city = 'Kiev'
API_KEY = '3723b133b8a60405eaef4951712ca0e9'
url1 = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
response1 = requests.get(url1)
url3 = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric'
response3 = requests.get(url3)
user = input('введите "1", если хотите увидеть прогноз погоды на 1 день, и "3", если хотите увидеть прогноз погоды на 3 дня: ')


def func1():
    answ = {}
    if user == '1':
        answ['day'] = str(datetime.datetime.utcfromtimestamp(response1.json()['dt']))[0:10]
        answ['time'] = str(datetime.datetime.utcfromtimestamp(response1.json()['dt']))[11:]
        answ['temp_max'] = response1.json()['main']['temp_max']
        answ['temp_min'] = response1.json()['main']['temp_min']
        answ['temp_for_now'] = response1.json()['main']['temp']
        answ['humidity'] = response1.json()['main']['humidity']
        answ['sunrise'] = str(datetime.datetime.utcfromtimestamp(response1.json()['sys']['sunrise']))[11:]
        answ['sunset'] = str(datetime.datetime.utcfromtimestamp(response1.json()['sys']['sunset']))[11:]
        answ['description'] = response1.json()['weather'][0]['description']
        answ1.append(answ)
    elif user == '3':
        ch = 0
        description = []
        date = response3.json()['list'][ch]['dt_txt'][0:10]
        while ch <= 24:
            humidity = 0
            if response3.json()['list'][ch]['dt_txt'][0:10] == date:
                temp_max.append(response3.json()['list'][ch]['main']['temp_max'])
                temp_min.append(response3.json()['list'][ch]['main']['temp_min'])
                humidity += response3.json()['list'][ch]['main']['humidity']
                if str(response3.json()['list'][ch]['dt_txt'][11:]) == '15:00:00' or str(response3.json()['list'][ch]['dt_txt'][11:]) == '18:00:00':
                    description = response3.json()['list'][ch]['weather'][0]['description']
                elif str(response3.json()['list'][ch]['dt_txt'][11:]) < '18:00:00':
                    description = response3.json()['list'][ch]['weather'][0]['description']
                ch += 1
            else:
                average_humidity = humidity / ch
                answ = {'day': date, 'temp_max': max(temp_max), 'temp_min': min(temp_min), 'average_humidity': str(average_humidity)[0:4], 'description': description}
                answ1.append(answ)
                date = response3.json()['list'][ch]['dt_txt'][0:10]
    return answ1


def func2(answer, user):
    if user == '1':
        print('|--------------------------------|')
        for i in answer[0]:
            if i == 'day' or i == 'time':
                net = (34 - len(answer[0][i]) - 6) // 2
                print('|', net*' ', answer[0][i], net*' ', '|')
                print('|--------------------------------|')
            elif (len(str(answer[0][i])) + len(i) + 7) != 34:
                net = 34 - (len(str(answer[0][i])) + len(i) + 7)
                net_da = f'{i}: {answer[0][i]}'
                print('|', net_da, net*' ', '|')
        print('|--------------------------------|')
    elif user == '3':
        ch1 = 0
        print('|--------------------------------------|')
        while ch1 != 3:
            for i in answer[ch1]:
                if i == 'day':
                    net = (40 - len(answer[ch1][i]) - 6) // 2
                    print('|', net*' ', answer[ch1][i], net*' ', '|')
                    print('|--------------------------------------|')
                elif i == 'description':
                    net = 40 - (len(str(answer[ch1][i])) + len(i) + 7)
                    net_da = f'{i}: {answer[ch1][i]}'
                    print('|', net_da, net*' ', '|')
                    print('|--------------------------------------|')
                    ch1 += 1
                else:
                    net = 40 - (len(str(answer[ch1][i])) + len(i) + 7)
                    net_da = f'{i}: {answer[ch1][i]}'
                    print('|', net_da, net*' ', '|')
    return '\n'


print(func2(func1(), user))


def func3(an):
    pasha = pyttsx3.init()
    ch = 0
    for j in an:
        for i in j:
            pasha.say(i)
            pasha.say(an[ch][i])
        ch += 1
        pasha.runAndWait()


print(func3(func1()))
