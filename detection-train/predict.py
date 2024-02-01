from ultralytics import YOLO
from pathlib import Path
import cv2
def getPath(targetDir, globStr, targetDirList=None):
    if targetDirList is None:
        targetDirList = list()

    childDirList = list(targetDir.iterdir())
    for childDir in childDirList:
        if childDir.is_dir():
            targetDirList = getPath(childDir, globStr, targetDirList)

    targetList = list(targetDir.glob(globStr))

    if len(targetList) > 0:
        targetDirList = targetDirList+targetList
        return targetDirList
    else:
        return targetDirList

imgDirList = [
    Path("/home/industai/datasets/北京训练验证/gdwDatasets/v1_v2/images"), #v1_v2
    Path("/home/industai/datasets/北京训练验证/gdwDatasets/v3/images"), #7207
    Path("/home/industai/datasets/北京训练验证/gdwDatasets/v4/images"), #v4 8427
    Path("/home/industai/datasets/北京训练验证/gdwDatasets/v5/images"), #v5
    Path("/home/industai/datasets/北京训练验证/gdwDatasets/v6/images"), #v6
    Path("/home/industai/datasets/北京训练验证/gdwDatasets/v7/images"),
    Path("/home/industai/datasets/北京训练验证/gdwDatasets/v8/images"),
    Path("/home/industai/datasets/北京训练验证/gdwDatasets/v9/images"),]

pathList = []
for idx,imgDir in enumerate(imgDirList):
    globStrList_pic = ['*.jpg', '*.jpeg','*.png']
    for globStr in globStrList_pic:
        pathList = pathList + getPath(imgDir, globStr)
# 加载模型
model = YOLO('/media/industai/DATA1/game_model/tcbj/四川思极_1211/detect/70类/best.pt')  # 预训练的 YOLOv8n 模型

# 在图片列表上运行批量推理

# 处理结果列表
for path in pathList:
    print("="*20)
    print(str(path))
    results = model.predict([str(path)],save=True,imgsz=640)  # 返回 Results 对象列表
    boxes = results[0].boxes  # 边界框输出的 Boxes 对象
    # img = cv2.imread(str(path))
    # label_path = str(path).replace("images","labels")
    # label_path = str(label_path).replace(str(label_path).split(".")[-1],"txt")
    # label = open(label_path,'r',encoding='utf-8')
    # for lineLabel in label.readline():
    #     x = float(lineLabel.split()[1])*img.shape[1]
    #     y = float(lineLabel.split()[2])*img.shape[0]
    #     w = float(lineLabel.split()[3])*img.shape[1]
    #     h = float(lineLabel.split()[4])*img.shape[0]
    #     cv2.rectangle(img,(x,y))
    print(f"{boxes}")