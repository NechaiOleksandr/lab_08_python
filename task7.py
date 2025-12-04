class DecimalToRoman:
    def convert(self, number):
        values = [1000, 500, 100, 50, 10, 5, 1]
        chars = ['M', 'D', 'C', 'L', 'X', 'V', 'I']

        roman = ''
        i = 0

        while number > 0:
            count = number // values[i]
            roman += chars[i] * count
            number -= values[i] * count
            i += 1

        return roman


class RomanToDecimal:
    def convert(self, roman):
        values = [1000, 500, 100, 50, 10, 5, 1]
        chars = ['M', 'D', 'C', 'L', 'X', 'V', 'I']

        number = 0
        prev_value = 0

        for char in reversed(roman):
            i = chars.index(char)
            current_value = values[i]
            if current_value < prev_value:
                number -= current_value
            else:
                number += current_value

            prev_value = current_value

        return number

decimal = DecimalToRoman()
print(decimal.convert(1952))
roman = RomanToDecimal()
print(roman.convert('VL'))