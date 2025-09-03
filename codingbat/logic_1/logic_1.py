"""
This file contains all the solutions to problems
covered in "Logic-1" of CodingBat Python Exercises.
"""


class Solution:

    def cigar_party(self, cigars: int, is_weekend: bool) -> bool:
        """
        Determine if a squirrel party is successful based on the number of cigars and the day.

        A party is successful if:
          - On weekdays: the number of cigars is between 40 and 60 (inclusive).
          - On weekends: the number of cigars is at least 40 (no upper bound).

        Args:
            cigars (int): The number of cigars at the party.
            is_weekend (bool): True if the party is on a weekend, False otherwise.

        Returns:
            bool: True if the party is successful, False otherwise.
        """
        return cigars >= 40 if is_weekend else 40 <= cigars <= 60

    def date_fashion(self, you: int, date: int) -> int:
        """
        Determine whether you and your date can get a table at a restaurant
        based on your style ratings.

        Rules:
            - If either style rating is 2 or less → return 0 (no).
            - If either style rating is 8 or more → return 2 (yes).
            - Otherwise → return 1 (maybe).

        Args:
            you (int): Your stylishness rating (0–10).
            date (int): Your date's stylishness rating (0–10).

        Returns:
            int: 0 if no table, 1 if maybe, 2 if yes.
        """
        if you <= 2 or date <= 2:
            return 0
        elif you >= 8 or date >= 8:
            return 2
        return 1

    # Initial compact ternary solution - lacks clarity
    #  def date_fashion(you, date):
    #   return 0 if you <= 2 or date <= 2 else 2 if you >= 8 or date >= 8 else 1

    def squirrel_play(self, temp: int, is_summer: bool) -> bool:
        """
        Determine whether the squirrels in Palo Alto play based on temperature and season.

        Rules:
            - Normally: squirrels play if temperature is in [60, 90].
            - In summer: squirrels play if temperature is in [60, 100].

        Args:
            temp (int): The temperature.
            is_summer (bool): True if it is summer, False otherwise.

        Returns:
            bool: True if squirrels play, False otherwise.
        """
        return 60 <= temp <= 100 if is_summer else 60 <= temp <= 90

    def caught_speeding(self, speed: int, is_birthday: bool) -> int:
        """
        Determine the type of speeding ticket based on speed and birthday allowance.

        Args:
            speed (int): The driver's speed.
            is_birthday (bool): True if it's the driver's birthday (5 mph grace allowed).

        Returns:
            int: 0 = no ticket, 1 = small ticket, 2 = big ticket.
        """
        allowance = 5 if is_birthday else 0
        if speed <= 60 + allowance:
            return 0
        elif speed <= 80 + allowance:
            return 1
        return 2
