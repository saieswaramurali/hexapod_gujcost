import rclpy 
from rclpy.node import Node 
from std_msgs.msg import String 

class SimplePublisher(Node) : 
    
    def __init__(self) :
        super().__init__("Simple_publisher") 

        self.pub_ = self.create_publisher(String, 'chatter', 10)

        self.counter = 0 
        self.frequency_ = 1.0

        self.get_logger().info("the message is publishing at %d Hz" % self.frequency_)

        self.timer_ = self.create_timer(self.frequency_, self.timerCallback) 

    
    def timerCallback(self) : 
        msg = String()
        msg.data = "hello im publishing in ROS2 for %d " % self.counter 
        self.pub_.publish(msg)
        self.counter = self.counter + 1 


    
def main() : 
    rclpy.init()
    simplepublisher = SimplePublisher()
    rclpy.spin(simplepublisher)
    simplepublisher.destroy_node()
    rclpy.shutdown()



if __name__ == "__main__" : 
    main()