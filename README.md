# DTSH: Digital Twin (DT) Driven Smart Home

A proof of concept of a DT-driven smart home powered by several packages from ROS and Gazebo. It includes aspects of 3D representation, robot navigation, and semantics.

## How the smart home model is created in Gazebo?
The steps of the creation of a smart home model are defined as follows. 
The smart home is scanned using a hand-held RGB-D camera and a SLAM algorithm (RTAB-Map) to build a 3D reconstruction of it. 
A modeling software (Blender) is used to construct the CAD models of the home and objects inside it from the scan. The CAD models (augmented with different properties, for example, being static or movable) are imported into a robotic simulator (Gazebo). <!-- A TurtleBot model in URDF format is spawn into the simulator. --> A proof-of-concept is developed (using YOLO-v3 and Darknet ROS 3D) to enable semantic understanding of objects. A TurtleBot model in URDF format is spawn into the simulator.

![picture2](https://github.com/alirezaasvadi/DTSH/blob/main/2022-05-05%2016-07-33.png)

## The smart home file <!-- roslaunch turtlebot_gazebo my_turtlebot_world.launch -->
To start the simulated smart home you need to run `smart_home.launch`. It will launch Gazebo with the smart home model (`simple_world_v2.world`) and a Turtlebot model. The smart home file is in WORLD format.<!-- that can be directly read by Gazebo (it is `simple_world_v2.world` which will be loaded using the launch file). --> It consists of the address to all 3D CAD models of the elements/objects in the smart home (including wall, cabinet, chair, sofa, table, etc) with the associated properties (being movable or static, collision and visual properties, etc). The pose of objects are extracted from the reconstructed point cloud of the environment and using Blender.

<!--The output of the SLAM algorithm is a 3D point cloud (in ply format). It canbe denoised by pcdenoise function in MATLAB. It is inputted to Blender (if it is made of different rooms it can be aligned manually or semi-automatically using Align tool in Meshlab)
The smart home is composed of two main components: static parts (walls) and movable objects. -->

## A note on different file formats
Different file formats are required to build the smart home model including URDF, SDF, WORLD, and DAE.  
**URDF:** describes kinematics and dynamics of a robot (with some limitaions imposed from previous presumptions in ROS). It includes properties such as robot, sensor, transmissions, link, joint, model, etc.  
**SDF:** defined to solve the problems with URDF and can be used to describe both a robot and a world.  
**WORLD:** directly can be read by ROS or Gazebo. Similar to SDF but unlike SDF can't be reused/included in another file of the same type.  
**DAE:** called Collada format, and it is to represent a 3D CAD model (like as STL format).  
*The DAE files has no properties, they are required to be loaded in the SDF format and to be augmented with different properties such as collision, visual, world, scene, physics, light, actor, model, link, sensor, joint, material, geometry, etc. More information about SDF format in: http://sdformat.org/spec*



For more information please refer to the project page (https://sites.google.com/view/heron-project) and the associated publication:
