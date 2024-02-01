from ultralytics import YOLO
import sys
sys.path.append("/home/industai/code_folder/Python_code/gitlab_project/ultralytics/detection-train")
# 加载模型
model = YOLO('yolov8n-cls.yaml').load('/home/industai/code_folder/Python_code/gitlab_project/ultralytics/classify-train/yolov8n-cls.pt')  # 从YAML构建并转移权重

# 训练模型
results = model.train(data='/home/industai/datasets/北京训练验证/分类训练数据', epochs=100, imgsz=640,batch=4,device=0,val=False)