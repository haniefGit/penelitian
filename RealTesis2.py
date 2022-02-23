from pyfirmata import util, ArduinoMega
import time
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
new_model = load_model('ANN44.h5')


board = ArduinoMega('COM6')
it = util.Iterator(board)
it.start()

nA = board.get_pin('a:0:i')
nB = board.get_pin('a:1:i')
nC = board.get_pin('a:2:i')
nD = board.get_pin('a:3:i')
nE = board.get_pin('a:4:i')
nF = board.get_pin('a:5:i')
nG = board.get_pin('a:6:i')
nH = board.get_pin('a:7:i')

serv1 = board.get_pin('d:4:s')
serv2 = board.get_pin('d:5:s')
serv3 = board.get_pin('d:6:s')
serv4 = board.get_pin('d:7:s')
serv5 = board.get_pin('d:8:s')
serv6 = board.get_pin('d:9:s')
serv7 = board.get_pin('d:10:s')
serv8 = board.get_pin('d:11:s')


nR = 0 #Rstate
RecovSpeed = 0.05
delayServo = 0.0907
i = 0

while True:
    if nA.read() is not None:
        # -------------------------------------------------
        n0 = int (nA.read()*1024)
        n1 = int (nB.read()*1024)
        n2 = int (nC.read()*1024)
        n3 = int (nD.read()*1024)
        n4 = int (nE.read()*1024)
        n5 = int (nF.read()*1024)
        n6 = int (nG.read()*1024)
        n7 = int (nH.read()*1024)
        # ------------------------------------------------
        if n0 > 400:
            N1 = 1
        else:
            N1 = 0
        if n1 > 400:
            N2 = 1
        else:
            N2 = 0
        if n2 > 400:
            N3 = 1
        else:
            N3 = 0
        if n3 > 400:
            N4 = 1
        else:
            N4 = 0
        if n4 > 400:
            N5 = 1
        else:
            N5 = 0
        if n5 > 400:
            N6 = 1
        else:
            N6 = 0
        if n6 > 400:
            N7 = 1
        else:
            N7 = 0
        if n7 > 400:
            N8 = 1
        else:
            N8 = 0
        # ------------------------------------------------
        if nR >= 1:
            Rstate = 1
        else:
            Rstate = 0

        NN = [N1, N2, N3, N4, N5, N6, N7, N8, Rstate]
        print(NN)
        array_input = NN
        predict_folder = np.argmax(new_model.predict([array_input]))
        video = 'Video' + str(predict_folder + 1)
        print(video)
        # ------------------------------------------------
        if(predict_folder<=25 and nR >= 0.5):
            print(predict_folder)
            print(n0, n1, n2, n3, n4, n5, n6, n7, Rstate)
            servo_angle = 0
            #---------------------------------------------
            start_time = time.time()
            fileNum = predict_folder + 1
            madlib = f"100load{fileNum}.xlsx"

            path = pd.ExcelFile(madlib)
            df = pd.read_excel(path, 'Sheet1')
            df.index += 1
            last = df.index[-1]
            print(last)

            while (i < last - 1):
                if (i <= last ):
                    t1 = int(df.time[i:i + 1])
                    s1 = int(df.z1[i:i + 1])
                    s2 = int(df.z2[i:i + 1])
                    s3 = int(df.z3[i:i + 1])
                    s4 = int(df.z4[i:i + 1])
                    s5 = int(df.z5[i:i + 1])
                    s6 = int(df.z6[i:i + 1])
                    s7 = int(df.z7[i:i + 1])
                    s8 = int(df.z8[i:i + 1])
                    print(t1, s1, s2, s3, s4, s5, s6, s7, s8)

                    serv1.write(s1)
                    serv2.write(s2)
                    serv3.write(s3)
                    serv4.write(s4)
                    serv5.write(s5)
                    serv6.write(s6)
                    serv7.write(s7)
                    serv8.write(s8)

                    i = i + 1
                    time.sleep(delayServo)
            else:
                print("End of the loop")
                print("--- %s seconds ---" % (time.time() - start_time))

            # ---------------------------------------------
            nR = 0

        # ------------------------------------------------


        nR = nR + RecovSpeed
        print(nR)

    time.sleep(1)

