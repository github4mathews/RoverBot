"""
Project Brainstorming

Hardware:
    - PWM 

Goals:
    Track lines using vision and map the nodes as it moves along
        - Move (Wheels)
        - Measure Distance (encoders)
        - Video Feed
        - Computer Vision
        -
"""

from Robot import RobotHandler
from time import sleep

if __name__ == "__main__":
    robot = RobotHandler()

    robot.setSpeed(10)
    sleep(1)
    robot.setSpeed(0)
    sleep(.25)
    robot.setSpeed(-10)
    sleep(1)


    robot.close()
