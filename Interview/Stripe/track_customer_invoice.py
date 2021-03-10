'''
In HackerRank OA Stripe asked me to implement a program that would track customer's invoices. You are given a list of strings with billing info: action (CREATE, FINALIZE, PAY), id, amount, currency. Invoice can not be paid if it wasn't finalized or created. It can not be finalized if it wasn't created. For all invoices in USD you have to return total amount that is being owed to your the customer (created + finalized).
'''

'''
Verify the order in which the billing info is provided as input [The order of parameters amount, currency etc]. This should pass the last 2 test cases
'''