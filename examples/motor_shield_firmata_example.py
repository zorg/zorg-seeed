import zorg
import time

def work(robot):

    # Set the speed of both motors
    robot.motor_shield.set_right_motor_speed(200)
    robot.motor_shield.set_left_motor_speed(200)

    robot.motor_shield.set_right_motor_direction(0)

    time.sleep(2)

    robot.motor_shield.set_right_motor_direction(1)

    time.sleep(2)

    # Stop the right side motor
    robot.motor_shield.set_right_motor_direction(-1)

    robot.motor_shield.set_left_motor_direction(1)

    time.sleep(2)

    robot.motor_shield.set_left_motor_direction(0)

    time.sleep(2)

    # Stop the left motor
    robot.motor_shield.set_left_motor_direction(-1)
    
    
robot = zorg.robot({
    'connections': {
        'firmata': {
            'adaptor': 'zorg_firmata.Firmata',
            'port': '/dev/ttyACM0'
        },
    },
    'devices': {
        'motor_shield': {
            'connection': 'firmata',
            'driver': 'zorg_seeed.MotorShield'
        }
    },
    'name': 'example', # Give your robot a unique name
    'work': work, # The method (on the main level) where the work will be done
})

robot.start()
