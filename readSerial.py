import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

portList = []

for onePort in ports:
    portList.append(str(onePort))
    print(str(onePort))

val = input("select Port: COM")

for x in range(0,len(portList)):
    if portList[x].startswith("COM" + str(val)):
        portVar = "COM" + str(val)
        print(portList[x])

serialInst.baudrate = 9600
serialInst.port = portVar
serialInst.open()

while True:
    if serialInst.in_waiting:
        packet = serialInst.readline()
        new = packet.decode('utf')
        # print(new)
        new1 = new.split(': ')
        # print(new1)
        dataIn = new1[0]
        if dataIn == 'data1':
            data1 = new1[1]
            # print('Data1 Success: ',data1)
        if dataIn == 'data2':
            data2 = new1[1]
            # print('Data2 Success: ',data2)
        if dataIn == 'data3':
            data3 = new1[1]
            # print('Data3 Success: ',data3)
        if dataIn == 'data4':
            data4 = new1[1]
            # print('Data4 Success: ',data4)
        if dataIn == 'data5':
            data5 = new1[1]
            # print('Data5 Success: ',data5)
        if dataIn == 'data6':
            data6 = new1[1]
            # print('Data6 Success: ',data6)
        if dataIn == 'data7':
            data7 = new1[1]
            # print('Data7 Success: ',data7)
        if dataIn == 'data8':
            data8 = new1[1]
            # print('Data8 Success: ',data8)
            # print(data1,data2,data3,data4,data5,data6,data7,data8)

            if int(data1) > 400:
                N1 = 1
            else : N1 = 0
            if int(data2) > 400:
                N2 = 1
            else : N2 = 0
            if int(data3) > 400:
                N3 = 1
            else : N3 = 0
            if int(data4) > 400:
                N4 = 1
            else : N4 = 0
            if int(data5) > 400:
                N5 = 1
            else : N5 = 0
            if int(data6) > 400:
                N6 = 1
            else : N6 = 0
            if int(data7) > 400:
                N7 = 1
            else : N7 = 0
            if int(data8) > 400:
                N8 = 1
            else : N8 = 0
            Rstate = 1
            InputData = [data1,data2,data3,data4,data5,data6,data7,data8]
            new_items = [x[:-2] for x in InputData]
            NN=[N1,N2,N3,N4,N5,N6,N7,N8,Rstate]
            # print(new_items)
            print(NN)
            # print(InputData)
