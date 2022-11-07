 # We'll use the time module to measure the time of evaluating
# game tree in every move. It's a nice way to show the
# distinction between the basic Minimax and Minimax with
# alpha-beta pruning :)
# Since we'll be implementing this through a tic-tac-toe game,
# let's go through the building blocks.
# First, let's make a constructor and draw out the board:
import time
import datetime
class Game:
    def __init__(self):
        self.initialize_game()

    def initialize_game(self):
        self.current_state = [['.','.','.'],
                              ['.','.','.'],
                              ['.','.','.']]

        # Player X always plays first, اللاعب اكس دائما يلعب اولا
        self.player_turn = 'X'

    def draw_board(self):
        for i in range(0, 3):
            for j in range(0, 3):
                print('{}|'.format(self.current_state[i][j]), end=" ")
            print()
        print()

    # Determines if the made move is a legal move, تحدد اذا كانت هذه الحركة مسموحه
    def is_valid(self, px, py):
        if px < 0 or px > 2 or py < 0 or py > 2:
            return False
        elif self.current_state[px][py] != '.':
            return False
        else:
            return True

    # Checks if the game has ended and returns the winner in each case,   يتحقق مما اذا كانت اللعبة قد انتهت ويعيد الفائ في كل حاله
    def is_end(self):
        # Vertical win
        for i in range(0, 3):
            if (self.current_state[0][i] != '.' and
                    self.current_state[0][i] == self.current_state[1][i] and
                    self.current_state[1][i] == self.current_state[2][i]):
                return self.current_state[0][i]

        # Horizontal win
        for i in range(0, 3):
            if (self.current_state[i] == ['X', 'X', 'X']):
                return 'X'
            elif (self.current_state[i] == ['O', 'O', 'O']):
                return 'O'

        # Main diagonal win
        if (self.current_state[0][0] != '.' and
                self.current_state[0][0] == self.current_state[1][1] and
                self.current_state[0][0] == self.current_state[2][2]):
            return self.current_state[0][0]

        # Second diagonal win
        if (self.current_state[0][2] != '.' and
                self.current_state[0][2] == self.current_state[1][1] and
                self.current_state[0][2] == self.current_state[2][0]):
            return self.current_state[0][2]

        # Is whole board full?
        for i in range(0, 3):
            for j in range(0, 3):
                # There's an empty field, we continue the game
                if (self.current_state[i][j] == '.'):
                    return None

        # It's a tie!
        return '.'

    # Player 'O' is max, in this case AI,اللاعب او في هذه الحاله هو الاكبر وهو الكمبيوتر
    def max(self, count):

        # Possible values for maxv are:
        # -1 - loss
        # 0  - a tie
        # 1  - win

        # We're initially setting it to -2 as worse than the worst case:
        maxv = -2

        px = None
        py = None

        result = self.is_end()

        # If the game came to an end, the function needs to return
        # the evaluation function of the end. That can be:
        # -1 - loss
        # 0  - a tie
        # 1  - win
        if result == 'X':
            return (-1, 0, 0, count)
        elif result == 'O':
            return (1, 0, 0, count)
        elif result == '.':
            return (0, 0, 0, count)

        for i in range(0, 3):
            for j in range(0, 3):
                if self.current_state[i][j] == '.':
                    # On the empty field player 'O' makes a move and calls Min
                    # That's one branch of the game tree.
                    self.current_state[i][j] = 'O'
                    (m, min_i, min_j, count) = self.min(count)
                    # Fixing the maxv value if needed
                    if m > maxv:
                        maxv = m
                        px = i
                        py = j
                    # Setting back the field to empty
                    self.current_state[i][j] = '.'
        count = count + 1
        return (maxv, px, py, count)

    # Player 'X' is min, in this case human,اللاعب اكس هو الاصغر في هذه الحاله وهو يمثل الانسان
    def min(self, count):

# Possible values for minv are:
        # -1 - win
        # 0  - a tie
        # 1  - loss

        # We're initially setting it to 2 as worse than the worst case:,  نعرفه مبدئيا بقيمة ٢ كأسوأ الحالات
        minv = 2

        qx = None
        qy = None

        result = self.is_end()

        if result == 'X':
            return (-1, 0, 0, count)
        elif result == 'O':
            return (1, 0, 0, count)
        elif result == '.':
            return (0, 0, 0, count)

        for i in range(0, 3):
            for j in range(0, 3):
                if self.current_state[i][j] == '.':
                    self.current_state[i][j] = 'X'
                    (m, max_i, max_j, count) = self.max(count)
                    if m < minv:
                        minv = m
                        qx = i
                        qy = j
                    self.current_state[i][j] = '.'


        count = count + 1
        return (minv, qx, qy, count)

    def play(self):
        count = 0
        depth = 0
        print("=================================================")
        print("TIC-TAC-TOE using MINIMAX Algorithm")
        print("=================================================")
        print(time.ctime())

        print("X is You and O is Computer")
        print("You will always start,ready ?!, Let's start the game 😍!")
        print("Position on the board according to coordinates X, Y")
        # 1,1 =>> Row No. 1 Column No. 1,Don't forget the numbering starts at 0 .
        # So 1.1 will be the position in the middle of the board.
        #التربيب ف اللوحة يعتمد على احداثيات x , y ويبدا تترقيم الصفوف والاعمدة من الصفر.


        while True:
            self.draw_board()
            self.result = self.is_end()
            dt = datetime.datetime.now()

            # Printing the appropriate message if the game has ended
            if self.result != None:
                if self.result == 'X':
                    print('The winner is X!🥳')
                    print(time.ctime())
                elif self.result == 'O':
                    print('The winner is O!😟!')
                    print(time.ctime())
                elif self.result == '.':
                    print("It's a tie!😀")
                    print(time.ctime())

                print("The maximum Depth of tree is =>>", depth)
                print("The Size of tree is =>>", count)


                self.initialize_game()
                return

            # If it's player's turn
            if self.player_turn == 'X':

                while True:

                    start = time.time()
                    (m, qx, qy, count) = self.min(count)
                    end = time.time()
                    print('Evaluation time⏳: {}s'.format(round(end - start, 7)))
                    print('Recommended move: X = {}, Y = {}'.format(qx, qy))

                    px = int(input('Insert the X coordinate: '))
                    py = int(input('Insert the Y coordinate: '))


                    (qx, qy) = (px, py)

                    if self.is_valid(px, py):
                        self.current_state[px][py] = 'X'
                        self.player_turn = 'O'
                        depth = depth + 1
                        break
                    else:
                        print('The move is not valid! Try again.')

            # If it's AI's turn
            else:
                (m, px, py, count) = self.max(count)
                self.current_state[px][py] = 'O'
                self.player_turn = 'X'
                depth=depth+1

def main():
         g = Game()
         g.play()


if __name__ == "__main__":
        main()