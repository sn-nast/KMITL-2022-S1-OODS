# TODO

import random

print("*** Election ***")
candidate = 20
voters = int(input("Enter a number of voter(s) : "))
ballot = []

for i in range(voters):
    # vote = random.choice([-1, 1])*random.randint(0, candidate)
    vote = random.randint(0, candidate)
    print(vote, end=" ")
    ballot.append(vote)

winner = max(ballot, key=ballot.count)
print('\n')
if winner not in range(1, candidate) :
    print("*** No Candidate Wins ***")
else:
    print(winner)
