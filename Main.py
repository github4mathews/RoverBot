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
# import Video

if __name__ == "__main__":
    robot = RobotHandler()



    robot.setMoveRadius(-200, 100)
    print("Final: ", robot.LWheel.encoder.getVelocity(sampleSize=50))
    sleep(10)

    robot.close()
