# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****
def hollow_square(n):
    return ""

# 1
# 12
# 123
# 1234
def number_pattern(n):
    return ""

# Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
def sum_of_natural_numbers(n):
    return ""

# Example for n = 4:
#    *
#   ***
#  *****
# *******
def centered_star_pyramid(n):
    result = ""

    for i in range (n):
        for j in range(n - i - 1):
            result += " "

        for k in range(2*i + 1):
            result += "*"
        result += "\n"

    return result.rstrip()

print(centered_star_pyramid(4))
