# Election

print("*** Election ***")
candidate = 20
candidate_count = []

for i in range(0, candidate):
    candidate_count.append(0)

voters = int(input("Enter a number of voter(s) : "))
ballots = [int(i) for i in input().split()]
del ballots[voters:]

for i in range(voters):
    for ballot in ballots:
        if ballot>0:
            candidate_count[i] += (1 if ballot == i+1 else 0)

candidate_count.insert(0, 0)
winner = candidate_count.index(max(candidate_count))

if winner in range(1, candidate+1) :
    print(winner)
else:
    print("*** No Candidate Wins ***")