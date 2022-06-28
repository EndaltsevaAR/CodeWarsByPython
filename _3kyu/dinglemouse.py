class Dinglemouse(object):

    def __init__(self, queues, capacity):
        self.queues = queues
        self.capacity = capacity
        self.liftMovingList = []
        self.floorsToStopList = []

    def theLift(self):
        self.liftMovingList.append(0)
        current_floor = 0
        while self.is_higher_passengers_wait(0):
            for floor in range(len(self.queues)):
                self.entry_floor_checking(True, floor)
                if not self.is_higher_passengers_wait(floor + 1) and not is_lift_need_to_up(floor):
                    current_floor = floor
                    break
            for floor in range(current_floor, 0, -1):
                self.entry_floor_checking(False, floor)
        if self.liftMovingList[len(self.liftMovingList) - 1] != 0:
            self.liftMovingList.append(0)
        return self.liftMovingList


    def is_higher_passengers_wait(self, param):
        pass


    def entry_floor_checking(self, param, floor):
        if floor in self.floorsToStopList:
            self.floorsToStopList.remove(floor)
            if self.liftMovingList[len(self.liftMovingList) - 1] != floor:
                self.liftMovingList.append(floor)
        for passenger in range(len(self.queues[floor])):



    def is_lift_need_to_up(self, floor):
        pass