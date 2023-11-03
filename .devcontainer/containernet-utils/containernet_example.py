#!/usr/bin/python
"""
This is the most simple example to showcase Containernet.
"""
from node_ext import DynamicDocker
from mininet.net import Containernet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.log import info, setLogLevel
setLogLevel('info')

net = Containernet(controller=Controller)
info('*** Adding controller\n')
net.addController('c0')
info('*** Adding docker containers\n')
d1 = net.addHost('rucio', ip='10.0.0.250', cls=DynamicDocker)
d2 = net.addHost('xrd1', ip='10.0.0.251', cls=DynamicDocker)
d3 = net.addHost('xrd2', ip='10.0.0.252', cls=DynamicDocker)
info('*** Adding switches\n')
s1 = net.addSwitch('s1')
s2 = net.addSwitch('s2')
info('*** Creating links\n')
net.addLink(d1, s1)
net.addLink(s1, s2, cls=TCLink, delay='100ms', bw=1)
net.addLink(s2, d2)
net.addLink(s2, d3)
info('*** Starting network\n')
net.start()
info('*** Testing connectivity\n')
net.ping([d1, d2, d3])
info('*** Running CLI\n')
CLI(net)
info('*** Stopping network')
net.stop()
