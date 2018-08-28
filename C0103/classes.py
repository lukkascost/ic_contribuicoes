import random


class State:

    def __init__(self, nsize):
        self.n_size = nsize
        self.t_size = pow(self.n_size, 2)
        self.goal = range(1, self.t_size)
        self.goal.append(0)

    def print_st(self, st):
        for (index, value) in enumerate(st):
            print ' %s ' % value,
            if index in [x for x in range(self.n_size - 1, self.t_size,
                                          self.n_size)]:
                print
        print

    def get_values(self, key):
        values = [1, -1, self.n_size, -self.n_size]
        valid = []
        for x in values:
            if 0 <= key + x < self.t_size:
                if x == 1 and key in range(self.n_size - 1, self.t_size,
                                           self.n_size):
                    continue
                if x == -1 and key in range(0, self.t_size, self.n_size):
                    continue
                valid.append(x)
        return valid

    def expand(self, st):
        p_expands = {}
        for key in range(self.t_size):
            p_expands[key] = self.get_values(key)
        pos = st.index(0)
        moves = p_expands[pos]
        exp_states = []
        for mv in moves:
            nstate = st[:]
            (nstate[pos + mv], nstate[pos]) = (nstate[pos], nstate[pos +
                    mv])
            exp_states.append(nstate)
        return exp_states

    def one_of_poss(self, st):
        exp_sts = self.expand(st)
        rand_st = random.choice(exp_sts)
        return rand_st

    def start_state(self, seed=1000):
        start_st = self.goal[:]
        for sts in range(seed):
            start_st = self.one_of_poss(start_st)
        return start_st

    def goal_reached(self, st):
        return st == self.goal

    def manhattan_distance(self, st):
        mdist = 0
        for node in st:
            if node != 0:
                g_dist = abs(self.goal.index(node) - st.index(node))
                (jumps, steps) = (g_dist // self.n_size, g_dist % self.n_size)
                mdist += jumps + steps
        return mdist

    def heuristic_next_state(self, st):
        exp_sts = self.expand(st)
        m_dists = []
        for st in exp_sts:
            m_dists.append(self.manhattan_distance(st))
        m_dists.sort()
        short_path = m_dists[0]
        if m_dists.count(short_path) > 1:
            least_paths = [st for st in exp_sts if self.manhattan_distance(st) == short_path]
            return random.choice(least_paths)
        else:
            for st in exp_sts:
                if self.manhattan_distance(st) == short_path:
                    return st

    def solve_it(self, st):
        while not self.goal_reached(st):
            st = self.heuristic_next_state(st)
            self.print_st(st)

