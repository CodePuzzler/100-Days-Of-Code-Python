# Day6 of my 100DaysOfCode Challenge

# Problem

# You are conducting a contest at your college. This contest consists of two problems and n participants. You know the problem that a candidate will solve during the contest.

# You provide a balloon to a participant after he or she solves a problem. There are only green and purple-colored balloons available in a market. Each problem must have a balloon associated with it as a prize for solving that specific problem. You can distribute balloons to each participant by performing the following operation:

#   1. Use green-colored balloons for the first problem and purple-colored balloons for the second problem
#   2. Use purple-colored balloons for the first problem and green-colored balloons for the second problem
# You are given the cost of each balloon and problems that each participant solve. Your task is to print the minimum price that you have to pay while purchasing balloons.

# Input format

# First line: T that denotes the number of test cases (1 <= T <= 10)
# For each test case: 
#   First line: Cost of green and purple-colored balloons 
#   Second line: n that denotes the number of participants (1 <=n <= 10)
# Next n lines: Contain the status of users. For example, if the value of the jth integer in the ith row is 0, then it depicts that the ith participant has not solved the jth problem. Similarly, if the value of the jth integer in the ith row is 1, then it depicts that the ith participant has solved the jth problem.

# Output format
# For each test case, print the minimum cost that you have to pay to purchase balloons.

test_cases = int(input("Enter number of test cases: "))
for _ in range(test_cases):
    cost_green_balloons, cost_purple_balloons = map(int, input().split())
    no_of_participants = int(input("Enter number of participants: "))
    cost1, cost2 = 0, 0
    for i in range(no_of_participants):
        value1, value2 = map(int, input().split())
        cost1 = cost1 + ((value1 * cost_green_balloons) + (value2 * cost_purple_balloons))
        cost2 = cost2 + ((value1 * cost_purple_balloons) + (value2 * cost_green_balloons))
    print(min(cost1,cost2))