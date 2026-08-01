import json
import random

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class SensorPublisher(Node):
    def __init__(self) -> None:
        super().__init__("sensor_publisher")
        self.publisher = self.create_publisher(String, "manufacturing/sensor_data", 10)
        self.timer = self.create_timer(1.0, self.publish_sensor_data)

    def publish_sensor_data(self) -> None:
        payload = {
            "temperature_c": round(random.uniform(20.0, 35.0), 2),
            "pressure_bar": round(random.uniform(4.5, 6.0), 2),
            "machine_state": "RUNNING",
        }
        message = String()
        message.data = json.dumps(payload)
        self.publisher.publish(message)
        self.get_logger().info(f"Published sensor data: {message.data}")


def main(args=None) -> None:
    rclpy.init(args=args)
    node = SensorPublisher()
    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
