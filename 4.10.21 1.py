def da(data):
    b = []
    processed_data = []
    for i in range(len(data)):
        if i not in b:
            f = data.find(data[i])
            s = data.rfind(data[i])
            processed_data.append(data[f:s+1:])
            b.append(i)
    processed_data.sort()
    return processed_data[:1]


print(da('sdkjfhlazxnmcbzmnxbcmznxbcmznxbcae'))
