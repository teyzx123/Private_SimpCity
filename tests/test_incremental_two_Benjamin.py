from files.Game_Options import building_choice, check_adjacent, display_remaining_building, place_building, prevent_overlap
from files.Menu import *
from files.Board import *


def test_invaild_Location():
    board=Board()
    checkboard=board.New_Board()
    result=place_building(board,"HWY","A6")
    assert result==False
def test_Overlapping_Location():
    board=Board()
    checkboard=board.New_Board()
    building_choice(board,"A1","HWY")
    result=prevent_overlap(board,"A1","HWY")
    assert result == False
def test_not_adjacent():
    board=Board()
    checkboard=board.New_Board()
    building_choice(board,"A1","HWY")
    result=check_adjacent(board, "A3","HWY")
    assert result == False

def test_ViewBuilding():
        board=Board()
        checkboard=board.New_Board()
        display_remaining_building(board)

def test_updatebuilding():
    board=Board()
    Building=board.New_Board()
    DefaultNum=board.Beach
    building_choice(board,"A1","BCH")
    ChangeNum=board.Beach
    assert DefaultNum != ChangeNum
    