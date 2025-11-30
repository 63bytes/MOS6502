import utils
uint8 = lambda:utils.BITS(8)
uint16 = lambda:utils.BITS(16)

MEMORY_SIZE = 64 * 1024

class Emulator:
    memory_ = [uint8() for _ in range(MEMORY_SIZE)]
    A = uint8()
    X = uint8()
    Y = uint8()
    SP = uint8()
    PC = uint16()
    P = uint8()

    def __init__(self):
        pass