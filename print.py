name = 'shaun'
surname = 'Moloto'

def out_put():
    count = 0
    for char in name:
        count += 1

    while count < len(name):
        characters = ''
        for char in name:
            characters += char
        print(characters)

out_put()
            
print('Hello World')
