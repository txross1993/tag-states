MAX_DISTANCE_THRESHOLD=5

class Point:

    def __init__(self):
        self._x = None
        self._y = None

    def __cmp__(self, other):
        return any([point>=MAX_DISTANCE_THRESHOLD for point in self.__sub__(other)])

    def __sub__(self, other):
        sub = [abs(self._x-other.x), abs(self._y-other.y)]
        return sub                                                                           

    @property
    def x(self):
        return self._x

    def setX(self, x):
        self._x = x

    @property
    def y(self):
        return self._y

    def setY(self, y):
        self._y = y