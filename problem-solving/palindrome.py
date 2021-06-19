def palindrome(x):
    if x < -(2**31 -1) or x >(2**31):
                return False
    else:
        if x < 0:
            return False
        else:
            rev = 0
            while x > 0:
                rem = x % 10
                rev = rev*10 + rem
                x //=10
            print(rev)
            if rev == x:
                return True
            else:
                return False