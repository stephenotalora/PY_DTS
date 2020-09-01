# test input 'azcbobobegghakl'

def longest_alphabetical_substr(s):
    z = 1     # fast pointer
    x = y = 0  # slow pointers
    substr = longeststr = ''

    while z < len(s):
        char_a = s[y]
        char_b = s[z]

        if char_a <= char_b:  # include repeating characters
            substr = s[x:z]   # create substring from x to z
            y = y + 1         # increment the slow pointer
            if z + 1 < len(s) and s[z + 1] < s[z]:
                substr = substr + s[z]
            elif z == len(s) - 1:
                substr = substr + s[len(s) - 1]
        else:
            # otherwise... we found an edge
            x = y = z  # reset slow ptrs to the the fast ptr
            longeststr = substr if len(substr) > len(
                longeststr) else longeststr  # update longest substr
            substr = ''

        z = z + 1  # increment the fast pointer

    return substr if not x else longeststr
