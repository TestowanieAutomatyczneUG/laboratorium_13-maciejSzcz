class Roman(object):
    def check_guess(self, letters, user_guess):
        if type(user_guess) != str:
            raise TypeError("guess must be of string type")
        elif type(letters) != int:
            raise TypeError("letters must be of int type")

        values = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        symbols = ["M", "CM", "D", "CD", "C", "XC",
                "L", "XL", "X", "IX", "V", "IV", "I"]
        roman = ''
        i = 0
        while letters > 0:
            for _ in range(letters // values[i]):
                roman += symbols[i]
                letters -= values[i]
            i += 1

        if user_guess == roman:
            return True
        else:
            return False
