import cv2
import numpy as np
import utlis

curveList=[]
avgVal=10

def getLaneCurve(img,display=2):

    imgCopy=img.copy()
    imgResult =img.copy()

    #step 1 thershholding

    imgThres = utlis.thresholding(img)

    #step 2 warpinggg

    h,w,c=img.shape
    points = utlis.valTrackbars()
    imgWarp=utlis.warpImage(imgThres,points,w,h)
    imgWarpPoints=utlis.drawPoints(imgCopy,points)

    #step 3 histogram
    midPoint,imgHist=utlis.getHistogram(imgWarp,display=True,minPer=0.5,region=4)
    curvePoint,imgHist=utlis.getHistogram(imgWarp,display=True,minPer=0.9)
    curveAvg=curvePoint-midPoint

    #step 4 curve thingy
    curveList.append(curveAvg)
    if len(curveList)>avgVal:
        curveList.pop(0)
    curve=int(sum(curveList)/len(curveList)) #basically findind the average to reduce the noise


    cv2.imshow('Histogram',imgHist)
    cv2.imshow('Thres',imgThres)
    cv2.imshow('Warp', imgWarp)
    cv2.imshow('WarpPoints', imgWarpPoints)
    return curve


if __name__ == '__main__':
    cap = cv2.VideoCapture('vid2.mp4')
    initialTrackBarValues=[99,96,25,220]
    utlis.initializeTrackbars(initialTrackBarValues)
    frameCounter=0
    while True:
        frameCounter += 1
        if cap.get(cv2.CAP_PROP_FRAME_COUNT) == frameCounter:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            frameCounter = 0
        success, img = cap.read()
        img = cv2.resize(img,(480,240))
        curve=getLaneCurve(img,display=2)
        print(curve)
        #cv2.imshow("Video",img)
        cv2.waitKey(1)

