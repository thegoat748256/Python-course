
def isitPalendrome(string):
    left_pos = 0
    right_pos = len(string) - 1

    while right_pos>=left_pos:
         if not string[left_pos] == string[right_pos]:
              return False
         left_pos = left_pos + 1
         right_pos = right_pos - 1     
    return True
print(isitPalendrome("food"))              