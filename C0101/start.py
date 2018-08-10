# coding=utf-8
from classes import MissionaryCannibals


def main():
    problem = MissionaryCannibals()
    problem.generate_solution()
    for state in problem.solution:
        print state
        print 34 * '-'


if __name__ == '__main__':
    main()
