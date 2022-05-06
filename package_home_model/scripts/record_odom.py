#! /usr/bin/python
# record odometry information from the simulated turtlebot
# the result is recorded in :~/.ros/record.txt or in home:~/ 

import rospy
from nav_msgs.msg import Odometry

f = open("record.txt", "w")  
f.write("x y\n")
#f.close()

def callback(msg):
    x, y = msg.pose.pose.position.x, msg.pose.pose.position.y
    s = str(x) + " " + str(y)
    print(s)
    f.write(s + "\n")

rospy.init_node("record_odometry")
odom_sub = rospy.Subscriber("/odom", Odometry, callback)

rospy.spin() 
