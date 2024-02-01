from ultralytics import YOLO

# 加载模型
model = YOLO('/media/industai/DATA1/game_model/tcbj/四川思极_1211/detect/28类/best.pt')  # 加载自定义模型

# 验证模型
metrics = model.val(data="/home/industai/code_folder/Python_code/gitlab_project/ultralytics/detection-train/gwbs.yaml")  # 无需参数，数据集和设置记忆
metrics.box.maps   # 包含每个类别的map50-95列表