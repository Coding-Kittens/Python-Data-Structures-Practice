def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    phrase = phrase.strip()
    phrase_list = list(phrase)
    phrase_list[0] = phrase_list[0].upper()
    return ''.join(phrase_list)

    # return phrase.capitalize()
