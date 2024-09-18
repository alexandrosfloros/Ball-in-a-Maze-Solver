# Overview

This is a simulation of an autonomous ball-in-a-maze puzzle solution algorithm, designed as part of a complete system using a combination of hardware and software. The system aims to sucessfully solve the puzzle by tilting the board and moving the ball through the maze, while avoiding any obstacles.

The system consists of the following components:

* The camera setup, ensuring high-quality live video could be taken from the puzzle
* The image processing algorithm, translating the image input into meaningful data, useful for the motor control algorithm
* The motor control algorithm, using the input from the image processing in every frame to determine the desirable motor angle to control the ball's motion
* The motors attached to the puzzle board, programmed to respond to the motor control algorithm's outputs
* The user interface, allowing the user to interact with the puzzle via a computer application

# How to Use

The file used to run the project is ``testbench.py``. The discrete solution path, consisting of the nodes as well as holes of the puzzle, can be specified in Cartesian coordinates via the respective lists.
