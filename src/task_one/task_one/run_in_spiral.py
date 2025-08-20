#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class SpiralMover(Node):
    def __init__(self):
        super().__init__('spiral_mover')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.linear_vel=1.0
        self.timer = self.create_timer(0.5, self.move_spiral)

    def move_spiral(self):
        msg = Twist()
        msg.linear.x = self.linear_vel  
        msg.angular.z = 1.0 
        self.linear_vel+=0.1
        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = SpiralMover()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

