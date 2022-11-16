#!/usr/bin/env python

import rospy
from ros_tutorial.srv import MySrvFile, MySrvFileResponse


def callback_function(req):
    print(req)
    return MySrvFileResponse('Hello client, your message received.')


rospy.init_node('server')
rospy.Service('a_topic', MySrvFile, callback_function)
rospy.spin()
