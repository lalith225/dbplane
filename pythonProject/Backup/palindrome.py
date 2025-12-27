def is_palindrom(x):
    if x < 0:
        print("Not a Palindrome")
        return 0
    reveresed_x = int(str(x)[::-1])
    if x == reveresed_x:
        print("Is Palindrome")
    else:
        print("Not Palidrome")


is_palindrom(-121)