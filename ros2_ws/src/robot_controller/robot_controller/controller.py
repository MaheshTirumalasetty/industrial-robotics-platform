import json

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class RobotController(Node):
    def __init__(self) -> None:
        super().__init__("robot_controller")
        self.subscription = self.create_subscription(
            String,
            "manufacturing/sensor_data",
            self.process_sensor_data,
            10,
        )

    def process_sensor_data(self, message: String) -> None:
        try:
            payload = json.loads(message.data)
            temperature = float(payload["temperature_c"])
            pressure = float(payload["pressure_bar"])

            if temperature > 32.0 or pressure < 4.8:
                state = "DEGRADED"
            else:
                state = "OPERATIONAL"

            self.get_logger().info(
                f"Cell state={state}, temperature={temperature}, pressure={pressure}"
            )
        except (ValueError, KeyError, json.JSONDecodeError) as exc:
            self.get_logger().error(f"Invalid sensor message: {exc}")


def main(args=None) -> None:
    rclpy.init(args=args)
    node = RobotController()
    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
