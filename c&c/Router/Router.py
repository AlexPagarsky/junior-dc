from IPv4Address import IPv4Address
from Network import Network
from Route import Route
from typing import Iterable, List


class Router:

    def __init__(self, routes: Iterable[Route]):
        self.routes = list(routes)

    def add_route(self, route : Route) -> None:
        self.routes.append(route)

    def get_route_for(self, address : IPv4Address) -> Route:
        for route in sorted(self.routes, key=(lambda route: route.network.mask), reverse=True):
            if address in route.network:
                return route
        raise Exception("No route found")

    def get_routes(self) -> List[Route]:
        return self.routes

    def remove_route(self, route : Route) -> None:
        try:
            self.routes.remove(route)
        except ValueError:
            pass


if __name__ == "__main__":
    routes = [
        Route(Network(IPv4Address("0.0.0.0"), 0), "192.168.0.1", "en0", 10),
        Route(Network(IPv4Address("192.168.0.0"), 24), None, "en0", 10),
        Route(Network(IPv4Address("10.0.0.0"), 8), "10.123.0.1", "en1", 10),
        Route(Network(IPv4Address("10.123.0.0"), 20), None, "en1", 10)
    ]

    router = Router(routes)
    print("Route for 192.168.0.176 is ", route := router.get_route_for(IPv4Address("192.168.0.176")))
    print(route.get_metric())
    print(route.get_interface_name())
    net = route.get_network()
    print(net)
    print(net.address)

    route = router.get_route_for(IPv4Address("10.0.1.1"))
    print(route.get_metric())
    print(route.get_interface_name())
    net = route.get_network()
    print(net)

#
# List<Route> routes = new ArrayList<Route>() {{
#    add(new Route(new Network(new IPv4Address("0.0.0.0"), 0), "192.168.0.1", "en0", 10));
#    add(new Route(new Network(new IPv4Address("192.168.0.0"), 24), null, "en0", 10));
#    add(new Route(new Network(new IPv4Address("10.0.0.0"), 8), "10.123.0.1", "en1", 10));
#    add(new Route(new Network(new IPv4Address("10.123.0.0"), 20), null, "en1", 10));
# }};
#
# Router router = new Router(routes);
#
# Route route = router.getRouteForAddress(new IPv4Address("192.168.0.176"));
# route.getMetric();                  // 10
# route.getInterfaceName();           // en0
# Network net = route.getNetwork();
# net.toString();                     // 192.168.0.0/24
# net.getAddress().toString();        // 192.168.0.0
#
# route = router.getRouteForAddress(new IPv4Address("10.0.1.1"));
# route.getMetric();                  // 10
# route.getInterfaceName();           // en1
# net = route.getNetwork();
# net.toString();                     // 10.0.0.0/8
#
#
# for ( Route route : router.getRoutes() ) {
#    Network net = route.getNetwork();
#    // other important operations
# }

# class Router {
#   public Router(Iterable<Route> routes) {}
#   public void addRoute(Route route) {}
#   public Route getRouteForAddress(IPv4Address address) {}
#   public Iterable<Route> getRoutes() {}
#   public void removeRoute(Route route) {}
# }
