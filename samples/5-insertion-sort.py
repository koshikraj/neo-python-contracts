"""
In prompt.py, you need to execute `config sc-events on` to see the events showing up.

Description:
Simple implementation of insertion sort algorithm

Test & Build:
neo> build samples/5-insertion-sort.py test 10 07 False False [3,2,1,7,6,2,3
,4,1]
"""

def main(unsorted_list):
    index_u = 1
    while index_u < len(unsorted_list):
        item_u = unsorted_list[index_u]
        index_s = index_u - 1
        while index_s >= 0 and item_u < unsorted_list[index_s]:
            unsorted_list[index_s + 1] = unsorted_list[index_s]
            index_s -= 1
        unsorted_list[index_s + 1] = item_u
        index_u += 1
    return unsorted_list

