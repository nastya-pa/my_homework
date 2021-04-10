def gen():
    with open('lol.txt', 'r') as file:
        a = []
        b = ''
        file_read = file.read()
        for i in file_read:
            if i == ' ' or i == '\n':
                a.append(b)
                b = ''
            else:
                b += i
        ind = 0
        while True:
            if ind > len(a)-1:
                break
            data = yield a[ind]
            if data == 'next':
                ind += 1
            if data == 'previous':
                if ind == 0:
                    continue
                else:
                    ind -= 1
                    yield a[ind]
                    gen()
                    yield a[ind]


answ = gen()
print(next(answ))
answ.send('previous')
print(next(answ))
print(next(answ))
answ.send('next')
print(next(answ))
print(next(answ))
answ.send('previous')
print(next(answ))
print(next(answ))
print(next(answ))
answ.send('next')
print(next(answ))
