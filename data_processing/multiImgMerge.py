import cv2
import numpy
import os
from utils import *
from pathlib import Path
import random

imgDirList = [
              Path("/home/industai/datasets/北京训练验证/gdwDatasets/v1_v2/images"), #v1_v2
              Path("/home/industai/datasets/北京训练验证/gdwDatasets/v3/images"), #7207
              Path("/home/industai/datasets/北京训练验证/gdwDatasets/v4/images"), #v4 8427
              Path("/home/industai/datasets/北京训练验证/gdwDatasets/v5/images"), #v5
              Path("/home/industai/datasets/北京训练验证/gdwDatasets/v6/images"), #v6
              Path("/home/industai/datasets/北京训练验证/gdwDatasets/v7/images"),
              Path("/home/industai/datasets/北京训练验证/gdwDatasets/v8/images"),
              Path("/home/industai/datasets/北京训练验证/gdwDatasets/v9/images"),]
saveDir = "/home/industai/datasets/北京训练验证/gdwDatasets/mergeData/"
def imgSizeAndLabelZoom(img,label,outSize=(640,640)):
    H,W,_ = img.shape
    scale_w = outSize[1]/W
    scale_h = outSize[1]/H
    out_img = cv2.resize(img,outSize)
    out_label = list()
    for lineLabel in label:
        lineLabel = lineLabel.split(" ")
        cls = int(lineLabel[0])
        x = float(lineLabel[1])*scale_w
        y = float(lineLabel[2])*scale_h
        w = float(lineLabel[3])*scale_w
        h = float(lineLabel[4])*scale_h
        out_label.append([cls,x,y,w,h])
    return out_img,out_label
if __name__ == '__main__':
    pathList = []
    for idx,imgDir in enumerate(imgDirList):
        globStrList_pic = ['*.jpg', '*.jpeg','*.png']
        for globStr in globStrList_pic:
            pathList = pathList + getPath(imgDir, globStr)
    random.shuffle(pathList)
    for i in range(0,len(pathList),16):
        print(i/len(pathList))
        imgList = list()
        labelList = list()
        if i + 16 <len(pathList):
            for j in range(16):
                imgPathId=i+j
                imgPath = str(pathList[imgPathId])
                txtPath = imgPath.replace("images","labels")
                txtPath = txtPath[:txtPath.rfind(".")]+".txt"                      
                img = cv2.imread(imgPath)
                f_label = open(txtPath,"r",encoding='utf-8').readlines()
                img,f_label = imgSizeAndLabelZoom(img,f_label)
                imgList.append(img)
                labelList.append(f_label)
        else:
            for j in range(len(pathList)-i):
                imgPathId=i+j
                imgPath = str(pathList[imgPathId])
                txtPath = imgPath.replace("images","labels")
                txtPath = txtPath.replace(txtPath.split(".")[-1],"txt")                         
                img = cv2.imread(imgPath)
                f_label = open(txtPath,"r",encoding='utf-8').readlines()
                img,f_label = imgSizeAndLabelZoom(img,f_label)
                imgList.append(img)
                labelList.append(f_label)
        imgSizeList = list()
        mergeNumpy = None
        
        for img in imgList:
            imgCode = cv2.imencode(".jpg",img)
            imgSizeList.append(str(imgCode[1].size))
            if mergeNumpy is None:
                mergeNumpy = imgCode[1]
            else:
                mergeNumpy = numpy.concatenate((mergeNumpy,imgCode[1]),axis=0)
        
        labelSizeList = list()
        mergeLabel = "" 
        for label in labelList:
            labelStr = str(label)
            labelStrSize = len(labelStr)
            mergeLabel = mergeLabel + labelStr
            labelSizeList.append(str(labelStrSize))
        
        imgSizeList.extend(labelSizeList)
        dst_file = ",".join(imgSizeList)
        with open(saveDir +str(i)+".mmeta",'w',encoding="utf-8") as f:
            f.write(dst_file)
        with open(saveDir +str(i)+".mblob",'wb') as f:
            f.write(bytes(mergeNumpy))
        with open(saveDir +str(i)+".mlabel",'w',encoding="utf-8") as f:
            f.write(mergeLabel)


            


                
    
    