#!/usr/bin/python3
"""
function to check if data is UTF-8 validated
"""


def validUTF8(data):
    """check for utf-8 validation using bytes"""
    num_of_bytes_to_check = 0

    for byte in data:
        if num_of_bytes_to_check == 0:
            if byte >> 7 == 0b0:
                """singkr byte character (ASCII)"""
                continue
            elif byte >> 5 == 0b110:
                num_of_bytes_to_check = 1  # 2-byte character
            elif byte >> 4 == 0b1110:
                num_of_bytes_to_check = 2  # 3-byte character
            elif byte >> 3 == 0b11110:
                num_to_bytes_to_check = 3  # 4-byte character
            else:
                return False

        else:
            if byte >> 6 != 0b10:
                return False
            num_of_bytes_to_check -= 1
    return num_of_bytes_to_check == 0
