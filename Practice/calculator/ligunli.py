year_interest = 2 * 0.01
deposit = 10000
interval = 20

def all_money(deposit, interest, interval):
    current_money = deposit
    for i in range(interval):
        current_money = current_money + current_money * interest
    return current_money

print(all_money(deposit, year_interest, interval))