import pyttsx3
pasha = pyttsx3.init()
a = {'day': '2021-05-28', 'time': '09:51:00', 'temp_max': 24.23, 'temp_min': 20.29, 'temp_for_now': 22.12, 'humidity': 78, 'sunrise': '01:55:12', 'sunset': '17:55:34', 'description': 'scattered clouds'}
for i in a:
    pasha.say(i)
    pasha.say(a[i])
pasha.runAndWait()
