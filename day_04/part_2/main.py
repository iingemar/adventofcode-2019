import math


class PasswordChecker:
    def __init__(self, password):
        self.password = password
        self.password_str = str(self.password)

    def is_ok(self):
        return self.is_six_digits() and self.has_two_adjacent_digits() and self.never_decrease()

    # It is a six-digit number.
    def is_six_digits(self):
        return int(math.log10(self.password))+1 == 6

    # Two adjacent digits are the same (like 22 in 122345).
    def has_two_adjacent_digits(self):
        adjacent_counter = 1
        for idx, char in enumerate(self.password_str):
            if idx == (len(self.password_str) - 1):
                return False
            next_character = self.password_str[idx + 1]
            if char == next_character:
                adjacent_counter += 1
            else:
                # When no more adjacent digits, check how many
                adjacent_counter = 1

        return False

    # Going from left to right, the digits never decrease; they only ever increase or stay the same.
    def never_decrease(self):
        for idx, char in enumerate(self.password_str):
            # If we are at the last digit, the password is ok
            if idx == (len(self.password_str) - 1):
                return True
            next_character = self.password_str[idx + 1]
            if int(char) > int(next_character):
                return False
        return True


if __name__ == "__main__":
    # Your puzzle input is 206938-679128.
    ok = 0
    for psw in range(206938, 679129):
        if PasswordChecker(psw).is_ok():
            ok += 1
    print(ok)

