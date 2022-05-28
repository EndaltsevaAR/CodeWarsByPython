# TODO: create the User class
# it must support rank, progress, and the inc_progress(rank) method
class User:
    def __init__(self):
        self.progress = 0
        self.rank_list = (-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8)
        self.rank = self.rank_list[0]

    def inc_progress(self, rank):
        try:
            self.rank_list.__contains__(rank) == True
        except ValueError:
            print("ValueError")
        d = self.rank_list.index(rank) - self.rank_list.index(self.rank)
        if d < -1:
            return
        elif d == -1:
            self.progress += 1
        elif d == 0:
            self.progress += 3
        else:
            self.progress += d*d*10
        while self.progress >= 100 and rank < 8:
            self.progress -= 100
            self.rank = self.rank_list[self.rank_list.index(self.rank) + 1]
        if self.rank == 8:
            self.progress = 0


user = User()
print(user.rank)
print(user.progress)
user.inc_progress(-7)
print(user.rank)
print(user.progress)
user.inc_progress(-5)
print(user.rank)
print(user.progress)

