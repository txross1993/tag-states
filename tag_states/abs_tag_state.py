from abc import ABCMeta, abstractmethod

class AbstractTagState(metaclass=ABCMeta):

    def accept(self, tagEventVisitor):
        tagEventVisitor.get