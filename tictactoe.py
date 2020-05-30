game_is_still_going = True
winner = None
current_player = "X"


def game():

    game_board()

    while game_is_still_going:
        turn_control(current_player)
        check_if_game_over()
        flip_player()

    if (winner == "X") or (winner == "O"):
        print("Winner: " + winner)
    elif winner == None:
        print("NO WINNER!")


def game_board():
    global x
    x = int(input("What size game GoPy?"))
    while x < 3:
        print("please enter another value that bigger than 2!")
        x = int(input("What size game GoPy? "))

    global dizi
    dizi = []
    for i in range(x):
        a = []
        for j in range(x):
            u = j + (x*i)
            a.append(u)
        dizi.append(a)
    for k in dizi:
        for j in k:
            digit = str(j)
            if len(digit) <= 1:
                print(j, end="  ")
            else:
                print(j, end=" ")
        print()


def turn_control(player):
    global position
    if current_player == "X":
        print("Player1 turn")
    else:
        print("Player2 turn")

    position = input("Choose a position from 0 to {}: ".format(x ** 2))
    position = int(position)
    while (position > x ** 2 - 1) or (position < 0):
        print("Please enter another value!")
        position = input("Choose a position from 0 to {}: ".format(x ** 2))
        position = int(position)

    if dizi[position // x][position % x] == "X" and current_player == "X":
        print("You have made this choice before")

    elif dizi[position // x][position % x] == "X" and current_player == "O":
        print("The other player select this cell before.")

    elif dizi[position // x][position % x] == "O" and current_player == "X":
        print("The other player select this cell before.")

    elif dizi[position // x][position % x] == "O" and current_player == "O":
        print("You have made this choice before")

    else:
        dizi[position // x][position % x] = player



    for k in dizi:
        for j in k:
            digit = str(j)
            if len(digit) <= 1:
                print(j, end="  ")
            else:
                print(j, end=" ")
        print()


def check_if_game_over():
    check_win()
    check_tie()


def check_win():
    global winner
    # check_rows
    row_winner = check_rows()
    # check_columns
    column_winner = check_columns()
    # check diagonals
    diagonal_winner = check_diagonals()
    if row_winner:
        # there is a winner
        winner = row_winner
    elif column_winner:
        # there is a winner
        winner = column_winner
    elif diagonal_winner:
        # there is a winner
        winner = diagonal_winner
    return


def check_rows():
    global winner
    global game_is_still_going
    for i in dizi:
        if i.count("X") == x:
            winner = "X"
            game_is_still_going = False

        elif i.count("O") == x:
            winner = "O"
            game_is_still_going = False
    return


def check_columns():
    global winner
    global game_is_still_going
    r = []
    for i in dizi:
        for j in i:
            r.append(j)

    for z in range(x):
        c = []
        d = []
        for k in range(z, (x ** 2), x):
            if r[k] == "X":
                c.append(r[k])
            elif r[k] == "O":
                d.append(r[k])

        if c.count("X") == x:
            winner = "X"
            game_is_still_going = False

        if d.count("O") == x:
            winner = "O"
            game_is_still_going = False

    return


def check_diagonals():
    global winner
    global game_is_still_going
    r = []
    for i in dizi:
        for j in i:
            r.append(j)

    for z in range(0, x, x + 1):
        c = []
        d = []
        for k in range(z, (x ** 2), x + 1):
            if r[k] == "X":
                c.append(r[k])
            elif r[k] == "O":
                d.append(r[k])

        if c.count("X") == x:
            winner = "X"
            game_is_still_going = False

        if d.count("O") == x:
            winner = "O"
            game_is_still_going = False

    for z in range(x - 1, x, x - 1):
        c = []
        d = []
        for k in range(z, (x ** 2), x - 1):
            if r[k] == "X":
                c.append(r[k])
            elif r[k] == "O":
                d.append(r[k])

        if c.count("X") == x:
            winner = "X"
            game_is_still_going = False

        if d.count("O") == x:
            winner = "O"
            game_is_still_going = False

    return


def check_tie():
    global winner
    global game_is_still_going
    r = []
    for i in dizi:
        for j in i:
            r.append(j)

    if r.count("X") + r.count("O") == x ** 2:
        game_is_still_going = False

    return


def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return


game()
