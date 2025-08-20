#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import math


class SpringMover(Node):
    def __init__(self):
        super().__init__('spring_mover')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.timer = self.create_timer(0.05, self.move_spring)
        self.time = 0.0
        self.angular_speed = 3.0

    def move_spring(self):
        msg = Twist()
        angle = self.time * self.angular_speed
        if int(angle / math.pi) % 2 == 0:
            msg.linear.x = 3.0
        else:
            msg.linear.x = 0.5
        msg.angular.z = self.angular_speed
        self.publisher_.publish(msg)
        self.time += 0.05


def main(args=None):
    rclpy.init(args=args)
    node = SpringMover()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

