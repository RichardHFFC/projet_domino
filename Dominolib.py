from colors import bcolors

# class domino
class Domino:

    def __init__(self, number, land_one, king_one, land_two, king_two):
        self.number = number
        self.land_one = land_one
        self.king_one = king_one
        self.land_two = land_two
        self.king_two = king_two

    def __str__(self):
        if self.king_one == 3:
            kingOne = "***"
        elif self.king_one == 2:
            kingOne = "** "
        elif self.king_one == 1:
            kingOne = "*  "
        elif self.king_one == 0:
            kingOne = "   "
        if self.king_one == 3:
            kingOne = "***"
        elif self.king_one == 2:
            kingOne = "** "
        elif self.king_one == 1:
            kingOne = "*  "
        elif self.king_one == 0:
            kingOne = "   " 

        if self.land_one == 6:
            landOne = f"{bcolors.BBLACKB}C" + kingOne + f"{bcolors.BASE}"
        elif self.land_one == 5:
            landOne = f"{bcolors.BREDB}W" + kingOne + f"{bcolors.BASE}"
        elif self.land_one == 4:
            landOne = f"{bcolors.BPURPLEB}S" + kingOne + f"{bcolors.BASE}"
        elif self.land_one == 3:
            landOne = f"{bcolors.BBLUEB}W" + kingOne + f"{bcolors.BASE}"
        elif self.land_one == 2:
            landOne = f"{bcolors.BGREENB}F" + kingOne + f"{bcolors.BASE}"
        elif self.land_one == 1:
            landOne = f"{bcolors.BYELLOWB}W" + kingOne + f"{bcolors.BASE}"

        if self.king_two == 3:
            kingTwo = "***"
        elif self.king_two == 2:
            kingTwo = "** "
        elif self.king_two == 1:
            kingTwo = "*  "
        elif self.king_two == 0:
            kingTwo = "   "
        if self.king_two == 3:
            kingTwo = "***"
        elif self.king_two == 2:
            kingTwo = "** "
        elif self.king_two == 1:
            kingTwo = "*  "
        elif self.king_two == 0:
            kingTwo = "   " 

        if self.land_two == 6:
            landTwo = f"{bcolors.BBLACKB}C" + kingTwo + f"{bcolors.BASE}"
        elif self.land_two == 5:
            landTwo = f"{bcolors.BREDB}W" + kingTwo + f"{bcolors.BASE}"
        elif self.land_two == 4:
            landTwo = f"{bcolors.BPURPLEB}S" + kingTwo + f"{bcolors.BASE}"
        elif self.land_two == 3:
            landTwo = f"{bcolors.BBLUEB}W" + kingTwo + f"{bcolors.BASE}"
        elif self.land_two == 2:
            landTwo = f"{bcolors.BGREENB}F" + kingTwo + f"{bcolors.BASE}"
        elif self.land_two == 1:
            landTwo = f"{bcolors.BYELLOWB}W" + kingTwo + f"{bcolors.BASE}"
           
        return "| %s | %s | " % (landOne, landTwo)

class DominoOne():

    def __init__(self, land_one, king_one):
        self.land_one = land_one
        self.king_one = king_one

    def __str__(self):           
        if self.king_one == 3:
            kingOne = "***"
        elif self.king_one == 2:
            kingOne = "** "
        elif self.king_one == 1:
            kingOne = "*  "
        elif self.king_one == 0:
            kingOne = "   "
        if self.king_one == 3:
            kingOne = "***"
        elif self.king_one == 2:
            kingOne = "** "
        elif self.king_one == 1:
            kingOne = "*  "
        elif self.king_one == 0:
            kingOne = "   " 

        if self.land_one == 6:
            landOne = f"{bcolors.BBLACKB}C" + kingOne + f"{bcolors.BASE}"
        elif self.land_one == 5:
            landOne = f"{bcolors.BREDB}W" + kingOne + f"{bcolors.BASE}"
        elif self.land_one == 4:
            landOne = f"{bcolors.BPURPLEB}S" + kingOne + f"{bcolors.BASE}"
        elif self.land_one == 3:
            landOne = f"{bcolors.BBLUEB}W" + kingOne + f"{bcolors.BASE}"
        elif self.land_one == 2:
            landOne = f"{bcolors.BGREENB}F" + kingOne + f"{bcolors.BASE}"
        elif self.land_one == 1:
            landOne = f"{bcolors.BYELLOWB}W" + kingOne + f"{bcolors.BASE}"

        return "%s" % (landOne)

class DominoTwo():

    def __init__(self, land_two, king_two):
        self.land_two = land_two
        self.king_two = king_two

    def __str__(self):           
        if self.king_two == 3:
            kingTwo = "***"
        elif self.king_two == 2:
            kingTwo = "** "
        elif self.king_two == 1:
            kingTwo = "*  "
        elif self.king_two == 0:
            kingTwo = "   "
        if self.king_two == 3:
            kingTwo = "***"
        elif self.king_two == 2:
            kingTwo = "** "
        elif self.king_two == 1:
            kingTwo = "*  "
        elif self.king_two == 0:
            kingTwo = "   " 

        if self.land_two == 6:
            landTwo = f"{bcolors.BBLACKB}C" + kingTwo + f"{bcolors.BASE}"
        elif self.land_two == 5:
            landTwo = f"{bcolors.BREDB}W" + kingTwo + f"{bcolors.BASE}"
        elif self.land_two == 4:
            landTwo = f"{bcolors.BPURPLEB}S" + kingTwo + f"{bcolors.BASE}"
        elif self.land_two == 3:
            landTwo = f"{bcolors.BBLUEB}W" + kingTwo + f"{bcolors.BASE}"
        elif self.land_two == 2:
            landTwo = f"{bcolors.BGREENB}F" + kingTwo + f"{bcolors.BASE}"
        elif self.land_two == 1:
            landTwo = f"{bcolors.BYELLOWB}W" + kingTwo + f"{bcolors.BASE}"

        return "%s" % (landTwo)