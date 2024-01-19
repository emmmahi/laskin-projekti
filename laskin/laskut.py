""" Tämä on yksikertainen laskin
yhteen-, vähennys, kerto- ja jakolaskuille.
"""
from typing import Union
class Laskin:
    """ Tämä on yksinkertainen Laskin luokka
    """

    def summa(self, luku1:Union[float,int], luku2:Union[float,int]) -> float:
        """Metodi yhteenlaskua varten

        Examples:
            >>> Laskin().summa(3,2)
            5.0
            >>> Laskin().summa(-2, -1)
            -3.0
            >>> Laskin().summa(100, 101)
            201.0
        """
        return float(luku1 + luku2)


    def vahennys(self, luku1:Union[float,int], luku2:Union[float,int]) -> float:
        """ Metodi vähennyslaskua varten

        Eaxmples:
            >>> Laskin().vahennys(5,2)
            3.0
            >>> Laskin().vahennys(-3,-3)
            0.0
            >>> Laskin().vahennys(100, 98)
            2.0
        """
        return float(luku1 -luku2)

    def kertolasku(self, luku1:Union[float,int], luku2:Union[float,int]) -> float:
        """ Metodi kertolaskua varten

        Examples:
            >>> Laskin().kertolasku(3,5)
            15.0
            >>> Laskin().kertolasku(4,0)
            0.0
            >>> Laskin().kertolasku(2.5, 2)
            5.0
        """
        return float(luku1 * luku2)

    def jakolasku(self, luku1:Union[float,int], luku2:Union[float,int]) -> float:
        """ Metodi jakolaskua varten

        Examples:
            >>> Laskin().jakolasku(4,2)
            2.0
            >>> Laskin().jakolasku(9,3)
            3.0
            >>> Laskin().jakolasku(1,0)
            Traceback (most recent call last):
            .
            ZeroDivisionError: division by zero
        """
        return float(luku1/luku2)
        # else:
        #     raise ZeroDivisionError
