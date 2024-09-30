import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge

class CameraNode(Node):
    def __init__(self):
        super().__init__('camera_node')
        self.publisher_ = self.create_publisher(Image, 'camera_data', 10)
        self.cap = cv2.VideoCapture(0)
        self.bridge = CvBridge()
        self.timer = self.create_timer(0.1, self.publish_image)

    def publish_image(self):
        ret, frame = self.cap.read()
        if ret:
            msg = self.bridge.cv2_to_imgmsg(frame, "bgr8")
            self.publisher_.publish(msg)
            self.get_logger().info('Published image frame')

def main(args=None):
    rclpy.init(args=args)
    camera_node = CameraNode()
    rclpy.spin(camera_node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
