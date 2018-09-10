from point import Point
from time import sleep
from enum import Enum

class TagComparisonStates(Enum):
    NEW = 1
    UNCHANGED = 2
    UPDATED = 3
    ERR = 4

TIMESTAMP_THRESHOLD = 3000

class TagComparer:

    def __init__(self, event1, event2):
        self._event1 = event1
        self._event2 = event2

        self.newLocation = self.isNewLocation()
        self.newTimestamp = self.isNewTimestamp()
        self.newStream = self.isNewStream()

    def isNewTimestamp(self):
        return abs(self._event1.timestamp - self._event2.timestamp) >= TIMESTAMP_THRESHOLD

    def isNewLocation(self):
        newLocation =self._event1.location.__cmp__(self._event2.location)
        print("Is new location? {}".format(newLocation))
        return newLocation

    def isNewStream(self):
        return self._event1.sourceStream!=self._event2.sourceStream

    def compare(self):
        if not self.newLocation and not self.newTimestamp:
            return TagComparisonStates.UNCHANGED
        
        if self.newStream and not self.newTimestamp and self.newLocation:
            return TagComparisonStates.ERR

        else:
            return TagComparisonStates.UPDATED
        

class TagEvent:

    def __init__(self):
        self._tagId = int()
        self._location = Point()
        self._srcStream = str()
        self._ts = float()
 
    def __eq__(self, other):
        return self._tagId==other.tagId

    def toDict(self):
        return { 'tagId': self._tagId, 'location': self._location.__dict__, 'sourceStream': self._srcStream, 'timestamp': self._ts}

    @property
    def tagId(self):
        return self._tagId

    def setTagId(self, tagId):
        self._tagId = tagId

    @property
    def timestamp(self):
        return self._ts

    def setTimestamp(self, ts):
        self._ts = ts

    @property
    def location(self):
        return self._location

    def setLocation(self, point:Point):
        self._location = point

    @property
    def sourceStream(self):
        return self._srcStream

    def setSourceStream(self, sourceStream):
        self._srcStream = sourceStream

from datetime import datetime

def getNow():
    unix_epoch = datetime(1970, 1, 1)
    utcnow = datetime.utcnow()
    epochMilliseconds = round(((utcnow-unix_epoch).total_seconds()*1000),0)
    return epochMilliseconds

# event1 = TagEvent()
# point1  = Point()
# point1.setX(7)
# point1.setY(10)


# event1.setTagId(110)
# event1.setSourceStream("dummy")
# event1.setTimestamp(getNow())
# event1.setLocation(point1)

# event2 = TagEvent()
# point2 = Point()
# point2.setX(11)
# point2.setY(14)

# event2.setTagId(110)
# event2.setSourceStream("dummy2")
# event2.setTimestamp(getNow())
# event2.setLocation(point2)

# subtraction = point1.__sub__(point2)
# comparison = point1.__cmp__(point2)
# print(subtraction)
# print(comparison)

# print(event1.__cmp__(event2))

# print(event1.__dict__)
# print(event2.__dict__)
# sleep(1)