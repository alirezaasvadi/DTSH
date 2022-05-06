#! /usr/bin/python
# turtlebot/turtlesim

import rospy
from geometry_msgs.msg import Twist

rospy.init_node("turtle_move")

#pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=1) # turtlesim
#pub = rospy.Publisher('/cmd_vel_mux/input/navi', Twist, queue_size=1) # turtlebot
pub = rospy.Publisher('/mobile_base/commands/velocity', Twist, queue_size=1) # turtlebot simulation

# Create a Twist message and add linear x and angular z values
move = Twist()
move.linear.x = 0.25 
move.angular.z = -0.1 

# Save current time and set publish rate at 10 Hz
now = rospy.Time.now()
rate = rospy.Rate(10) #orginal

# For the next 4 seconds publish cmd_vel move commands to Turtlesim
while rospy.Time.now() < (now + rospy.Duration.from_sec(4)): #org 
    pub.publish(move)
    rate.sleep()

