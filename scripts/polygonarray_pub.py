import rospy
from jsk_recognition_msgs.msg import PolygonArray
from geometry_msgs.msg import Polygon, PolygonStamped, Point32

msg = PolygonArray()

p1 = PolygonStamped()
p1.header.frame_id = "map"
p1.polygon.points = [Point32(x=10, y=10, z=0),
                     Point32(x=10, y=-10, z=0),
                     Point32(x=-10, y=-10, z=0),
                     Point32(x=-10, y=10, z=0)
                     ]


msg.polygons = [p1]

pub = rospy.Publisher('p_array', PolygonArray, queue_size=1)
rospy.init_node('pub')
r = rospy.Rate(1)
msg.header.frame_id = "map"
while not rospy.is_shutdown():
  pub.publish(msg)
  print("publish!")
  r.sleep()
