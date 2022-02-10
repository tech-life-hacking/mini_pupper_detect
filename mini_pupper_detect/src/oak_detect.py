#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from depthai_ros_msgs.msg import SpatialDetectionArray

twist = Twist()

#yolov4 object list
#0: person
#1: bicycle
#2: car
#3: motorbike
#4: aeroplane
#5: bus
#6: train
#7: truck
#8: boat
#9: traffic light
#10: fire hydrant
#11: stop sign
#12: parking meter
#13: bench
#14: bird
#15: cat
#16: dog
#17: horse
#18: sheep
#19: cow
#20: elephant
#21: bear
#22: zebra
#23: giraffe
#24: backpack
#25: umbrella
#26: handbag
#27: tie
#28: suitcase
#29: frisbee
#30: skis
#31: snowboard
#32: sports ball
#33: kite
#34: baseball bat
#35: baseball glove
#36: skateboard
#37: surfboard
#38: tennis racket
#39: bottle
#40: wine glass
#41: cup
#42: fork
#43: knife
#44: spoon
#45: bowl
#46: banana
#47: apple
#48: sandwich
#49: orange
#50: broccoli
#51: carrot
#52: hot dog
#53: pizza
#54: donut
#55: cake
#56: chair
#57: sofa
#58: pottedplant
#59: bed
#60: diningtable
#61: toilet
#62: tvmonitor
#63: laptop
#64: mouse
#65: remote
#66: keyboard
#67: cell phone
#68: microwave
#69: oven
#70: toaster
#71: sink
#72: refrigerator
#73: book
#74: clock
#75: vase
#76: scissors
#77: teddy bear
#78: hair drier
#79: toothbrush


def toward_obj(obj_class,obj_list):
    global twist
    rate = rospy.Rate(200) # 200hz
    for i in obj_list:
        bb = i.bbox #BoundingBoxes
        pz = i.position.z #position.z
        r = i.results #Results
        rr = r[0] #RealResults
        if(rr.id == obj_class):
            if pz > 0.5:
                variation = 0.5
            else:
                variation = -0.5

            twist.linear.x = variation

            pub_twist.publish(twist)
    rate.sleep()

def callback(data):
    bounding_boxes = data
    detections = bounding_boxes.detections
    toward_obj(39,detections)

def listener():
    rospy.init_node('yolo_detect', anonymous=True)
    rospy.Subscriber("/yolov4_publisher/color/yolov4_Spatial_detections", SpatialDetectionArray, callback)
    rospy.spin()

if __name__ == '__main__':
    pub_twist = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    listener()