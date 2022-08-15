# Overview

This is a simulation of an autonomous ball-in-a-maze puzzle solution algorithm, designed as part of an overall system, using a combination of software and hardware. The system aims to sucessfully solve the puzzle by tilting the board and, hence, moving the ball through the maze, whilst avoiding any obstacles.

The system consists of the following components:

* The camera setup, ensuring high-quality live video could be taken from the puzzle
* The image processing algorithm, translating the image input into meaningful data, useful for the motor control algorithm
* The motor control algorithm, using the input from the image processing in every frame to determine the desirable motor angle to control the ball’s motion
* The motors attached to the puzzle board, programmed to respond to the motor control algorithm’s outputs
* The user interface, allowing the user to interact with the puzzle via a computer application

<p align = "center">
    <img src="https://github.com/alexandrosfloros/Rolling-Ball-Control/blob/main/system_flowchart.png">
</p>

# How to Use

## Execution

The file used to run the project is ``testbench.py``.

## Defining the Topology

The discrete solution path consisting of the nodes as well as holes of the puzzle can be specified as Cartesian co-ordinates in ``testbench.py`` via the respective lists.
