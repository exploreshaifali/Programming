def travel_linkedlist(curr):
    """Recursively travel to linkedlist."""
    if curr is None:
        return
    print(curr.data)
    travel_linkedlist(curr._next)
