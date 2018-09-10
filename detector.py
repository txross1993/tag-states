from expiringdict import ExpiringDict
from tag_event import TagEvent, TagComparisonStates, TagComparer
from tag_event import getNow
from point import Point

MAX_LENGHT=300
MAX_AGE_SECONDS=5

class TagDetector:

    cache = ExpiringDict(MAX_LENGHT,MAX_AGE_SECONDS)

    def __init__(self):
        pass

    def addToCache(self, event):
        entry = { event.tagId: event }
        TagDetector.cache.update(entry)

    def checkIfInCache(self, event):
        print(TagDetector.cache)

        print(event.tagId)
        try:
            TagDetector.cache[event.tagId]
            return True
        except KeyError:
            return False


    def getEvents(self):
        
        #New
        point1=Point()
        point1.setX(10)
        point1.setY(10)
        event1=TagEvent()
        event1.setLocation(point1)
        event1.setSourceStream("first-stream")
        event1.setTimestamp(getNow())
        event1.setTagId(110)

        #ERR
        point3=Point()
        point3.setX(15)
        point3.setY(10)
        event3=TagEvent()
        event3.setLocation(point3)
        event3.setSourceStream("second-stream")
        event3.setTimestamp(event1.timestamp)
        event3.setTagId(110)

        #Updated
        point2=Point()
        point2.setX(10)
        point2.setY(10)
        event2=TagEvent()
        event2.setLocation(point2)
        event2.setSourceStream("first-stream")
        event2.setTimestamp(event1.timestamp+5001)
        event2.setTagId(110)

        #Unchanged
        point4=Point()
        point4.setX(10)
        point4.setY(10)
        event4=TagEvent()
        event4.setLocation(point4)
        event4.setSourceStream("fourth-stream")
        event4.setTimestamp(event1.timestamp+5001)
        event4.setTagId(110)

        tagEvents = [event1, event3, event2, event4]

        return tagEvents

    def work(self):
        events = self.getEvents()
        for index, event in enumerate(events):
            print("Processing {}th index of events".format(index))
            print(event.toDict())
            tagId = event.tagId
            
            if self.checkIfInCache(event):
                tagState = TagComparer(event, TagDetector.cache[tagId]).compare()                
                if tagState == TagComparisonStates.UPDATED:
                    self.addToCache(event)
                    print("Added event to cache: {}. tag state was UPDATED".format(event.toDict()))
                elif tagState == TagComparisonStates.ERR:
                    print("Possible homography error for stream {}".format(event.sourceStream))
                    print(""" First event {} \n
                              Second event with error: {}""".format(TagDetector.cache[event.tagId].toDict(), event.toDict()))
                else:
                    print("Tag state was {}".format(tagState))
            else:
                self.addToCache(event)
                print("Added event to cache: {}. Tag state was NEW".format(event.toDict()))

detector = TagDetector()
detector.work()

from time import sleep
sleep(1)

