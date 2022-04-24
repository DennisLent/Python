import random
import numpy as np


def pass_gen(length, capital=True, numbers=False, spec_sym=False, *, num_capitals=3, num_numbers=2, num_spec_sym=1):
    """
    Function to generate random password
    :param length: Length of password
    :param capital: use capitals
    :param numbers: use numbers
    :param spec_sym: use special symbols
    :arg num_capitals: amount of capital letters (default=3)
    :arg num_numbers: amount of numbers (default=2)
    :arg num_spec_sym: amount of special characters (default=1)
    :return: password string
    """

    if length <6:
        return f"length of {length} invalid. Use length > 6"

    def list_to_string(lst):
        string = ""
        for elem in lst:
            string += str(elem)
        return string

    specials = ["$", "%", "&", "/", "?", "^", "!"]
    nums = [i for i in range(10)]
    password = []

    while len(password) < length:
        password += chr(random.randint(97, 122))

    if capital:
        for n in range(num_capitals):
            i = random.randint(0, length-1)
            password[i] = password[i].capitalize()

    if numbers:
        for n in range(num_numbers):
            i = random.randint(0, length-1)
            j = random.randint(0, len(nums)-1)
            password[i] = nums[j]

    if spec_sym:
        for n in range(num_spec_sym):
            i = random.randint(0, length-1)
            j = random.randint(0, len(specials)-1)
            password[i] = specials[j]

    return list_to_string(password)


if __name__ == "__main__":
    tf = [True, False]
    for i in range(10):
        length = random.randint(12,20)
        c1, c2, c3 = random.choice(tf), random.choice(tf), random.choice(tf)
        print(f"Password of length {length} with capitals={c1}, numbers={c2}, special symbols={c3}")
        out = pass_gen(length, capital=c1, numbers=c2, spec_sym=c3)
        print(out)
