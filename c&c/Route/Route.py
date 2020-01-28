from IPv4Address.IPv4Address import IPv4Address
from Network.Network import Network


class Route:

    def __init__(self, network : Network, gateway : IPv4Address, interface : str, metric : int):
        self.network = network
        self.gateway = gateway
        self.interface = interface
        self.metric = metric

    def get_gateway(self) -> IPv4Address:
        return self.gateway

    def get_interface_name(self) -> str:
        return self.interface

    def get_metric(self) -> int:
        return self.metric

    def get_network(self) -> Network:
        return self.network

    def __str__(self):
        out = [f" net: {self.network},", f" interface: {self.interface}," f" metric: {self.metric}"]
        if self.gateway is not None:
            out.insert(1, f" gateway: {self.gateway},")
        return "".join(out)


if __name__ == "__main__":
    net = Network("192.168.1.0", 24)
    route = Route(network=net, gateway=None, interface="en0", metric=10)
    route2 = Route(Network("0.0.0.0", 0), gateway=IPv4Address("192.168.0.1"), interface="en0", metric=10)
    print(route)
    print(route2)


# net: 192.168.0.0/24, interface: en0, metric: 10
# net: 0.0.0.0/0, gateway: 192.168.0.1, interface: en0, metric: 10


# class Route {
#   public Route(Network network, IPv4Address gateway, String interfaceName, int metric) {}
#   public IPv4Address getGateway() {}
#   public String getInterfaceName() {}
#   public int getMetric() {}
#   public Network getNetwork() {}
#   public String toString() {}
# }

# Route route = router.getRouteForAddress(new IPv4Address("192.168.0.176"));
# route.getMetric();                  // 10
# route.getInterfaceName();           // en0
# Network net = route.getNetwork();
# net.toString();                     // 192.168.0.0/24
# net.getAddress().toString();        // 192.168.0.0
