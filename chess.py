checkmate = false
board = [
['br','bn','bb','bq','bk','bb','bn','br'],
['bp','bp','bp','bp','bp','bp','bp','bp'],
['  ','  ','  ','  ','  ','  ','  ','  '],
['  ','  ','  ','  ','  ','  ','  ','  '],
['  ','  ','  ','  ','  ','  ','  ','  '],
['  ','  ','  ','  ','  ','  ','  ','  '],
['wp','wp','wp','wp','wp','wp','wp','wp'],
['wr','wn','wb','wq','wk','wb','wn','wr']]

def viable()

def print_board():
    print('-----------------------------------------')
    for row in board:
        print('|', end='')
        for elem in row:
            print(' ' + elem + ' |', end='')
        print()
        print('-----------------------------------------')

def update_board():
    while(True):
        print_board()
        if (checkmate):
            break
        viable(white_move())
        print_board()
        if (checkmate):
            break
        viable(black_move())

update_board()
