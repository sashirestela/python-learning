from flat import Bill, Flatmate
from reports import PdfReport

amount = float(input('Enter the bill amount: '))
period = input('Enter the bill period: ')
name1 = input('Enter the name of the first flatmate: ')
name2 = input('Enter the name of the second flatmate: ')
days_in_house1 = int(input(f'How many days did {name1} stay in the house? '))
days_in_house2 = int(input(f'How many days did {name2} stay in the house? '))

the_bill = Bill(amount, period)
flatmate1 = Flatmate(name1, days_in_house1)
flatmate2 = Flatmate(name2, days_in_house2)

print(f'{flatmate1.name} pays:', flatmate1.pays(the_bill, flatmate2))
print(f'{flatmate2.name} pays:', flatmate2.pays(the_bill, flatmate1))

pdf_report = PdfReport(filename=f'{the_bill.period}.pdf')
pdf_report.generate(flatmate1, flatmate2, the_bill)
