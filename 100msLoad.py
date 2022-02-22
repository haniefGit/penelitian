import time
import pandas as pd
import pyfirmata
start_time1 = time.time()
path = pd.ExcelFile('load26.xlsx')
df = pd.read_excel(path,'Sheet1')
df.index += 1
last = df.index[-1]
print(last)

da = .09100001
db = 0.09251
dc = 0.09253
dd = 0.0921
d6 = 0.092505
d9 = 0.0914
d10 = 0.09059
d11 = 0.0913
d14 = 0.0907
d15 = 0.091
d18 = .09100005
d22 = 0.0922
d23 = 0.09255
d12 = 0.0909
d25 = 0.0919
d24 = 0.0924
d26 = 0.0922

shift = 2
delay = d14

port = 'COM6'
board = pyfirmata.Arduino(port)
servo_pin4 = board.get_pin('d:4:s') #pin 11 Arduino
servo_pin5 = board.get_pin('d:5:s')
servo_pin6 = board.get_pin('d:6:s')
servo_pin7 = board.get_pin('d:7:s')
servo_pin8 = board.get_pin('d:8:s')
servo_pin9 = board.get_pin('d:9:s')
servo_pin10 = board.get_pin('d:10:s')
servo_pin11 = board.get_pin('d:11:s')
print("--- %s seconds preparing ---" % (time.time() - start_time1))
start_time = time.time()
i = 0
while(i<last-1):
    if(i<=last-1 and shift == 1):

        t1 = int(df.time[i:i + 1])
        s1 = int(df.z1[i:i + 1])
        s2 = int(df.z2[i:i + 1])
        s3 = int(df.z3[i:i + 1])
        s4 = int(df.z4[i:i + 1])
        s5 = int(df.z5[i:i + 1])
        s6 = int(df.z6[i:i + 1])
        s7 = int(df.z7[i:i + 1])
        s8 = int(df.z8[i:i+1])
        print(t1,s1,s2,s3,s4,s5,s6,s7,s8, f"Shift: {shift}")

        servo_pin8.write(s1)
        servo_pin9.write(s2)
        servo_pin10.write(s3)
        servo_pin11.write(s4)
        i = i + 1
        time.sleep(delay)
    if (i <= last - 1 and shift == 2):
        t1 = int(df.time[i:i + 1])
        s1 = int(df.z1[i:i + 1])
        s2 = int(df.z2[i:i + 1])
        s3 = int(df.z3[i:i + 1])
        s4 = int(df.z4[i:i + 1])
        s5 = int(df.z5[i:i + 1])
        s6 = int(df.z6[i:i + 1])
        s7 = int(df.z7[i:i + 1])
        s8 = int(df.z8[i:i + 1])
        print(t1, s1, s2, s3, s4, s5, s6, s7, s8, f"Shift: {shift}")

        servo_pin4.write(s1)
        servo_pin5.write(s2)
        servo_pin6.write(s3)
        servo_pin7.write(s4)
        servo_pin8.write(s5)
        servo_pin9.write(s6)
        servo_pin10.write(s7)
        servo_pin11.write(s8)

        i = i + 1
        time.sleep(delay)
else:
    print("End of the loop")
    print("--- %s seconds ---" % (time.time() - start_time))