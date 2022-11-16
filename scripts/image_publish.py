#!/usr/bin/env python
from __future__ import print_function

import sys
import os
import rospy
import cv2
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
import urllib
import numpy as np
import logging
logging.basicConfig()

class ImagePublisher:

    def __init__(self):
        self.pub = rospy.Publisher('image_topic', Image, queue_size=10)
        rospy.init_node('image_publish', anonymous=True)
        self.bridge = CvBridge()
        self.rate = rospy.Rate(10) # 10hz
    
    def readImage(self):
        req = urllib.urlopen('https://upload.wikimedia.org/wikipedia/zh/3/34/Lenna.jpg')
        arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
        image = cv2.imdecode(arr, -1) # 'Load it as it is'
        return image
    
    def readImageByPath(image_path, self):
        if not os.access(image_path, os.R_OK):
            rospy.logerr("Cannot read file at '{0}'".format(image_path))
            return None
        image = cv2.imread(image_path)
        return image

    def publishImage(image, self):
        while not rospy.is_shutdown():
            try:
                self.pub.publish(self.bridge.cv2_to_imgmsg(image, "bgr8"))
            except CvBridgeError as e:
                print(e)
            self.rate.sleep()

def main(args):
    ip = ImagePublisher()
    image = ip.readImage()
    ip.publishImage(image)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")
    
if __name__ == '__main__':
    main(sys.argv)