def format_telefon(telefon: str):
    digits = ''.join(filter(str.isdigit, telefon))
    if len(digits) == 11 and digits.startswith('8'):
        digits = '7' + digits[1:]
    elif len(digits) == 10 and digits.startswith('9'):
        digits = '7' + digits
    formatted_telefon = '+{}({}){}-{}-{}'.format(
        digits[0], digits[1:4], digits[4:7], digits[7:9], digits[9:11]
    )

    return formatted_telefon
