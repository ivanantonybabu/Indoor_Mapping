import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/ivan-antony-babu/Indoor_Mapping/ros2_ws/install/my_first_package'
