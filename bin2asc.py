binArray = [1010100,1000001,1000101,1011000,1000011,1010111,1010000,1001010,1000001,1000101,1011000,1000110,1011000,1010001,1010011,1000111,1010011,1001000,1000010,1010101,1010101,1001110,1010110,1001010,1010111,1010111,1001000]
decArray = []
decTemp = 0
for i in range(len(binArray)):
    power = 64
    decTemp = 0
    for j in str(binArray[i]):
        if j == '1':
            decTemp += int(j) * power
            power = power/2
        else:
            power = power/2
    decArray.append(int(decTemp))
print(decArray)
print("converted to ascii:")
print(''.join([chr(i) for i in decArray]))