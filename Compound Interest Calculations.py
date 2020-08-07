def compound_by_period(balance,rate,num_periods):
    compound_list=[1]
    for n in range (0,num_periods):
        balance = balance * (1 + rate)
        compound_list.append(balance)
    return compound_list

def change_per_period(compound_list):
    new_list=[compound_list[n]-compound_list[n-1] for n in range(1, len(compound_list))]
    return new_list

wheat=compound_by_period(1,1,63)
new_list_wheat=change_per_period(wheat)

print(wheat)
total_wheat=sum(wheat)

balance_list=compound_by_period(100,0.03,10)
change_of_balance=change_per_period(balance_list)


