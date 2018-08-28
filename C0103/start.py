from classes import State

if __name__ == '__main__':
    print 'N-Puzzle Solver!'
    print 10 * '-'
    state = State(3)
    print 'The Starting State is:'
    start = state.start_state(5)
    state.print_st(start)
    print 'The Goal State should be:'
    state.print_st(state.goal)
    print 'Here it Goes:'
    state.print_st(start)
    state.solve_it(start)