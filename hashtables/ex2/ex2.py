#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    # insert takes in key, value we can insert (starting location, destination)
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    # Now we have all our tickets in hashtable, now we need to set up our route
    # We can find first by retreiving the key with NONE
    first_flight = hash_table_retrieve(hashtable, "NONE")

    # We can find the next location by using retrieve of route[i-1]

    # ith location can be found by checking hash for i - 1th location...might need to cleanup to pass tests
    for i in range(length):
        if i < 1:
            route[i] = first_flight
        else:
            next_flight = hash_table_retrieve(hashtable, route[i-1])
            route[i] = next_flight

    route.remove("NONE")
    return route
