#!/bin/bash

# Create folders for different categories
mkdir -p Arrays Strings LinkedLists Stacks Queues Trees Graphs HashTables Heaps Sorting Searching DynamicProgramming BitManipulation Greedy Backtracking

# Categorize files based on their names
for file in *.py *.java; do
    case "$file" in
        # Arrays
        KFrequent.py | SingleNumber.java | accounts_merge.py | backspace.py | buy_and_sell_stock.py | buyingstocks2.py | character_replacement.py | check_sequence.py | coin_change.py | combination_sum.py | container_with_most_water.py | contigarray.py | counting.py | gas_station.py | groupanagrams.py | insert_interval.py | islands_and_treasures.py | jump_game* | jumpgame.py | kokos_banans.py | kth_largest_element.py | largest_rectangle_area.py | last_stone_weight | letter_combinations.py | longest_increasing_path.py | longest_mountain.py | longest_sequence.py | longest_substring_without_repeating.py | make_board.py | max_area_of_island.py | max_product.py | max_stock_price_given_range.py | maximum_product_subarray.py | maximum_subarray.py | maxsubarray.py | median_finder.py | merge_intervals.py | middlelist.py | min_cost_connect_points.py | min_window_substring.py | minimum_difference_chocolates.py | move0s.py | non_overlapping_intervals* | nqueens.py | num_distinct_chars_subsequence.py | num_islands.py | organges_rotting.py | overlapping_intervals.py | partition_labels.py | partition_palindromes.py | partition_palindromic_strings.py | permutations_in_string.py | puzzles.py | remove_nth_from_end.py | search | search_2d_matrix* | search_rotated_sorted_array.py | shortest_path_while_avoiding_obstacles* | sort_colors.py | stoneweight.py | stringshift.py | subarray.py | surrounded_regions.py | swap_numbers.py | swim_in_water.py | target_sum.py | three_sum.py | two_sum.py | uniq_paths.py | word_break.py)
            mv "$file" Arrays ;;

        # Strings
        decode_ways_string_to_number | is_interleaving.py | is_palindrome*.py | valid_ip_address.py | valid_parentheses.py | word_dictionary.py)
            mv "$file" Strings ;;

        # Linked Lists
        LRUCache.java | reverse_linked_list.py)
            mv "$file" LinkedLists ;;

        # Stacks & Queues
        KNN.py | min_stack.py | minstack.py)
            mv "$file" Stacks ;;

        # Trees
        LCA.py | LCS.py | balanced_tree.py | binary_tree_max_path_sum.py | diameter_of_tree.py | diameterbinarytree.py | is_balanced.py | is_bst.py | level_order_traversal.py | maxpathsum.py | serialize_and_serialize_tree.py | subtree_of_another_tree.py)
            mv "$file" Trees ;;

        # Graphs
        clone_graph.py)
            mv "$file" Graphs ;;

        # Hash Tables
        course_schedule*.py | job_scheduling.py | task_scheduler.py)
            mv "$file" HashTables ;;

        # Heaps
        *)
            mv "$file" Heaps ;;

        # Sorting
        *)
            mv "$file" Sorting ;;

        # Searching
        *)
            mv "$file" Searching ;;

        # Dynamic Programming
        *)
            mv "$file" DynamicProgramming ;;

        # Bit Manipulation
        bitwiseand.py | count_bits.py | hamming_weight.py | happynumber.py | reverse_bits.py)
            mv "$file" BitManipulation ;;

        # Greedy
        *)
            mv "$file" Greedy ;;

        # Backtracking
        *)
            mv "$file" Backtracking ;;
    esac
done

# Create a README.md file
cat > README.md <<EOF
# Data Structures & Algorithms Interview Prep

This repository contains a collection of Python and Java code files organized into folders based on the data structures and algorithms they implement or utilize.

## Folder Structure

* **Arrays:** Problems and solutions related to arrays and array manipulation.
* **Strings:** Problems and solutions involving string processing and manipulation.
* **LinkedLists:** Problems and solutions related to linked lists.
* **Stacks:** Problems and solutions involving stacks.
* **Queues:** Problems and solutions involving queues.
* **Trees:** Problems and solutions related to trees (binary trees, binary search trees, etc.).
* **Graphs:** Problems and solutions related to graphs and graph algorithms.
* **HashTables:** Problems and solutions involving hash tables.
* **Heaps:** Problems and solutions involving heaps (priority queues).
* **Sorting:** Implementations of various sorting algorithms.
* **Searching:** Implementations of various searching algorithms.
* **DynamicProgramming:** Problems and solutions using dynamic programming techniques.
* **BitManipulation:** Problems and solutions involving bit manipulation.
* **Greedy:** Problems and solutions using greedy algorithms.
* **Backtracking:** Problems and solutions using backtracking algorithms.

## How to Use

1. Navigate to the relevant folder based on the data structure or algorithm you want to study.
2. Explore the code files in that folder to learn about different problem-solving approaches and implementations.
3. Feel free to modify and experiment with the code to deepen your understanding.

## Contributing

Contributions are welcome! If you have any code files related to data structures and algorithms that you'd like to add, please follow these steps:

1. Fork the repository.
2. Create a new branch for your changes.
3. Add your code files to the appropriate folder.
4. Update the README.md file if necessary.
5. Submit a pull request.

Happy coding!
EOF

echo "Categorization and README creation complete!"