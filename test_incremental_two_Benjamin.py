from files.Game_Options import *
from files.Menu import *
from files.Board import *


def test_invalid_Location():
    board=Board()
    checkboard=board.New_Board()
    result=place_building(board,"HWY","A6")
    assert result=="Invalid row"
def test_Overlapping_Location():
    board=Board()
    checkboard=board.New_Board()
    building_choice(board,"A1","HWY")
    result=prevent_overlap(board,"A1","HWY")
    assert result == "Overlap"
def test_not_adjacent():
    board=Board()
    checkboard=board.New_Board()
    building_choice(board,"A1","HWY")
    result=check_adjacent(board, "A3","HWY")
    assert result == "No adjacent"

def test_updatebuilding():
    board=Board()
    Building=board.New_Board()
    DefaultNum=board.Beach
    building_choice(board,"A1","BCH")
    ChangeNum=board.Beach
    assert DefaultNum != ChangeNum
    
