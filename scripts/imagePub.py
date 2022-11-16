#!/usr/bin/env python
from __future__ import print_function

import os
import rospy
import cv2
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
import urllib
import numpy as np
import logging
logging.basicConfig()

def imagePub():
    req = urllib.urlopen('https://upload.wikimedia.org/wikipedia/zh/3/34/Lenna.jpg')
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    image = cv2.imdecode(arr, -1) # 'Load it as it is'

    bridge = CvBridge()
    pub = rospy.Publisher('image_topic', Image, queue_size=10)
    rospy.init_node('imagePub', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():
        try:
            pub.publish(bridge.cv2_to_imgmsg(image, "bgr8"))
        except CvBridgeError as e:
            print(e)
        rate.sleep()

if __name__ == '__main__':
    try:
        imagePub()
    except rospy.ROSInterruptException:
        print("node imagePub launch failed")
        pass