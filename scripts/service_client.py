#!/usr/bin/env python

import rospy
from ros_tutorial.srv import MySrvFile

rospy.wait_for_service('a_topic')
try:
    send_hi = rospy.ServiceProxy('a_topic', MySrvFile)
    print('Client: Hi, do you hear me?')
    resp = send_hi('Hi, do you hear me?')
    print("Server: {}".format(resp.response))

except rospy.ServiceException, e:
    print "Service call failed: %s"%e

