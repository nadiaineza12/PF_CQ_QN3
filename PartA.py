def sum_from_to(first, last):
    # Calculate the sum of all integers from 'first' to 'last' inclusive
    if first > last:
        # If first is greater than last, swap them to ensure proper summation
        first, last = last, first
    return sum(range(first, last + 1))


