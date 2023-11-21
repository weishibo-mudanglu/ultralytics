import cv2
import numpy as np
size_f = open("0.mmeta",'r')
size_str = size_f.read()
size_list = size_str.split(",")
size_list = [int(x) for x in size_list]
half = int(len(size_list)/2)


#print(size_list)

label_f = open("0.mlabel",'r')
label_str = label_f.read()
offset = 0
for item in size_list[half:]:
    label_item = label_str[offset:offset+item]
    offset += item
    label_object = eval(label_item)
    print("==== label_object:{}".format(label_object))

img_f = open("0.mblob",'rb')
img_data = img_f.read()

offset = 0
for item in size_list[:half]:
    label_item = img_data[offset:offset+item]
    offset += item
    label_object = cv2.imdecode(np.frombuffer(label_item,dtype=np.uint8),cv2.IMREAD_COLOR)
    
