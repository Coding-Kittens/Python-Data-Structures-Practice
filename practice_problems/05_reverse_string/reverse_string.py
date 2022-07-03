def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    phraselist =list(phrase)
    phraselist.reverse()
    return ''.join(phraselist)
