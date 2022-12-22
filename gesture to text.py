import cv2
import time
import os
import math
import HandtrackingModule as htm

wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

folderpath = "fingers"
myList = os.listdir(folderpath)
print(myList)
pTime = 0
overlayList = []


for imPath in myList:
    image = cv2.imread(f'{folderpath}/{imPath}')
    overlayList.append(image)

detector = htm.handDetector(detectionCon=0.75)

tipIds = [4, 8, 12, 16, 20]
alph = ' '

while True:

    success, img = cap.read()
    img = cv2.flip(img, 1)
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    print(lmList)

    if len(lmList) != 0:
        fingers = []

        # thumb (use right hand)
        if lmList[tipIds[0]][1] < lmList[tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
        # another 4 finger
        for id in range(1, 5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        # print(fingers)
        totalFingers = fingers.count(1)
        print(totalFingers)

        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        x3, y3 = lmList[12][1], lmList[12][2]
        x9, y9 = lmList[9][1], lmList[9][2]
        x5, y5 = lmList[5][1], lmList[5][2]
        x6, y6 = lmList[6][1], lmList[6][2]
        x10, y10 = lmList[10][1], lmList[10][2]
        x4, y4= lmList[4][1], lmList[4][2]
        x15, y15 = lmList[15][1], lmList[15][2]
        x8, y8 =lmList[8][1], lmList[8][2]
        x12, y12= lmList[12][1], lmList[12][2]
        x16, y16 = lmList[16][1], lmList[16][2]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
        length12_4 = math.hypot(x3 - x1, y3 - y1)
        length4_8 = math.hypot(x2 - x1, y2 - y1)
        length4_9 = math.hypot(x9 - x1, y9 - y1)
        length4_5 = math.hypot(x5 - x1, y5 - y1)
        length4_6 = math.hypot(x6 - x1, y6 - y1)
        length4_10 = math.hypot(x10 - x1, y10 - y1)
        length4_10 = math.hypot(x10 - x1, y10 - y1)
        length4_15 = math.hypot(x15 - x4, y15 - y4)
        length8_12 = math.hypot(x12 - x8, y12 - y8)
        length16_12=math.hypot(x16 - x12, y16 -y12)
        length4_5= math.hypot(x5-x4, y5-y4)
        if totalFingers == 0:
            alph = 'E'

            if lmList[16][2] and lmList[4][1] > lmList[12][1]:
                alph='N'
            if lmList[14][2]<lmList[18][2] and lmList[4][1] >lmList[16][1]:
                alph='M'

        if totalFingers==1:
            if lmList[4][1] - lmList[8][1] < 20 and lmList[8][1] - lmList[12][1] < 20 and lmList[12][1] - lmList[16][1] < 20:
                alph='O'

            if lmList[4][2] < lmList[tipIds[0] - 1][2] and lmList[4][1]+10 > lmList[tipIds[0] - 1][1] and lmList[tipIds[0]][1] < lmList[8][1]:
                alph = 'A'
            if lmList[4][2] < lmList[tipIds[0] - 1][2] and lmList[tipIds[0]][1] > lmList[8][1] and lmList[tipIds[0]][1] < lmList[8][1]+10 :
                alph = 'S'
            if lmList[4][2] < lmList[tipIds[0] - 1][2] and lmList[3][1] > lmList[6][1] and lmList[3][1] < lmList[10][1]  and lmList[4][1] < lmList[10][1]-5:
                alph = 'T'
            if length12_4 <=70 and lmList[8][2] > lmList[6][2] and lmList[12][2] > lmList[10][2] and lmList[16][2] > lmList[14][2] and lmList[20][2] < lmList[18][2]:
                alph = 'I'
            if length12_4 <=40 and lmList[8][2] < lmList[6][2] and lmList[12][2] > lmList[10][2] and lmList[16][2] > lmList[14][2] and lmList[20][2] > lmList[18][2]:
                alph = 'D'
            if lmList[17][1]<lmList[20][1] and length12_4 <=70 and lmList[8][2] > lmList[6][2] and lmList[12][2] > lmList[10][2] and lmList[16][2] > lmList[14][2] and lmList[20][2] < lmList[18][2]:
                alph = 'J'

            if lmList[8][2]<lmList[7][2] and length12_4>50:
                alph='z'



            if lmList[12][2] < lmList[11][2]:
                alph = 'p'
        if totalFingers == 3:
            if length4_8 <=30:
                alph ='F'
            if lmList[8][2]<lmList[6][2] and lmList[12][2]<lmList[10][2] and lmList[4][1]>lmList[6][1] :
               alph='W'

        if totalFingers >= 2:
            if length4_9 <=30 and lmList[8][2] < lmList[6][2] and lmList[12][2] < lmList[10][2]:
                alph = 'H'
        if totalFingers == 1 or totalFingers == 2:
            if length4_6 <=40 and lmList[8][2] > lmList[6][2] and lmList[8][1] > lmList[5][1]:
                alph = 'G'
        if totalFingers==2:

            if lmList[8][2]<lmList[6][2] and lmList[12][2]<lmList[10][2] and lmList[4][1]>lmList[6][1] and lmList[4][1]<lmList[10][1]:
               alph='K'
            if lmList[8][2]<lmList[6][2] and lmList[12][2]<lmList[10][2] and lmList[4][1]>lmList[6][1] and lmList[4][1]<lmList[10][1] and length4_15 <=40:
               alph='V'
            if length8_12<=40 and lmList[8][2]<lmList[6][2] and lmList[12][2]<lmList[10][2] and lmList[4][1]>lmList[6][1] and lmList[4][1]<lmList[10][1] and length4_15 <=40:
               alph='U'
            if lmList[17][1]<lmList[20][1] and lmList[8][2] > lmList[6][2] and lmList[12][2] > lmList[10][2] and lmList[16][2] > lmList[14][2] and lmList[20][2] < lmList[18][2]:
                alph = 'Y'
            if lmList[8][2] < lmList[6][2] and lmList[12][2] > lmList[10][2] and lmList[16][2] > lmList[14][2] and lmList[20][2] > lmList[18][2]:
                alph='L'
            if (lmList[8][1]>lmList[12][1] and length8_12<20) or (lmList[8][1]>lmList[12][1] and lmList[7][1]-lmList[11][1]<10) :
                alph='R'

        if totalFingers==4:

            if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1] and lmList[8][2] < lmList[6][2] and lmList[12][2] < lmList[10][2] and lmList[16][2] < lmList[14][2] and lmList[20][2] < lmList[18][2]:
                alph = 'B'
                if length4_9 <= 30 and lmList[8][2] < lmList[6][2] and lmList[12][2] < lmList[10][2]:
                    alph = 'H'
        if totalFingers==5 and lmList[8][2] -lmList[7][2]<=-2 and lmList[8][2] -lmList[7][2]>=-20:
            if lmList[6][2]<lmList[4][2]:
                alph='c'












        # h, w, c = overlayList[totalFingers - 1].shape
        # # image size 200X200 recomended
        # img[0:h, 0:w] = overlayList[totalFingers - 1]
        #
        img2 = cv2.flip(img, 1)
        cv2.rectangle(img, (28, 255), (178, 425), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, str(alph), (45, 375), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 25)
        alph=' '

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (400, 70), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 3)

    cv2.imshow("Images", img)
    cv2.waitKey(1)
