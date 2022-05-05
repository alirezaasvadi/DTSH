# DTSH: Digital Twin (DT) Driven Smart Home

A proof of concept of a DT-driven smart home powered by several packages from ROS and Gazebo. It includes aspects of 3D representation, robot navigation, and semantics.

## How the smart home model is created in Gazebo?
The steps of the creation of a smart home model are defined as follows. 
The smart home is scanned using a hand-held RGB-D camera and a SLAM algorithm (RTAB-Map) to build a 3D reconstruction of it. 
A modeling software (Blender) is used to construct the CAD models of the home and objects inside it from the scan. The CAD models (augmented with different properties, for example, being static or movable) are imported into a robotic simulator (Gazebo). <!-- A TurtleBot model in URDF format is spawn into the simulator. --> A proof-of-concept is developed (using YOLO-v3 and Darknet ROS 3D) to enable semantic understanding of objects. A TurtleBot model in URDF format is spawn into the simulator.

![picture2](https://github.com/alirezaasvadi/DTSH/blob/main/2022-05-05%2016-07-33.png)

## The protocol for the creation of the smart home model

### Camera Calibration. 
The Orbbec Astra Pro sensor was used. 
The resolution for both the RGB and depth images was set to *640x480* pixels. The *camera_calibration* ROS package http://wiki.ros.org/camera_calibration was used for the intrinsic camera calibration.

### 3D Reconstruction. 
The *rtabmap_ros* package http://wiki.ros.org/rtabmap_ros was used to create the 3D map of the smart home. It outputs a dense 3D map of the environment in the form of point cloud data in *.PLY* or *.PCD* formats.
A simplified mesh can be generated using ball-pivoting surface reconstruction function of Meshlab http://www.meshlab.net. Another alternative is the marching cubes algorithm, at the cost of losing color data.

### CAD Model Creation. 
This step is to convert the obtained point cloud (or mesh) to object-level CAD models of the home items and home's frame.
Online public repositories (https://free3d.com, https://3dwarehouse.sketchup.com) were used to obtain the CAD models of home items. The models are modified in Blender (https://www.blender.org) to best represent (*i.e.*, to have the same shape and size) the physical objects.
They were created in *COLLADA (COLLAborative Design Activity)* format, *i.e.*, a set of *.DAE* files.

### Digital 3D Model.
Gazebo was used as the physics-based simulator. 
A digital 3D model is created in *SDFormat (Simulation Description Format)* (http://sdformat.org) format in a *.WORLD* file. 
It consists of the addresses to DAE files (*e.g.*, wall, cabinet, chair, sofa, table, etc) from the previous step. The DAE files (*i.e.*, the CAD models) were used to define the visual and collision properties of the objects and were augmented with other properties such as being static or movable, object pose, etc. For example, the home frame is static and is populated by movable objects (*e.g.*, chairs). The poses of objects were attained using Blender from previous step. The result in *.WORLD* file is the smart home model.

### Digital Model including a Robot.
A file in *.LAUNCH* format is required to start the Gazebo simulator with the created smart home model and a spawned Turtlebot model of *Unified Robot Description Format (URDF)*.
Therefore, the file comprises two sections: i) to launch the created *.WORLD* file, and ii) to launch Turtlebot components (base, sensors, etc).
This model was used in the paper for performing the experiments.


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
