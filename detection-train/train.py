from ultralytics import YOLO

# 加载模型
import sys
sys.path.append("/home/industai/code_folder/Python_code/gitlab_project/ultralytics/detection-train")
model = YOLO('yolov8l.yaml').load('yolov8l.pt')  # 从YAML构建并转移权重

# 训练模型
results = model.train(data='/home/industai/code_folder/Python_code/gitlab_project/ultralytics/detection-train/gwbs.yaml', 
                      epochs=100, imgsz=640,batch=16,device=1,close_mosaic=0,rect=False)