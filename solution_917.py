class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        n = len(s)
        l = 0
        r = n - 1
        while l < r:
            if not s[l].isalpha():
                l += 1
            elif not s[r].isalpha():
                r -= 1
            else:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1

        return ''.join(s)

  #so the explanation is : string are immutable so we convert into a list to exchange the element by their indices.
  # this is a classic 2 pointers approach. the 1st pointer will always be at the index 0 and 2nd pointer will be at last index
  # while l and r are gonna be at the index then the while loop exits for example l is at 4 and r is at 4 then while loop exits
#if we found l is not an alphabet we increment it by 1 as well as if we found r is not an alphabet we decrease it by 1
# if there are alphabets we simply exchange them and increment l by 1 and decrement r by 1
# time complexity - o(n) traverse over the list
#space - o(n) we creating a string list and again making it to a string as well
