import os
import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, QoSDurabilityPolicy, QoSHistoryPolicy, QoSReliabilityPolicy, QoSLivelinessPolicy
from urinterfaces.msg import SafetyStatus
from urinterfaces.srv import SetDigitalOutput

class AdvancedROS2Node(Node):
    def __init__(self):
        self.namespace = os.getenv('ROS2_NAMESPACE')
        super().__init__('advanced_ros2', namespace=self.namespace)

        self.qos_profile = QoSProfile(
            depth=1,
            history=QoSHistoryPolicy.KEEP_LAST,
            liveliness=QoSLivelinessPolicy.AUTOMATIC,
            reliability=QoSReliabilityPolicy.BEST_EFFORT,
            durability=QoSDurabilityPolicy.VOLATILE
        )

        self.subscription = self.create_subscription(
            SafetyStatus,
            'safety_status',
            self.safety_status_callback,
            self.qos_profile
        )

        self.client = self.create_client(SetDigitalOutput, 'set_standard_digital_output')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info(f'Robot Controller ({self.namespace}) not accessible, waiting again...')
        self.get_logger().info(f'Using Robot Controller: {self.namespace}')

        self.previous_safety_status = None

    def safety_status_callback(self, msg):
        self.get_logger().info(f'Received safety status: {msg.data}')

        if self.previous_safety_status != msg.data:
            self.get_logger().info(f'Safety status changed from {self.previous_safety_status} to {msg.data}')
            self.previous_safety_status = msg.data

        if msg.data == 3:
            self.get_logger().info('Detected PROTECTIVE_STOP, setting Digital Output 5 to High')
            req = SetDigitalOutput.Request()
            req.pin = 5
            req.state = True
            self.client.call_async(req)

def main(args=None):
    rclpy.init(args=args)
    advanced_ros2_node = AdvancedROS2Node()
    advanced_ros2_node.get_logger().info('ROS2 Node started')

    try:
        rclpy.spin(advanced_ros2_node)
        advanced_ros2_node.get_logger().info(f'Node spinning.')
    except KeyboardInterrupt:
        advanced_ros2_node.get_logger().info('Ctrl-C detected, shutting down')
    finally:
        advanced_ros2_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
