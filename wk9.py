def roman_to_int(s):
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
        next_num = roman_map[s[i + 1]] if i + 1 < len(s) else 0

        if current_number >= next_num:
            converted_number += current_number
        else:
            converted_number -= current_number

    return converted_number


result = roman_to_int("IX")
print(result)  # Output: 9
