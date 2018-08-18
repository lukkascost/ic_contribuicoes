from classes import LucasProblem


def main():
    problem = LucasProblem()
    problem.generate_solution()
    for state in problem.solution:
        print "\t", state, "\t"


if __name__ == '__main__':
    main()
