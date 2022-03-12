point_count = int(input())
point_list = []
solutions = [0,1,2]
for i in range(0,point_count):
    point_list.append(raw_input().split(' '))
    point_list[i][0] = int(point_list[i][0])
    point_list[i][1] = int(point_list[i][1])
    point_list[i].append(abs(point_list[i][0])+abs(point_list[i][1]))


for i in range(3,point_count):
    if((point_list[i][2] < point_list[solutions[0]][2]) or (point_list[i][2] < point_list[solutions[1]][2]) or (point_list[i][2] < point_list[solutions[2]][2])):
        max_num = 0
        if(point_list[solutions[max_num]][2] < point_list[solutions[1]][2]):
            max_num = 1
        if(point_list[solutions[max_num]][2] < point_list[solutions[2]][2]):
            max_num = 2
        solutions.pop(max_num)
        solutions.append(i)

solutions[0] += 1
solutions[1] += 1
solutions[2] += 1

print str(solutions[0]) + " " + str(solutions[1]) + " " + str(solutions[2])
