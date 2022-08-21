import dividendtax
import messages
import salarytax

messages = messages.Messages()

# Welcome
print(messages.welcome)

# Get the profit
profit = 0


while True:
    profit = input(messages.get_profit)
    
    if profit.isdigit():
        if int(profit) > 0:
            break
        
    else:
        print(messages.not_int)


while True:
    pays_state_tax = input(messages.pays_state_tax)
    
    if pays_state_tax == 'j' or pays_state_tax == 'n':
        if pays_state_tax == 'j':
            pays_state_tax = True
        else:
            pays_state_tax = False
        break
    
    else:
        print(messages.not_j_n)


while True:
    member_of_church = input(messages.member_of_church)
    
    if member_of_church == 'j' or member_of_church == 'n':
        if member_of_church == 'j':
            member_of_church = True
        else:
            member_of_church = False
        break
    
    else:
        print(messages.not_j_n)


print("{:<25} {:>10}".format("", ""))
print("{:<25} {:>10}".format("", ""))
print("{:<25} {:>10}".format("", ""))
print("{:<25} {:>10}".format("", ""))
print("{:<25} {:>10}".format("", ""))

print(messages.happens_salary_this_year)

this_year_salary_tax = salarytax.SalaryTax(int(profit), pays_state_tax, member_of_church)

tax_list = this_year_salary_tax.get_tax_list_this_year()
print("{:<25} {:>10}".format("", ""))
print("{:<25} {:>10}".format(messages.profit, profit))
print("{:<25} {:>10}".format(messages.salary_tax, int(tax_list[0])))
print("{:<25} {:>10}".format("-----", "-----"))
salary = int(profit) - int(tax_list[0])
print("{:<25} {:>10}".format(messages.salary, salary))
print("{:<25} {:>10}".format("", ""))
print("{:<25} {:>10}".format(messages.community_tax, int(tax_list[1])))
print("{:<25} {:>10}".format(messages.regional_tax, int(tax_list[2])))
print("{:<25} {:>10}".format(messages.state_tax, int(tax_list[3])))
print("{:<25} {:>10}".format(messages.church_fee, int(tax_list[4])))
print("{:<25} {:>10}".format(messages.burial_fee, int(tax_list[5])))
print("{:<25} {:>10}".format("-----", "-----"))
salary_to_keep = salary - int(tax_list[1]) - int(tax_list[2]) - int(tax_list[3]) - int(tax_list[4]) - int(tax_list[5])
print("{:<25} {:>10}".format(messages.salary_to_keep, salary_to_keep))
print("{:<25} {:>10}".format("", ""))
print("{:<25} {:>10}".format("", ""))
print("{:<25} {:>10}".format("", ""))
print("{:<25} {:>10}".format("", ""))
print("{:<25} {:>10}".format("", ""))

next_year_dividend_tax = dividendtax.DividendTax(int(profit))
tax_list = next_year_dividend_tax.getTaxList()

print(messages.happens_dividends_next_year)
print("{:<25} {:>10}".format("", ""))
print("{:<25} {:>10}".format(messages.profit, profit))
print("{:<25} {:>10}".format(messages.corporate_tax, int(tax_list[0])))
print("{:<25} {:>10}".format("-----", "-----"))
print("{:<25} {:>10}".format(messages.dividend, int(tax_list[1])))
print("{:<25} {:>10}".format("", ""))
print("{:<25} {:>10}".format(messages.capital_tax, int(tax_list[2])))
print("{:<25} {:>10}".format("-----", "-----"))
salary_to_keep = int(profit) - int(tax_list[0]) - int(tax_list[2])
print("{:<25} {:>10}".format(messages.salary_to_keep, salary_to_keep))
