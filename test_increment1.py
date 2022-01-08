from files.Menu import *


def test_newboard():
    board=Board()
    board.New_Board
    #When its true that means the connection is successful and
    #the program is able to take the empty board from the excelfile
    assert board.New_Board() == True
