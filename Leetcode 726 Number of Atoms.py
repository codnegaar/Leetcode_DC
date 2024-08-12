'''
Leetcode 726 Number of Atoms

Given a string formula representing a chemical formula, return the count of each atom.
The atomic element always starts with an uppercase character, then zero or more lowercase letters, representing the name.
One or more digits representing that element's count may follow if the count is greater than 1. If the count is 1, no digits will follow.
For example, "H2O" and "H2O2" are possible, but "H1O2" is impossible. Two formulas are concatenated together to produce another formula.

For example, "H2O2He3Mg4" is also a formula. A formula placed in parentheses, and a count (optionally added) is also a formula.

For example, "(H2O2)" and "(H2O2)3" are formulas. Return the count of all elements as a string in the following form: the first name (in sorted order),
followed by its count (if that count is more than 1), followed by the second name (in sorted order), followed by its count (if that count is more than 1), and so on.
The test cases are generated so that all the values in the output fit in a 32-bit integer.

 

Example 1:
        Input: formula = "H2O"
        Output: "H2O"
        Explanation: The count of elements are {'H': 2, 'O': 1}.
        
Example 2:
        Input: formula = "Mg(OH)2"
        Output: "H2MgO2"
        Explanation: The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.
        
Example 3:
        Input: formula = "K4(ON(SO3)2)2"
        Output: "K4N2O14S4"
        Explanation: The count of elements are {'K': 4, 'N': 2, 'O': 14, 'S': 4}.
 

Constraints:
        1 <= formula.length <= 1000
        formula consists of English letters, digits, '(', and ')'.
        formula is always valid.

'''

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        n: int = len(formula)
        element_count: dict[str, int] = {}
        stack: list[dict[str, int]] = []
        i: int = 0

        while i < n:
            char: str = formula[i]

            if char == "(":
                # Start of a new group
                stack.append({})
                i += 1
            elif char == ")":
                # End of a group, process multipliers
                i += 1
                multiplier: str = ""
                while i < n and formula[i].isdigit():
                    multiplier += formula[i]
                    i += 1
                multiplier = int(multiplier) if multiplier else 1

                # Merge counts from the current group to the previous context
                current_group = stack.pop()
                if stack:
                    target = stack[-1]
                else:
                    target = element_count
                
                for elem, count in current_group.items():
                    if elem in target:
                        target[elem] += count * multiplier
                    else:
                        target[elem] = count * multiplier
            else:
                # Parse element and its count
                start = i
                i += 1
                while i < n and formula[i].islower():
                    i += 1
                element = formula[start:i]

                count_str = ""
                while i < n and formula[i].isdigit():
                    count_str += formula[i]
                    i += 1
                count = int(count_str) if count_str else 1

                if stack:
                    if element in stack[-1]:
                        stack[-1][element] += count
                    else:
                        stack[-1][element] = count
                else:
                    if element in element_count:
                        element_count[element] += count
                    else:
                        element_count[element] = count

        # Construct the output string
        result = []
        for elem in sorted(element_count):
            count = element_count[elem]
            result.append(elem)
            if count > 1:
                result.append(str(count))

        return "".join(result)
