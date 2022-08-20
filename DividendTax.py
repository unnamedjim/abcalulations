import json


class DividendTax:
    def __init__(self, profit):
        self.profit = profit

        f = open('taxes.json')
        tax_data = json.load(f)

        self.corporate_tax = float(tax_data['taxes']['corporate_tax']['rate'])
        self.capital_tax = float(tax_data['taxes']['capital_tax']['rate'])

        f.close()

        f = open('partners.json')
        partner_data = json.load(f)

        self.partners = partner_data['partners']

        f.close()

    def getTaxList(self):
        tax_list = []

        # Calculate corporate tax
        corporate_tax_amount = self.profit * self.corporate_tax
        tax_list.append(corporate_tax_amount)

        # Calculate dividend
        dividend = self.profit - corporate_tax_amount
        tax_list.append(dividend)

        # Calculate capital tax
        capital_tax_amount = dividend * self.capital_tax
        tax_list.append(capital_tax_amount)

        return tax_list

        

