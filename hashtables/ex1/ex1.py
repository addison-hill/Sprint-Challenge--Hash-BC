#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(length)

    # insert takes in key, value - we want to store weight as key, index as value
    for j in range(len(weights)):
        hash_table_insert(ht, weights[j], j)

    # Now we have our hash table filled up with linked pairs (weight, index)
    # if hash_table contains entry for limit - weight use those two indexes, higher value index first
    for i in range(len(weights)):
        remainder = limit - weights[i]

        newWeight = hash_table_retrieve(ht, remainder)
        print(newWeight, i)
        # retrieve function returns the .value which in this case is the index
        if newWeight is not None:
            if newWeight > i:
                return (newWeight, i)
            else:
                return (i, newWeight)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
