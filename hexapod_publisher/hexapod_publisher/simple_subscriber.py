import rclpy 
from rclpy.node import Node
from std_msgs.msg import String 

class simpleSubscriber(Node) : 

    def __init__(self) : 
        super().__init__('simple_subscriber') 

        self.sub_ = self.create_subscription(String, 'chatter', self.msgCallback,  10)
        self.get_logger().info("Subscriber node has been started.")


    def msgCallback(self, msg) : 
        self.get_logger().info("the msg is %s " %msg.data)



def main() : 
    rclpy.init()
    simple_subscriber = simpleSubscriber()
    rclpy.spin(simple_subscriber)
    simple_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__" : 
    main()
