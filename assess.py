def grade_average(grades):
    """ Write a program that returns the average number of a given list of grades.
    It should not add any negative grades to the average.

    Args:
        grades (list): List of grades to calculate
    """
    st_lst = grades[grades:]
    nd_lst = grades[:grades - 1]

    ave = st_lst + nd_lst // 2
    return ave


def find_prime_factors(number):
    """Write code to return the prime factors of the number.

    Args:
        number (int): Number to find the prime factors of
    """
    for i in range(number):
        if number % i == 0:
            return i



def calculate_interest(principal, rate, years):
    """Write a program that returns the compound interest

    Args:
        principal (int): The principal amount
        rate (int): The interest rate
        years (int): The amount of years to calculate the interest for
    """



def code_word(code):
    """Write a program that returns the word given a code.

    e.g. Given code: [3,1,20]
    Expected Word: "cat"

    Args:
        code (list): The code to decipher
    """
    alph = {1: "a", 3: "c", 16: "p", 25: "y", 20: "t", 8: "h",
    15: "o", 14: "n", 21: "u", 18: "r", 5: "e", 9: "i", 0: " ",
    4: "d"}

    for i in code:
        if i in code:
        


def triangles(length):
    """Write a program that returns a triangle of a certain length

    e.g. Input length = 5

    Expected Output: 
    *
    **
    ***
    ****
    *****

    Args:
        length (int): The ;ength your triangle should be
    """

    for c in range(length):
        column = print(c, end="")
        return column
        for r in length:
            row = print(r, "\n")
            return row


def hollow_triangle(length):
    """Write a program that returns a hollow triangle of a certain length

    e.g. Input length = 5

    Expected Output: 
    *
    **
    * *
    *  *
    *****

    Args:
        length (int): The ;ength your triangle should be
    """


# There are no tests for this function so test by running the program. 
def number_guessing(number):
    """Write a guessing game. The player has 10 opprtunites to guess.

    e.g. Number: 4
         User Input: 5
         Output: Incorrect

         Number: 4
         User Input: 4
         Output: Correct

    Args:
        number (int): The number to be guessed
    """

