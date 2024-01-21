import doctest
import math


def weighted_round_robin(
        rights: list[float],
        valuations: list[list[float]],
        y: float):
    """
    Perform a weighted round-robin allocation based on valuations and player rights.

    Args:
        rights (list[float]): List of rights for each player.
        valuations (list[list[float]]): 2D list of valuations where each sublist represents
                                       the valuations of a player for each item.
        y (float): Constant used in the allocation formula.

    Returns:
        None

    Example: (same rights, same valuations)
        >>> rights = [1, 1, 1]
        >>> valuations = [[11, 22, 33, 44, 55],
        ...               [11, 22, 33, 44, 55],
        ...               [11, 22, 33, 44, 55]]
        >>> weighted_round_robin(rights, valuations, 1)
        player 0 takes item 4 with value 55
        player 1 takes item 3 with value 44
        player 2 takes item 2 with value 33
        player 0 takes item 1 with value 22
        player 1 takes item 0 with value 11



    Example: (same rights, different valuations)
        >>> rights = [1, 1, 1]
        >>> valuations = [[11, 11, 22, 33, 44],
        ...               [11, 22, 44, 55, 66],
        ...               [11, 33, 22, 11, 66]]
        >>> weighted_round_robin(rights, valuations, 1)
        player 0 takes item 4 with value 44
        player 1 takes item 3 with value 55
        player 2 takes item 1 with value 33
        player 0 takes item 2 with value 22
        player 1 takes item 0 with value 11

    Example: (different rights, same valuations)
        >>> rights = [2, 3, 5]
        >>> valuations = [[11, 22, 33, 44, 55],
        ...               [11, 22, 33, 44, 55],
        ...               [11, 22, 33, 44, 55]]
        >>> weighted_round_robin(rights, valuations, 1)
        player 2 takes item 4 with value 55
        player 1 takes item 3 with value 44
        player 2 takes item 2 with value 33
        player 0 takes item 1 with value 22
        player 2 takes item 0 with value 11


    Example: (different rights, different valuations)
        >>> rights = [1, 2, 4]
        >>> valuations = [[11, 15, 22, 90, 44],
        ...               [39, 22, 44, 55, 66],
        ...               [11, 51, 22, 77, 66]]
        >>> weighted_round_robin(rights, valuations, 1)
        player 2 takes item 3 with value 77
        player 1 takes item 4 with value 66
        player 2 takes item 1 with value 51
        player 2 takes item 2 with value 22
        player 0 takes item 0 with value 11
        """

    def f(s):
        return s + y

    num_of_products = len(valuations[0])
    curr_products = [0] * len(rights)
    curr_result = [0] * len(rights)

    for i in range(num_of_products):
        for j in range(len(rights)):
            curr_result[j] = rights[j] / f(curr_products[j])

        index_max_result = curr_result.index(max(curr_result))
        index_max_product = valuations[index_max_result].index(max(valuations[index_max_result]))
        curr_products[index_max_result] += 1

        print(f"player {index_max_result} takes item {index_max_product} with value {valuations[index_max_result][index_max_product]}")

        for list1 in valuations:
            list1[index_max_product] = -math.inf


if __name__ == '__main__':
    # doctest
    doctest.testmod()

    # A simple example
    rights = [1, 2, 4]
    valuations = [[11, 11, 22, 33, 44],
                 [11, 22, 44, 55, 66],
                 [11, 33, 22, 11, 66]]
    weighted_round_robin(rights, valuations, 1)
