from copy import copy


class State:
    def __init__(self, initialState, solution=[" ", "<", "<", "<", "_", ">", ">", ">", " "]):
        self.state = initialState
        self.solution = solution
        self.father = None
        self.son = []

    def final_state(self):
        for j, i in enumerate(self.state):
            if i != self.solution[j]:
                return False
        return True

    def append_son(self, actual_state):
        state = State(actual_state)
        state.father = self
        self.son.append(state)

    def generate_son(self):
        for i in range(len(self.state)):
            statecopy = copy(self.state)
            if self.state[i] == '>':
                if self.state[i + 1] == '_':
                    statecopy[i] = self.state[i + 1]
                    statecopy[i + 1] = self.state[i]
                    self.append_son(statecopy)
                if self.state[i + 1] == '<' and self.state[i + 2] == '_':
                    statecopy[i] = self.state[i + 2]
                    statecopy[i + 2] = self.state[i]
                    self.append_son(statecopy)
            if self.state[i] == '<':
                if self.state[i - 1] == '_':
                    statecopy[i] = self.state[i - 1]
                    statecopy[i - 1] = self.state[i]
                    self.append_son(statecopy)
                if self.state[i - 1] == '>' and self.state[i - 2] == '_':
                    statecopy[i] = self.state[i - 2]
                    statecopy[i - 2] = self.state[i]
                    self.append_son(statecopy)

    def __str__(self):
        result = ""
        for i in self.state[1:-1]:
            result += i
        return result


class LucasProblem:
    def __init__(self):
        self.queue_exe = [State([" ", ">", ">", ">", "_", "<", "<", "<", " "])]
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
