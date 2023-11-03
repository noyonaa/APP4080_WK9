def roman_to_int(s):
    # Create a dictionary to map Roman numerals to their integer values
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    converted_number = 0
    for i in range(len(s)):
        current_number = roman_map[s[i]]
        # Check if there is a next character in the string
        next_num = roman_map[s[i + 1]] if i + 1 < len(s) else 0

        # If the current Roman numeral is greater than or equal to the next one,
        # add its value to the converted number. Otherwise, subtract it.
        if current_number >= next_num:
            converted_number += current_number
        else:
            converted_number -= current_number

    return converted_number
