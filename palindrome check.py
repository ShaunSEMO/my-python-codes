user = input("Enter word here: ")
check = []
let = ''

for i in user:
	check.append(i)

def check_pal(word):
	word_rev = word[::-1]
	if word_rev == word:
		print(f'/n PALINDROME {let.join(check)} : {user}')
	else:
		print(f'/n NOT PALINDROME {let.join(check)} : {user}')

check_pal(check)