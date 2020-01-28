from IPv4Address.IPv4Address import IPv4Address, IllegalArgumentException


class Network:

    def __init__(self, address: IPv4Address, mask: int):
        if isinstance(address, int) or isinstance(address, str):
            self.address = IPv4Address(address)
        elif isinstance(address, IPv4Address):
            self.address = address
        else:
            raise IllegalArgumentException("Cannot create Network without IP")
        self.mask = mask

    def __contains__(self, item: IPv4Address) -> bool:
        return self.address.body <= item.body <= self.address.body - 1 + (1 << (32 - self.mask))

    def get_address(self) -> IPv4Address:
        return self.address

    def get_broadcast_address(self) -> IPv4Address:
        return IPv4Address(self.address.body - 1 + (1 << (32 - self.mask)))

    def get_first_usable(self) -> IPv4Address:
        return IPv4Address(self.address.body + 1)

    def get_last_usable(self) -> IPv4Address:
        return IPv4Address(self.address.body - 2 + (1 << (32 - self.mask)))

    def get_mask_int(self) -> int:
        temp = (255 << 24) + (255 << 16) + (255 << 8) + 255
        temp -= (1 << (32 - self.mask)) - 1
        return temp

    def get_mask_str(self) -> str:  # 255.255.255.0
        temp = (255 << 24) + (255 << 16) + (255 << 8) + 255
        temp -= (1 << (32 - self.mask)) - 1
        return str(IPv4Address(temp))

    def get_mask_len(self) -> int:
        return self.mask

    def make_subnets(self) -> (IPv4Address, IPv4Address):
        return Network(self.address, self.mask + 1),\
            Network(IPv4Address(self.address.body + ((1 << (32 - self.mask)) // 2)), self.mask + 1)

    def get_total_hosts(self) -> int:
        return (1 << (32 - self.mask)) - 2

    def is_public(self) -> bool:
        return not (self.address in Network("10.0.0.0", 8)
                or self.address in Network("172.16.0.0", 12)
                or self.address in Network("192.168.0.0", 16))

    def __str__(self):
        return f"{self.address}/{self.mask}"


if __name__ == "__main__":
    ip = IPv4Address("192.168.0.122")
    net = Network(IPv4Address("192.168.0.0"), 24)
    pub = Network(IPv4Address("12.0.0.0"), 16)
    print(net)
    print(net.get_mask_int())
    print(net.get_mask_str())
    print(net.get_mask_len())
    print(net.get_first_usable())
    print(net.get_last_usable())
    print(net.get_broadcast_address())
    print(net.get_total_hosts())
    print(ip in net)
    net1, net2 = net.make_subnets()
    print(net1)
    print(net1.get_broadcast_address())
    print(net2)
    print(net2.get_first_usable())
    # print("123", net.address in Network(IPv4Address("192.168.0.0"), 24))
    print(net.is_public())
    print(pub.is_public())
    # print(not net.address in Network(IPv4Address("10.0.0.0"), 8))
    # print(not net.address in Network(IPv4Address("172.16.0.0"), 12))
    # print(not net.address in Network(IPv4Address("192.168.0.0"), 16))
    # print(net.is_public())
    # print(pub.is_public())


# class Network {
#   public Network(IPv4Address address, int maskLength) {}
#   public boolean contains(IPv4Address address) {}
#   public IPv4Address getAddress() {}
#   public IPv4Address getBroadcastAddress() {}
#   public IPv4Address getFirstUsableAddress() {}
#   public IPv4Address getLastUsableAddress() {}
#   public long getMask() {}
#   public String getMaskString() {}
#   public int getMaskLength() {}
#   public Network[] getSubnets() {} // produce two half-sized subnets
#   public long getTotalHosts() {} // excluding network and broadcast
#   public boolean isPublic() {}
# }

# IPv4Address address = new IPv4Address("192.168.0.0");
# Network net = new Network(address, 24);
#
# net.toString();                                // 192.168.0.0/24
# net.getAddress().toString();                   // 192.168.0.0
# net.getFirstUsableAddress().toString();        // 192.168.0.1
# net.getLastUsableAddress().toString();         // 192.168.0.254
# net.getMaskString();                           // 255.255.255.0
# net.getMaskLength();                           // 24
# net.isPublic();                                // false
# net.contains(new IPv4Address("10.0.23.4"));    // false
# net.contains(new IPv4Address("192.168.0.25")); // true
# net.getBroadcastAddress().toString();          // 192.168.0.255
#
#
# Network[] subnets = net.getSubnets();
#
# subnets[0].toString()                          // 192.168.0.0/25
# subnets[0].getAddress().toString()             // 192.168.0.0
# subnets[0].getFirstUsableAddress().toString(); // 192.168.0.1
# subnets[0].getLastUsableAddress().toString();  // 192.168.0.126
# subnets[0].getMaskLength();                    // 25
