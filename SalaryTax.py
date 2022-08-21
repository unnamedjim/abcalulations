import json


class SalaryTax:
    def __init__(self, profit, pays_state_tax = True, pays_church_fee = True):
        self.profit = profit
        self.pays_state_tax = pays_state_tax
        self.pays_church_fee = pays_church_fee

        f = open('taxes.json')
        tax_data = json.load(f)

        self.corporate_tax = float(tax_data['taxes']['corporate_tax']['rate'])
        self.salary_tax = float(tax_data['taxes']['salary_tax']['rate'])
        self.community_tax = float(tax_data['taxes']['community_tax']['rate'])
        self.regional_tax = float(tax_data['taxes']['regional_tax']['rate'])
        self.state_tax = float(tax_data['taxes']['state_tax']['rate'])
        self.church_fee = float(tax_data['taxes']['church_fee']['rate'])
        self.burial_fee = float(tax_data['taxes']['burial_fee']['rate'])

        f.close()

    def get_tax_list_this_year(self):

        tax_list = []

        # Calculate Salary Tax
        salary_tax_amount = self.profit * (1 - (1 / (1 + self.salary_tax)))
        tax_list.append(salary_tax_amount)

        # Calculate the salary
        salary = self.profit - salary_tax_amount

        # Calculate community tax
        community_tax_amount = salary * self.community_tax
        tax_list.append(community_tax_amount)
        
        # Calculate regional tax
        regional_tax_amount = salary * self.regional_tax
        tax_list.append(regional_tax_amount)

        # Calculate state tax
        if self.pays_state_tax:
            state_tax_amount = salary * self.state_tax
        else:
            state_tax_amount = 0

        tax_list.append(state_tax_amount)

        # Calculate church fee
        if self.pays_church_fee:
            church_fee_amount = salary * self.church_fee
        else:
            church_fee_amount = 0

        tax_list.append(church_fee_amount)

        # Calculate burial fee
        burial_fee_amount = salary * self.burial_fee
        tax_list.append(burial_fee_amount)

        return tax_list