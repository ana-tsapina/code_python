

start_money = float(input("How much money did you have originally? "))
cookies_sold = input("How many cookies did you sell? (Enter in string format please ex. ccc ")

big_cookies = cookies_sold.count('b')
cookies = cookies_sold.count('c')


# for current_cookie in cookies_sold: 
#    #print(current_cookie)
#     if current_cookie == "c": 
#         cookies += 1
#     elif current_cookie == "b": 
#         big_cookie += 1
#     else: 
#         print(f"{current_cookie} is not a valid sale item.")

total_cookies = big_cookies + cookies 

profit = (big_cookies * 1.25) + (cookies * 0.75)
end_day = start_money + profit

print(f"We sold {total_cookies} cookies. We made ${profit}. We now have {end_day}! ")

