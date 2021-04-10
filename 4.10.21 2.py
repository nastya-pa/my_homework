def net(data):
    processed_data = []
    lists = []
    answ = ''
    for i in range(len(data)):
        a = data.find(data[i])
        lists.append(a)
        f = lists.pop(0)
        b = data.find(data[i], int(f)+1)
        processed_data.append(data[a:b+1:])
        processed_data.sort(key=len)
        answ = processed_data[::-1]
    return answ[:1]


print(net('sdkjfhlazxnmcbzmnxbcmznxbcmznxbcae'))
