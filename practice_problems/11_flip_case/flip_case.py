def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    phrase_list = []
    for char in phrase:
        if char.upper() == to_swap.upper():
            if char.islower():
                phrase_list.append(char.upper())
            else:
                phrase_list.append(char.lower())
        else:
            phrase_list.append(char)


    return ''.join(phrase_list)
