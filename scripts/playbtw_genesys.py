# Thanks for this to @barakisbrown - https://github.com/barakisbrown/GenesysDiceRoller

import random

BOOST = ["", "", "X", "XA", "AA", "A"]
SETBACK = ["", "", "F", "F", "T", "T"]
ABILITY = ["", "X", "X", "XX", "A", "A", "XA", "AA"]
DIFFICULTY = ["", "F", "FF", "T", "T", "T", "TT", "FT"]
PROFICIENCY = ["", "X", "X", "XX", "XX", "A", "XA", "XA", "XA", "AA", "AA", "TP"]
CHALLENGE = ["", "F", "F", "FF", "FF", "T", "T", "FT", "FT", "TT", "TT", "DR"]


class GenesysDiceRoller:
    __success = 0
    __failure = 0
    __advantages = 0
    __threat = 0
    __triump = 0
    __dispair = 0
    __netSuccess = 0
    __netAdvantages = 0
    __displayDiceRolled = []

    def __init__(self, dice_array):
        self.bdice = dice_array[0]  # BOOST
        self.sdice = dice_array[1]  # SETBACK
        self.adice = dice_array[2]  # ABILITY
        self.ddice = dice_array[3]  # DIFFICULTY
        self.pdice = dice_array[4]  # PROFICIENCY
        self.cdice = dice_array[5]  # CHALLENGE

    def display_results(self):
        """
        Determines how well the user did on the dice roll and then displays
        those results to the user via the console
        :return: Nothing
        """
        print("")
        rolled = 'Dice Rolled => (B/S/A/D/P/C):({}/{}/{}/{}/{}/{})'.format \
            (self.bdice, self.sdice, self.adice, self.ddice, self.pdice, self.cdice)
        print(rolled)
        # Following functions will roll the actual dice
        self.__roll_dice(self.bdice, BOOST)  # BOOST
        self.__roll_dice(self.sdice, SETBACK)  # SETBACK
        self.__roll_dice(self.adice, ABILITY)  # ABILITY
        self.__roll_dice(self.ddice, DIFFICULTY)  # DIFFICULTY
        self.__roll_dice(self.pdice, PROFICIENCY)  # PROFICIENCY
        self.__roll_dice(self.cdice, CHALLENGE)  # CHALLENGE

        # PRINT OUT RESULTS FROM THE DICE ROLLING
        print("You rolled the following => ", self.__displayDiceRolled)
        print("")
        print("Detailed Results")

        good_results = "Success = {}     Advantages = {}     Triumps = {}".format(self.__success, self.__advantages,
                                                                                 self.__triump)
        bad_results = "Failure = {}     Threats    = {}     Dispairs = {}".format(self.__failure, self.__threat,
                                                                                 self.__dispair)
        # NET RESULTS SECTION
        net_results = self.print_out_results()

        # Let's print out the final results
        print(good_results)
        print(bad_results)
        print("")
        print(net_results)

    def __roll_dice(self, times, list_type):
        """
        Rolls dice from the type list number of times
        :param times: Number of dice being rolled
        :param list_type:  Dice List
        :return:
        """
        if times != 0:
            for times in range(1, times + 1):
                dice = random.randint(0, len(list_type) - 1)
                rolled = list_type[dice]
                self.__determine_results(rolled)

    def __determine_results(self, rolled: object):
        """
        Takes a string of what was rolled and then interpret them so then it can be displayed correctly
        :param rolled: list of what was rolled that needs to be interpreted
        :return:
        """
        self.__displayDiceRolled.append(rolled)
        if rolled == '':
            return
        elif rolled == 'X':
            self.__success += 1
        elif rolled == 'XX':
            self.__success += 2
        elif rolled == 'XA':
            self.__success += 1
            self.__advantages += 1
        elif rolled == 'A':
            self.__advantages += 1
        elif rolled == 'AA':
            self.__advantages += 2
        elif rolled == 'F':
            self.__failure += 1
        elif rolled == 'FF':
            self.__failure += 2
        elif rolled == 'FT':
            self.__failure += 1
            self.__threat += 1
        elif rolled == 'T':
            self.__threat += 1
        elif rolled == 'TT':
            self.__threat += 2
        elif rolled == 'TP':
            self.__triump += 1
            self.__success += 1
        elif rolled == 'DR':
            self.__dispair += 1
            self.__failure += 1
        # COMPUTE NET INFORMATION
        self.__netAdvantages = (self.__advantages - self.__threat)
        self.__netSuccess = (self.__success - self.__failure)

    def print_out_results(self) -> object:
        """
        Displays a pretty printout of the results to the user
        :return: string containing the results
        """
        net_results = ""

        if self.__netSuccess > 0:
            net_results = net_results + "Congrats. You succeeded at your task. You rolled a total of "
            net_results = net_results + str(self.__netSuccess) + " successes"
        elif self.__netSuccess == 0:
            net_results = "Your roll did not either succeed or fail since you did not roll any successes or failures"
        else:
            net_results = "Sorry. You failed at the task. You rolled a total of " + str(
                abs(self.__netSuccess)) + " failures"
        if self.__netAdvantages < 0:
            net_results = net_results + "\n" + "You also generated a total of " + str(
                abs(self.__netAdvantages)) + " threats"
        else:
            net_results = net_results + "\n" + "You also generated a total of " + str(
                abs(self.__netAdvantages)) + " advantages"

        return net_results
