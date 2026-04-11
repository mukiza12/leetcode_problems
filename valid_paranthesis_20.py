#valid paranthesis leetcode
def is_valid(s: str) -> bool:

    #the first step is to map each bracket with its expected 
    # openin bracket

    matching = {

        ")" : "(",
        "]": "[",
        "}" : "{"

    }

    #2ndv-- step here I am going to use a stack to to verify
    #  unmatched opening brackets

    stack = []

    # step 3: here I am goin going to use a for loop 
    # to go through this

    for char in s:
        if char not in matching:

            stack.append(char)

        else:

            if not stack:
                return False
            
            top = stack.pop()

            if top != matching[char]:

                return False
            
    return len(stack) == 0

print(is_valid("()[]{}"))