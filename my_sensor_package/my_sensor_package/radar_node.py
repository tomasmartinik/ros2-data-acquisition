import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Range
import random

class RadarNode(Node):
    def __init__(self):
        super().__init__('radar_node')
        self.publisher_ = self.create_publisher(Range, 'radar_data', 10)
        self.timer = self.create_timer(1.0, self.publish_data)

    def publish_data(self):
        msg = Range()
        msg.range = random.uniform(0.0, 10.0)  # Simulovaná data radaru
        self.publisher_.publish(msg)
        self.get_logger().info(f'Radar data: {msg.range}')

def main(args=None):
    rclpy.init(args=args)
    radar_node = RadarNode()
    rclpy.spin(radar_node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
