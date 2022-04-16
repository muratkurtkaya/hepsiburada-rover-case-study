
from asyncore import read


class Rover:
    #init
    def __init__(self, x, y, direction):
        self.x = int(x)
        self.y = int(y)
        self.direction = direction
        self.directions = ['N', 'E', 'S', 'W']
        self.moveVals = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
    def move(self, command):
        if command == 'M':
            self.x += self.moveVals[self.direction][0]
            self.y += self.moveVals[self.direction][1]
        elif command == 'L':
            self.direction = self.directions[(self.directions.index(self.direction) - 1) % 4]
        elif command == 'R':
            self.direction = self.directions[(self.directions.index(self.direction) + 1) % 4]
        else:
            print('Invalid command')

#read one line from txt file
def read_line(file):
    line = file.readline()
    if not line:
        return None
    return line.strip()

def txtParser(file):
    firstRoverVals = read_line(file)
    firstRoverCommands = read_line(file)
    return firstRoverVals, firstRoverCommands

#if main
if __name__ == '__main__':
    file = open("input.txt", 'r')
    _ = read_line(file)
    firstRov,firstRovCommands = txtParser(file)
    firstRov = firstRov.split(" ")
    firtRover = Rover(firstRov[0], firstRov[1], firstRov[2])
    for command in firstRovCommands:
        firtRover.move(command)

    secondRov, secondRovCommands = txtParser(file)
    file.close()
    secondRov = secondRov.split(" ")
    secondRover = Rover(secondRov[0], secondRov[1], secondRov[2])
    for command in secondRovCommands:
        secondRover.move(command)

    print(firtRover.x, firtRover.y, firtRover.direction)
    print(secondRover.x, secondRover.y, secondRover.direction)