###########################################################################################################
# Size of the grid( X and Y Axis): input1(X) & input2(Y) > 0 and rectangular                              #
# Current postion the robot: repre as string input3(X-Y-D) where X & Y the current position oF robot      #
#                           and D repre. the direction where the robot is currently facing.               #
# set of instructions to move the robot: Input4 it repre. string separated by space. like(M, L Or R)      #
#                     M: means "move 1 unit forword in the direction that the robot is facing"            #
#                     L: means "Turn 90 degree towards left"                                              #
#                     R: means "Turn 90 degree towards right"                                             #
#                                                                                                         #
#                                                                                                         #
#  IF robot moves out of grid it return current position with "-ER"                                       #
###########################################################################################################

def direction(D, inst):
    if D == "E":
        if inst == "L":
            return 'N'
        else:
            return 'S'
    elif D == "W":
        if inst == "L":
            return 'S'
        else:
            return 'N'

    elif D == "N":
        if inst == "L":
            return 'W'
        else:
            return 'E'
    elif D == "S":
        if inst == "L":
            return 'E'
        else:
            return 'W'


def moveRobot(X, Y, current_position, instruction):

    if X > 0 and Y > 0:
        for inst in instruction.replace(" ", ""):
            if inst != 'M':
                D = direction(current_position[4], inst)
                current_position = current_position[:4] + D + current_position[4+1:]

            else:

                if current_position[4] == "E" and int(current_position[0]) < X:
                    current_position = current_position[:0] + str(int(current_position[0]) + 1) + current_position[0+1:]

                elif current_position[4] == "W" and int(current_position[0]) < X:
                    current_position = current_position[:0] + str(int(current_position[0]) - 1) + current_position[0+1:]

                elif current_position[4] == "N" and int(current_position[2]) < Y:
                    current_position = current_position[:2] + str(int(current_position[2]) + 1) + current_position[2+1:]

                elif current_position[4] == "S" and int(current_position[2]) < Y:
                    current_position = current_position[:2] + str(int(current_position[2]) - 1) + current_position[2+1:]

                else:
                    current_position = current_position + "-ER"
                    break

        return current_position


if __name__ == '__main__':
    print("Enter size of Grid: X and Y")
    X, Y = map(int, input().split())
    print("Enter current position of robot")
    starting_position = input()
    print("set of inst to move the robot")
    instruction = input()

    print(moveRobot(X, Y, starting_position, instruction))
