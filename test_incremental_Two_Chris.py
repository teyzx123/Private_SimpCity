from files.Game_Options import *
import pytest


def test_save_game(): #
    board=Board()
    newboard=board.New_Board()
    assert board.Save_Board() == True
def test_load_game(): #
    board=Board()
    assert board.Load_Board()==True
@pytest.mark.parametrize("BuildingType,expectedResult",[("BCH","Successfully built"),("FAC","Successfully built"),("HSE","Successfully built"),("SHP","Successfully built"),("HWY","Successfully built")])
def test_play_game_after_load(BuildingType,expectedResult): #
    board=Board()
    board.Load_Board()
    result=building_choice(board,"B1",BuildingType)
    assert result== expectedResult
