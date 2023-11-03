from wk9 import roman_to_int
def test_roman_to_int():
    # Test valid uppercase Roman numerals
    assert roman_to_int("I") == 1
    assert roman_to_int("IV") == 4
    assert roman_to_int("IX") == 9
    assert roman_to_int("XII") == 12
    assert roman_to_int("XXI") == 21
    assert roman_to_int("XLII") == 42
    assert roman_to_int("LX") == 60
    assert roman_to_int("XC") == 90
    assert roman_to_int("CXX") == 120
    assert roman_to_int("CD") == 400
    assert roman_to_int("DCCC") == 800
    assert roman_to_int("CM") == 900
    assert roman_to_int("MCMXCIV") == 1994

    assert roman_to_int("ZSW") == 0
    # Test valid lowercase Roman numerals
    # assert roman_to_int("i") == 1
    # assert roman_to_int("iv") == 4
    # assert roman_to_int("ix") == 9
    # assert roman_to_int("xii") == 12
    # assert roman_to_int("xxi") == 21
    # assert roman_to_int("xlii") == 42
    # assert roman_to_int("lx") == 60
    # assert roman_to_int("xc") == 90
    # assert roman_to_int("cxx") == 120
    # assert roman_to_int("cd") == 400
    # assert roman_to_int("dcccl") == 800
    # assert roman_to_int("cm") == 900
    # assert roman_to_int("mcmxciv") == 1994

    # Test invalid characters
    # try:
    #     roman_to_int("XYZ")
    #     assert False, "Invalid characters should raise an exception"
    # except ValueError:
    #     pass

    print("All test cases passed for roman_to_int.")

test_roman_to_int()


