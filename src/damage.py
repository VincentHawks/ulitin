class Damage:

    def __init__(self, phys: int, math: int, phil: int, prog: int, absolute=0):
        self.__phys = phys
        self.__math = math
        self.__phil = phil
        self.__prog = prog
        self.__absolute = absolute

    def get_phys(self):
        return self.__phys

    def get_math(self):
        return self.__math

    def get_phil(self):
        return self.__phil

    def get_prog(self):
        return self.__prog

    def get_abs(self):
        return self.__absolute

    def set_phys(self, arg):
        self.__phys = arg

    def set_phil(self, arg):
        self.__phil = arg

    def set_math(self, arg):
        self.__math = arg

    def set_prog(self, arg):
        self.__prog = arg

    def set_abs(self, arg):
        self.__absolute = arg


class Resists:

    def __init__(self, phys: float, math: float, phil: float, prog: float):
        self.__phys = phys
        self.__math = math
        self.__phil = phil
        self.__prog = prog

    def get_phys(self):
        return self.__phys

    def get_math(self):
        return self.__math

    def get_phil(self):
        return self.__phil

    def get_prog(self):
        return self.__prog

    def set_phys(self, arg):
        self.__phys = arg

    def set_phil(self, arg):
        self.__phil = arg

    def set_math(self, arg):
        self.__math = arg

    def set_prog(self, arg):
        self.__prog = arg