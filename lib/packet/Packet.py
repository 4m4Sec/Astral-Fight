class Packet():

    PACKET_TYPE_ACTION = 0
    PACKET_TYPE_ENTITY = 1

    def __init__(self, type):
        self.type = type

    def get_type(self):
        return self.type

    # decode the packet
    def __call__(self):
        pass