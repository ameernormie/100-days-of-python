iterable = ['Spring', 'Summer', 'Autumn', 'Winter']
iterator = iter(iterable)
iterator    # <list_iterator object at 0x1029d4590>

next(iterator)      # 'Spring'
next(iterator)      # 'Summer'
next(iterator)      # 'Autumn'
next(iterator)      # 'Winter'
next(iterator)      # Exception:  StopIteration


def first(iterable):
    iterator = iter(iterable)
    try:
        return next(iterator)
    except StopIteration:
        raise ValueError("iterable is empty")
