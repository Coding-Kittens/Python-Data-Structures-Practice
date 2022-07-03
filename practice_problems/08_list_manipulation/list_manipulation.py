

def list_manipulation(lst, command, location, value=None):
    """Mutate lst to add/remove from beginning or end.

    - lst: list of values
    - command: command, either "remove" or "add"
    - location: location to remove/add, either "beginning" or "end"
    - value: when adding, value to add

    remove: remove item at beginning or end, and return item removed

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'remove', 'end')
        3

        >>> list_manipulation(lst, 'remove', 'beginning')
        1

        >>> lst
        [2]

    add: add item at beginning/end, and return list

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'add', 'beginning', 20)
        [20, 1, 2, 3]

        >>> list_manipulation(lst, 'add', 'end', 30)
        [20, 1, 2, 3, 30]

        >>> lst
        [20, 1, 2, 3, 30]

    Invalid commands or locations should return None:

        >>> list_manipulation(lst, 'foo', 'end') is None
        True

        >>> list_manipulation(lst, 'add', 'dunno') is None
        True
    """
    command = command.lower()
    location = location.lower()
    list_item = None
    num = 0

    if location != 'end' and location != 'beginning':
        return list_item

    if location == 'end' and command == 'add':
        num = len(lst)
    elif location == 'end' and command == 'remove':
        num = len(lst)-1

    if command == 'remove':
        list_item =lst.pop(num)
    elif command == 'add':
         lst.insert(num,value)
         list_item =lst;

    return list_item
