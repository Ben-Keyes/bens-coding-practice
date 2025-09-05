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

    def sorta_sum(self, a: int, b: int) -> int:
        """
        Return the sum of two integers, except if the sum is in the range 10..19 inclusive,
        in which case return 20.

        Args:
            a (int): The first integer.
            b (int): The second integer.

        Returns:
            int: The sum of a and b, or 20 if the sum is in the range 10..19.
        """
        return 20 if 10 <= a + b <= 19 else a + b

    def alarm_clock(self, day: int, vacation: bool) -> str:
        """
        Determine the alarm time based on the day of the week and vacation status.

        Rules:
            - Weekdays (Mon–Fri):
                - Normal: "7:00"
                - Vacation: "10:00"
            - Weekends (Sat, Sun):
                - Normal: "10:00"
                - Vacation: "off"

        Args:
            day (int): Day of the week (0=Sun, 1=Mon, ..., 6=Sat).
            vacation (bool): True if on vacation, False otherwise.

        Returns:
            str: The alarm time as "7:00", "10:00", or "off".
        """
        if vacation:
            return "off" if day in {0, 6} else "10:00"
        return "10:00" if day in {0, 6} else "7:00"

    def love6(self, a: int, b: int) -> bool:
        """
        Determine whether two integers are related to the number 6.

        Rules:
            - Return True if either number is 6.
            - Return True if their sum is 6.
            - Return True if their absolute difference is 6.

        Args:
            a (int): The first integer.
            b (int): The second integer.

        Returns:
            bool: True if the numbers meet the conditions, False otherwise.
        """
        return a == 6 or b == 6 or a + b == 6 or abs(a - b) == 6

    def in1to10(self, n: int, outside_mode: bool) -> bool:
        """
        Determine whether a number falls within a range or outside based on mode.

        Rules:
            - Normal mode: return True if 1 <= n <= 10.
            - Outside mode: return True if n <= 1 or n >= 10.

        Args:
            n (int): The number to check.
            outside_mode (bool): True if checking outside the range, False otherwise.

        Returns:
            bool: True if the condition is satisfied, False otherwise.
        """
        if outside_mode:
            return n <= 1 or n >= 10
        return 1 <= n <= 10

    def near_ten(self, num: int) -> bool:
        """
        Determine whether a number is within 2 of a multiple of 10.

        Rules:
            - Return True if num % 10 is 0, 1, 2, 8, or 9.
            - Return False otherwise.

        Args:
            num (int): A non-negative integer.

        Returns:
            bool: True if num is within 2 of a multiple of 10, False otherwise.
        """
        return num % 10 <= 2 or num % 10 >= 8
