import utils

MEMORY_SIZE = 64 * 1024

class Emulator:
    memory_ = [utils.uint8() for _ in range(MEMORY_SIZE)]
    A = utils.uint8()
    X = utils.uint8()
    Y = utils.uint8()

    SP = utils.uint8()
    PC = utils.uint16()
    P = utils.uint8()

    def OP_ADC_IMM(self):
        pass

    def __init__(self):
        pass