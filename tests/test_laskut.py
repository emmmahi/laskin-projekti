import pytest
from laskin.laskut import Laskin #tai import laskin.laskut

# python -m pytest -v --cov
# https://docs.pytest.org/en/6.2.x/fixture.html

@pytest.fixture
def laskut():
    return Laskin()

def test_summa(laskut):
    value = laskut.summa(3,3)
    assert value == 6.0

def test_vahennys(laskut):
    value = laskut.vahennys(4,2)
    assert value == 2.0
    
def test_jakolasku(laskut):
    value = laskut.jakolasku(4,2)
    assert value == 2.0

def test_kertolasku(laskut):
    value = laskut.kertolasku(2,4)
    assert value == 8.0

def test_zero_division(laskut):
    with pytest.raises(ZeroDivisionError):
        assert laskut.jakolasku(2,0)

#if __name__ == "__main__":
#    import doctest
#    doctest.testmod()

