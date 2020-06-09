# Essentially just commonly used parameter objects
class Damage:

    def __init__(self, phys: int, math: int, phil: int, prog: int, absolute=0):
        self.phys = phys
        self.math = math
        self.phil = phil
        self.prog = prog
        self.abs = absolute


class Resists:

    def __init__(self, phys: float, math: float, phil: float, prog: float):
        self.phys = phys
        self.math = math
        self.phil = phil
        self.prog = prog
