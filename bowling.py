import re

#score = ["X|X|X|X|X|X|X|X|X|X||XX","9-|9-|9-|9-|9-|9-|9-|9-|9-|9-||","X|7/|9-|X|-8|8/|-6|X|X|X||81"]
score = "9-|9-|9-|9-|9-|9-|9-|9-|9-|9-||"

def strike(frame):
    print('Strike')
    if score[frame + 1][1] == '/':
        total += 10 + int(score[frame + 1][0]) + spare(frame + 1)
        
    elif score2[frame + 1] == 'X':
        total += 10 
        strike(frame + 1)
    else:
        total += 10 + int(score[frame + 1][0] + int(score[frame + 1][1])
    return total

def spare(frame):
    print('Spare')
    total += 10 + int(score[frame + 1][0])
    return total

score2 = score.split("|")
count = len(score2)
print(score2, len(score2))
total = 0
for s range(0, count -2) :
    #print(s)
    if count2[s] == '':
        continue
    if score2[s] == 'X':
        total += strike(s)
    if  score2[s][1] =='/':
        total += spare(s)
    if  score2[0] == '-':
        total = total
    if  re.search("-\d", score2[s]):
        total += int(score[s][1])
    if  re.search("\d-", score2[s]):
        total += int(score[s][0])
    else:
        total += int(s[0]) + int(s[1])
print('TOTAL: ', total)
