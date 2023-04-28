# RIoT: Reinforced IoT
A Security solution for IoT devices.


IoT devices because of their lack of processing power and storage capabilities, running an anti-virus or any other forms of protection for such devices is very difficult. RIoT aims to solve this problem by having a system which monitors all the packets in the IoT network and by using a machine learning model on the observed packets, determine whether something is off.

The dataset used to train the model is created by capuring all the packets involved in IoT system which is deliberately attacked, labelling them and running these packet capture files(.pcap files) through a program called zeek to finally get a transactional log file to which additional two coloumns are added which denote whether these were part of an attack or not.
