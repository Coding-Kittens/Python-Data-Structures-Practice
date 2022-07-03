def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """

    phrase = [char for char in phrase if char != ' ']
    phrase = ''.join(phrase)
    phrase = phrase.lower()

    reverse_phrase = list(phrase)
    print(reverse_phrase)
    reverse_phrase.reverse()
    reverse_phrase = ''.join(reverse_phrase)

    return reverse_phrase == phrase
