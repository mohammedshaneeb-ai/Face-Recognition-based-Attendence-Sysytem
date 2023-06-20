print("shaneeb")
import cv2
import os


cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

imgBackground = cv2.imread('Resources/background.png')

# impoting modes
folderModePath = 'Resources/Modes/'
ModePathList = os.listdir(folderModePath)
ModePathList.sort()  
imgModeList = []

for path in ModePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath,path)))

print(ModePathList)



while True:
    success, img = cap.read() 

    imgBackground[162:162+480,55:55+640] = img
    imgBackground[44:44+633, 808:808+414] = imgModeList[2]
    

    cv2.imshow('Face Attendence',imgBackground)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break