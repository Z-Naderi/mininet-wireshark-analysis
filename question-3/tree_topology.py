from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink

class TreeTopo(Topo):
    def build(self):
        info('*** Creating tree topology\n')
       
        rootSwitch = self.addSwitch('s1')
        leftSwitch = self.addSwitch('s2')
        rightSwitch = self.addSwitch('s3')

   
        self.addLink(rootSwitch, leftSwitch)
        self.addLink(rootSwitch, rightSwitch)

        
        for i in range(1, 3):
            host = self.addHost(f'h{i}')
            self.addLink(host, leftSwitch)

        for i in range(3, 5):
            host = self.addHost(f'h{i}')
            self.addLink(host, rightSwitch)

def run():
    setLogLevel('info') 
    info('*** Creating network\n')
    topo = TreeTopo()
    net = Mininet(topo=topo, link=TCLink)
    info('*** Starting network\n')
    net.start()
    info('*** Running CLI\n')
    CLI(net)
    info('*** Stopping network\n')
    net.stop()

if __name__ == '__main__':
    run()

