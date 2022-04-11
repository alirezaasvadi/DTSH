# DTSH: Digital Twin (DT) Driven Smart Home

A proof of concept of a DT-driven smart home powered by several packages from ROS and Gazebo. It includes aspects of 3D representation, robot navigation, and semantics.

## How the smart home model is created in Gazebo?
The steps of DT creation are defined as follows. 
The smart home is scanned using a hand-held RGB-D camera and a SLAM algorithm to build a 3D reconstruction of it. 
A modeling software is used to construct the CAD models of the home and objects inside it from the scan. The CAD models (augmented with different properties, for example, being static or movable) are imported into a robotic simulator (Gazebo). 
A TurtleBot model in URDF format is spawn into the simulator.
A proof-of-concept is developed to enable semantic understanding of objects. 

