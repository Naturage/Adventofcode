#read data in
#f = open("test.txt","r")
f = open("day 3 task 1 in.txt","r")
day3in = f.read().split()
f.close()

day3wire1 = day3in[0].split(",")
day3wire2 = day3in[1].split(",")

directionwire1 = [i[0] for i in day3wire1]
lengthwire1 = [int(i[1:]) for i in day3wire1]

directionwire2 = [i[0] for i in day3wire2]
lengthwire2 = [int(i[1:]) for i in day3wire2]

#parse the endpoints of each wire
def parsing(direction, length):
    pos = [0,0]
    wirepos = [[0],[0]]
    for i in range(0,len(direction)):
        if direction[i] == 'U':
            pos[1] = pos[1] + length[i]
        elif direction[i] == 'D':
            pos[1] = pos[1] - length[i]
        elif direction[i] == 'R':
            pos[0] = pos[0] + length[i]
        elif direction[i] == 'L':
            pos[0] = pos[0] - length[i]
        else:
            print("ERROR")
        wirepos[0].append(pos[0])
        wirepos[1].append(pos[1])
    return wirepos;

wire1pos = parsing(directionwire1,lengthwire1)
wire2pos = parsing(directionwire2,lengthwire2)

def orientation(startx, starty, finishx, finishy):
    if startx == finishx:
        direction = 'V'
    elif starty == finishy:
        direction = 'H'
    else:
        print("ERROR")
    return direction

#loop over all steps:
for w1 in range(1,len(wire1pos[0])):
    for w2 in range(1,len(wire2pos[0])):
        #figure out if the stem gos V or H:
        dir1 = orientation(wire1pos[0][w1-1],wire1pos[1][w1-1],wire1pos[0][w1],wire1pos[1][w1])
        dir2 = orientation(wire2pos[0][w2-1],wire2pos[1][w2-1],wire2pos[0][w2],wire2pos[1][w2])
        #if the two intersect right:
        if dir1 == 'H' and dir2 == 'V':
            #check if the point of intersection would be within each line:
            if min(wire1pos[0][w1-1],wire1pos[0][w1]) < wire2pos[0][w2] and max(wire1pos[0][w1-1],wire1pos[0][w1]) > wire2pos[0][w2] and min(wire2pos[1][w2-1],wire2pos[1][w2]) < wire1pos[1][w1] and max(wire2pos[1][w2-1],wire2pos[1][w2]) > wire1pos[1][w1] :
                #add the steps up: from the first one to second last (note step 0 moves us from 0 to 1; and intersection is at step from w1-1 to w1, ie step w1-1 - we only want to take part of it.
                temp = sum(lengthwire1[0:w1-1])+ sum(lengthwire2[0:w2-1])
                #figure out where we approach from and add the required length
                if directionwire1[w1-1] == 'R':
                    temp = temp + wire2pos[0][w2] - wire1pos[0][w1-1]
                elif directionwire1[w1-1] == 'L':
                    temp = temp - wire2pos[0][w2] + wire1pos[0][w1-1]
                if directionwire2[w2-1] == 'U':
                    temp = temp + wire1pos[1][w1] - wire2pos[1][w2-1]
                elif directionwire2[w2-1] == 'D':
                    temp = temp - wire1pos[1][w1] + wire2pos[1][w2-1]
                print(temp, w1, w2, wire1pos[0][w1-1], wire1pos[1][w1-1], wire1pos[0][w1], wire1pos[1][w1], wire2pos[0][w2-1],wire2pos[1][w2-1],wire2pos[0][w2],wire2pos[1][w2])
                #if new minimum - remember.
                if temp < manhattan:
                    manhattan = temp
        #same thing but for 1 and 2 swapped.
        elif dir1 == 'V' and dir2 == 'H':
            if min(wire2pos[0][w2-1],wire2pos[0][w2]) < wire1pos[0][w1] and max(wire2pos[0][w2-1],wire2pos[0][w2]) > wire1pos[0][w1] and min(wire1pos[1][w1-1],wire1pos[1][w1]) < wire2pos[1][w2] and max(wire1pos[1][w1-1],wire1pos[1][w1]) > wire2pos[1][w2] :
                temp = sum(lengthwire1[0:w1-1])+ sum(lengthwire2[0:w2-1])
                if directionwire2[w2-1] == 'R':
                    temp = temp + wire1pos[0][w1] - wire2pos[0][w2-1]
                elif directionwire2[w2-1] == 'L':
                    temp = temp - wire1pos[0][w1] + wire2pos[0][w2-1]
                if directionwire1[w1-1] == 'U':
                    temp = temp + wire2pos[1][w2] - wire1pos[1][w1-1]
                elif directionwire1[w1-1] == 'D':
                    temp = temp - wire2pos[1][w2] + wire1pos[1][w1-1]
                print(temp, w1, w2, wire1pos[0][w1-1], wire1pos[1][w1-1], wire1pos[0][w1], wire1pos[1][w1], wire2pos[0][w2-1],wire2pos[1][w2-1],wire2pos[0][w2],wire2pos[1][w2])
                if temp < manhattan:
                    manhattan = temp

#output.
print(manhattan)
        


