# DTSH: Digital Twin (DT) Driven Smart Home

A proof of concept of a DT-driven smart home powered by several packages from ROS and Gazebo. It includes aspects of 3D representation, robot navigation, and semantics.

## How the smart home model is created in Gazebo?
The steps of the creation of a smart home model are defined as follows. 
The smart home is scanned using a hand-held RGB-D camera and a SLAM algorithm (RTAB-Map) to build a 3D reconstruction of it. 
A modeling software (Blender) is used to construct the CAD models of the home and objects inside it from the scan. The CAD models (augmented with different properties, for example, being static or movable) are imported into a robotic simulator (Gazebo). <!-- A TurtleBot model in URDF format is spawn into the simulator. --> A proof-of-concept is developed (using YOLO-v3 and Darknet ROS 3D) to enable semantic understanding of objects. 

## A note on different file formats
Different file formats are required to build the smat home model including URDF, SDF, WORLD, and DAE.  
URDF: describes kinematics and dynamics of a robot (with some limitaions imposed from previous presumptions in ROS). It includes properties such as robot, sensor, transmissions, link, joint, model, etc.  
SDF: defined to solve the problems with URDF and can be used to describe both a robot and a world.  
WORLD: directly can be read by ROS or Gazebo. Similar to SDF but unlike SDF can't be reused/included in another file of the same type.
DAE: called Collada format, and it is to represent a 3D model (like as STL format).  
*The DAE files has no properties, they are required to be loaded in the SDF format and to be augmented with different properties such as collision, visual, world, scene, physics, light, actor, model, link, sensor, joint, material, geometry, etc.*

