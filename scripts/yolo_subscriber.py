import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
import torch
import cv2
import numpy as np
from ultralytics import YOLO

class YOLOSubscriber(Node):

    def __init__(self):
        super().__init__('yolo_subscriber')
        
        # Load the YOLOv8 model directly
        self.model = YOLO('/home/mayuresh/ros2_ws/src/video_detection/best.pt')  # Path to your custom model
        
        self.subscription = self.create_subscription(
            Image,
            'video_frames',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        
        # Create a named window that is resizable
        cv2.namedWindow("YOLO Detection", cv2.WINDOW_NORMAL)

    def listener_callback(self, msg):
        # Convert ROS Image message to OpenCV image
        frame = self.convert_ros_image_to_cv2(msg)

        # Run YOLOv8 model on the frame
        results = self.model(frame)

        # Annotate frame
        annotated_frame = results[0].plot()  # Use .plot() to annotate the frame with bounding boxes
        
        # Show annotated frame
        cv2.imshow('YOLO Detection', annotated_frame)
        # Add the ability to resize the window manually
        cv2.resizeWindow("YOLO Detection", 800, 600)  # Set an initial size (optional)
        cv2.waitKey(1)

    def convert_ros_image_to_cv2(self, msg):
        # Convert ROS image message to OpenCV format
        height = msg.height
        width = msg.width
        img_data = np.array(msg.data, dtype=np.uint8).reshape(height, width, 3)
        return img_data


def main(args=None):
    rclpy.init(args=args)

    node = YOLOSubscriber()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
