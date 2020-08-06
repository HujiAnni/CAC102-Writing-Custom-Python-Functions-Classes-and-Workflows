# Food items (prices in US dollars):

apples = 2.69
coffee = 8.99
bread = 2.99
lettuce = 3.19
cheese = 6.89

# Non-food items

pencils = 3.49
toothpaste = 3.89
shoelaces = 4.99
flowers = 7.99
soap = 1.29


nontaxable=apples+coffee+bread+lettuce+cheese
taxable=pencils+toothpaste+shoelaces+flowers+soap
tax_rate=0.08
total_cost=nontaxable+(1+tax_rate)*taxable
print(total_cost)

new_tax_rate=0.09
new_total_cost=nontaxable+(1+new_tax_rate)*taxable
print(new_total_cost)
