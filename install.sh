#!bin/bash 

## Installation for Mobile robot tutorial
sudo apt-get install -y ros-melodic-joy ros-melodic-teleop-twist-joy \
      ros-melodic-teleop-twist-keyboard ros-melodic-laser-proc \
      ros-melodic-rgbd-launch ros-melodic-depthimage-to-laserscan \
      ros-melodic-rosserial-arduino ros-melodic-rosserial-python \
      ros-melodic-rosserial-server ros-melodic-rosserial-client \
      ros-melodic-rosserial-msgs ros-melodic-amcl ros-melodic-map-server \
      ros-melodic-move-base ros-melodic-urdf ros-melodic-xacro \
      ros-melodic-compressed-image-transport ros-melodic-rqt* \
      ros-melodic-gmapping ros-melodic-navigation ros-melodic-interactive-markers


sudo apt-get install -y ros-melodic-dynamixel-sdk \
                        ros-melodic-turtlebot3-msgs \
                        ros-melodic-turtlebot3

cd ~/catkin_ws/src && git clone https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git


## Installation for Manipulator tutorial
sudo apt-get install -y ros-melodic-moveit \
                        ros-melodic-industrial-core \
                        ros-melodic-moveit-visual-tools \
                        ros-melodic-joint-state-publisher-gui


sudo apt-get install -y ros-melodic-gazebo-ros-pkgs \
                        ros-melodic-gazebo-ros-control \
                        ros-melodic-joint-state-controller \
                        ros-melodic-effort-controllers \
                        ros-melodic-position-controllers \
                        ros-melodic-joint-trajectory-controller

cd ~/catkin_ws/src && git clone -b release-2.3 https://github.com/neuromeka-robotics/indy-ros
cd ~/catkin_ws/src && git clone https://github.com/neuromeka-robotics/indy-ros-examples

cd ~/catkin_ws && catkin_make
echo "export TURTLEBOT3_MODEL=waffle_pi" >> ~/.bashrc
