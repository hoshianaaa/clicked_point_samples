#!/usr/bin/env python
import rospy
from geometry_msgs.msg import PointStamped

def callback(data):
  print(data)
    
def listener():

  rospy.init_node('click_point_sub', anonymous=True)

  rospy.Subscriber("clicked_point", PointStamped, callback)

  rospy.spin()
      
if __name__ == '__main__':
    listener()
