class Solution:
    def shortestPalindrome(self, s: str) -> str:
        t = s[::-1]
        for i in range(len(s),-1,-1):
            if s[:i] == t[len(s)-i:]:
                # print(s[:i])
                # print(t[len(s)-i:])
                break
        return t[:len(s)-i]+s


def shortestPalindrome(s):
        t = s[::-1]
        for i in range(len(s),-1,-1):
            print("og: {0}".format(s[:i]))
            print("reversed: {0}".format(t[len(s)-i:]))
            if s[:i] == t[len(s)-i:]:
                break
        return t[:len(s)-i]+s

print(shortestPalindrome("aacecaaa"))