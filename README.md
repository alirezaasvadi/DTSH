# DTSH: Digital Twin (DT) Driven Smart Home

A proof of concept of a DT-driven smart home powered by several packages from ROS and Gazebo. It includes aspects of 3D representation, robot navigation, and semantics.

The steps of DT creation are defined as follows. 
The smart home is scanned using a hand-held RGB-D camera and a SLAM algorithm to build a 3D reconstruction of it. 
A modeling software is used to construct the CAD models of the home and objects inside it from the scan. The CAD models (augmented with different properties, for example, being static or movable) and a robot model are imported into a robotic simulator. 
A robot model is spawned
To represent a robot, the TurtleBot model in \textit{Unified Robot Description Format (URDF)} is spawn and imported into a robotic simulator (in Gazebo).

A proof-of-concept is developed to enable semantic understanding of objects. A set of experiments were performed to compare a Turtlebot's behavior (such as traversed trajectories and the generated 2D maps) in the actual and simulated DT environments. F


