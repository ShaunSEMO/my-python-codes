#!!WARNING!! THIS CODE MAY BE A REAL PAIN TO READ AND WORK WITH :(

class bank_account:
	def __init__(self, name, acc_num, balance):
		super(bank_account, self).__init__()
		self.name = name
		self.acc_num = acc_num
		self.balance = balance

	def withdraw(self, amount):
		self.balance = self.balance - amount
		return self.balance

	def deposit(self, amount):
		self.balance = self.balance + amount
		return self.balance

main_acc = bank_account('Absa', 12658, 10000)
savings_acc = bank_account('Savings', main_acc.acc_num, round(main_acc.balance/7,2))
business_acc = bank_account('Business', main_acc.acc_num, 7000)

def view_account(acc):
	print('\n			Main account\n 			+--------------------------+')
	print(f'			Bank name: {acc.name}')
	print('			+--------------------------+')
	print(f'			Account Number: {acc.acc_num}')
	print('			+--------------------------+')
	print(f'			Account balance: {acc.balance}')
	print('			+--------------------------+ \n')
	print('\n			What would you like to do?\n			1.Withdraw\n			2.Deposit\n			3.View sub-accounts\n\n			Type \'c\' to cancel!\n')

def view_sub_accounts(acc, acc2):
	print('\n	Savings account				Business account')
	print('	+--------------------------+		+--------------------------+')
	print(f'	Bank name: {acc.name}			Bank name: {acc2.name}')
	print('	+--------------------------+		+--------------------------+')
	print(f'	Account Number: {acc.acc_num}			Account Number: {acc2.acc_num}')
	print('	+--------------------------+		+--------------------------+')
	print(f'	Account balance: {acc.balance}		Account balance: {acc2.balance}')
	print('	+--------------------------+		+--------------------------+ \n')


view_account(main_acc)

while True:
	options = input('			Select options: ')

	if options == 'c':
		break

	elif options == '1':
		print('\n 			How much would you like to withdraw?')
		print('\n			1. R50		2. R100\n			3. R200		4. R400\n			5. Custom amount\n\n 			Type \'back\' to go back')
		amnt = input('			Select option: ')

		if amnt == '1':
			main_acc.withdraw(50)
		elif amnt == '2':
			main_acc.withdraw(100)
		elif amnt == '3':
			main_acc.withdraw(200)
		elif amnt == '4':
			main_acc.withdraw(400)
		elif amnt == '5':
			while True:
				how_much = input('			Enter amount: ')
				if int(how_much)%50 == 0:
					main_acc.withdraw(int(how_much))
					break
				else:
					pass
		elif amnt == 'b':
			pass
		view_account(main_acc)

	elif options == '2':
		while True:
			print(' 			Or type \'b\' to go back.')
			amnt = input('\n			Enter amount: ')
			try:
				amnt = int(amnt)
				if amnt%50 == 0:
					main_acc.deposit(amnt)
					break
				else:
					pass
			except ValueError:
				if amnt == 'b':
					view_account(main_acc)
					break
				else:
					print('			Please enter the amount or \'b\' to go back.')
		view_account(main_acc)

	elif options == '3':
		while True:
			view_sub_accounts(savings_acc, business_acc)
			print('\n			What would you like to do?\n			1.Withdraw\n			2.Deposit\n			Type \'c\' to cancel!\n')
			option = input(' 			Select option: ')
			while True:
				if option == '1':
					which_acc = input('\n 			Chooose account: ').lower()
					if which_acc == 'savings':
						amnt = input('\n 			Enter amount: ')
						try:
							amnt = int(amnt)
							if amnt%50 == 0:
								savings_acc.withdraw(amnt)
								view_sub_accounts(savings_acc, business_acc)
							else:
								pass
						except ValueError:
							if amnt == 'b':
								view_sub_accounts(savings_acc, business_acc)
							else:
								print('			Please enter the amount or \'b\' to go back.')
						view_account(main_acc)
					elif which_acc == 'business':
						amnt = input('\n 			Enter amount: ')
						try:
							amnt = int(amnt)
							if amnt%50 == 0:
								business_acc.withdraw(amnt)
								# view_sub_accounts(savings_acc, business_acc)
							else:
								pass
						except ValueError:
							if amnt == 'b':
								view_sub_accounts(savings_acc, business_acc)
							else:
								print('			Please enter the amount or \'b\' to go back.')
						view_account(main_acc)
					break
				elif option == 'c':
					view_account(main_acc)
					break
				elif option == '2':
					which_acc = input('\n 			Chooose account: ').lower()
					if which_acc == 'savings':
						amnt2 = input('\n 			Enter amount: ')
						try:
							while True:
								amnt2 = int(amnt2)
								if amnt2%50 == 0:
									savings_acc.deposit(amnt2)
									main_acc.withdraw(amnt2)
									break
						except ValueError:
							amnt2 = input('\n 			Enter amount: ')
						view_account(main_acc)
						break
					if which_acc == 'business':
						amnt2 = input('\n 			Enter amount: ')
						try:
							while True:
								amnt2 = int(amnt2)
								if amnt2%50 == 0:
									business_acc.deposit(amnt2)
									main_acc.withdraw(amnt2)
									break
						except ValueError:
							amnt2 = input('\n 			Enter amount: ')
						view_account(main_acc)
						break
			break
