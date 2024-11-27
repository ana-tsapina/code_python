def check(num): 
  def test(num, divider): 
    if num == divider:
        return True 
    else: 
        if num % divider == 0: 
            return False
        else: 
            return helper(num, divider+2)

    if num == 1: 
        return False
    elif num in {2,3}
        return True
    elif num % 2 == 0: 
        return False
    else: 
        return helper(num, 3)
