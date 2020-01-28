import re


class IllegalArgumentException(Exception):
    pass


class IPv4Address:

    def __init__(self, address):
        """Translate address string or integer into IPv4 address.

        raise IllegalArgumentException
            if input address is incorrect(<0.0.0.0 or >255.255.255.255) or
            if input string is incorrect
        """

        if isinstance(address, str):
            if re.fullmatch(r"\d{1,3}\D\d{1,3}\D\d{1,3}\D\d{1,3}", address):
                quads = list(map(int, re.findall(r"\d{1,3}", address)))
            else:
                raise IllegalArgumentException("Invalid input")

            quads = [int(quad) for quad in quads if 256 > int(quad) > -1]
            if len(quads) != 4:
                raise IllegalArgumentException("Invalid input")

            self.body = (quads[0] << 24) + (quads[1] << 16) + (quads[2] << 8) + quads[3]
        elif isinstance(address, int):
            self.body = address
        else:
            raise IllegalArgumentException("Invalid argument type")

        if self.body < 0 or self.body > 4294967295:    # 255.255.255.255
            raise IllegalArgumentException("Argument is out of range")

    def __lt__(self, other):
        return self.body < other.body

    def __gt__(self, other):
        return self.body > other.body

    def __eq__(self, other):
        return self.body == other.body

    def __str__(self):
        return f"{self.body >> 24}."                \
               f"{(self.body >> 16) & 0x00FF}."     \
               f"{(self.body >> 8) & 0x0000FF}."    \
               f"{self.body & 0x000000FF}"

    def __long__(self):
        return self.body


if __name__ == "__main__":
    ip = IPv4Address("192.168.1.0")
    lip = IPv4Address(3232235776)
    brok = IPv4Address("255.25.255.255")
    some = IPv4Address("192.168.1.0")
    print(ip)
    print(ip.__long__())
    print(lip)
    print(lip.__long__())
    print(brok)
    print(brok.__long__())
