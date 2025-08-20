#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class CircularMover(Node):
    def __init__(self):
        super().__init__('circle_mover')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.timer = self.create_timer(0.5, self.move_circle)

    def move_circle(self):
        msg = Twist()
        msg.linear.x = 1.0  
        msg.angular.z = 1.0 
        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = CircularMover()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

