# coding=utf-8
class State:
    def __init__(self, missionary_left, missionary_right, cannibals_left, cannibals_right, river_side):
        self.missionary_left = missionary_left
        self.missionary_right = missionary_right
        self.cannibals_left = cannibals_left
        self.cannibals_right = cannibals_right
        self.river_side = river_side
        self.father = None
        self.son = []

    def __str__(self):
        return 'Missionarios: {}\t| Missionarios: {}\nCanibais: {}\t| Canibais: {}'.format(
            self.missionary_left, self.missionary_right, self.cannibals_left, self.cannibals_right
        )

    def valid_state(self):
        if ((self.missionary_left < 0) or (self.missionary_right < 0)
                or (self.cannibals_left < 0) or (self.cannibals_right < 0)):
            return False
        return ((self.missionary_left == 0 or self.missionary_left >= self.cannibals_left) and
                (self.missionary_right == 0 or self.missionary_right >= self.cannibals_right))

    def final_state(self):
        result_left = self.missionary_left == self.cannibals_left == 0
        result_right = self.missionary_right == self.cannibals_right == 3
        return result_left and result_right

    def generate_son(self):
        new_river_side = 'dir' if self.river_side == 'esq' else 'esq'
        movements = [
            {'missionarios': 2, 'canibais': 0},
            {'missionarios': 1, 'canibais': 0},
            {'missionarios': 1, 'canibais': 1},
            {'missionarios': 0, 'canibais': 1},
            {'missionarios': 0, 'canibais': 2},
        ]
        for movement in movements:
            if self.river_side == 'esq':
                missionary_left = self.missionary_left - movement['missionarios']
                missionary_right = self.missionary_right + movement['missionarios']
                cannibals_left = self.cannibals_left - movement['canibais']
                cannibals_right = self.cannibals_right + movement['canibais']
            else:
                missionary_right = self.missionary_right - movement['missionarios']
                missionary_left = self.missionary_left + movement['missionarios']
                cannibals_right = self.cannibals_right - movement['canibais']
                cannibals_left = self.cannibals_left + movement['canibais']
            son = State(missionary_left, missionary_right, cannibals_left,
                        cannibals_right, new_river_side)
            son.father = self
            if son.valid_state():
                self.son.append(son)


class MissionaryCannibals:
    def __init__(self):
        self.queue_exe = [State(3, 0, 3, 0, 'esq')]
        self.solution = None

    def generate_solution(self):
        for element in self.queue_exe:
            if element.final_state():
                self.solution = [element]
                while element.father:
                    self.solution.insert(0, element.father)
                    element = element.father
                break
            element.generate_son()
            self.queue_exe.extend(element.son)
