def ispallindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False
print("test case 'madam'")
print('output ',ispallindrome('madam'))