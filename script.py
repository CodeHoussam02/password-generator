import random
import string
from time import sleep 
from rich.console import Console
from rich.text import Text
# password generator 
# note : password should contain at least half of it chars
app: str = " Password Generator "
# create the string of characters 
letters_chars: str = string.ascii_letters
special_chars: str = string.digits + string.punctuation
# get the number of chars in the password from the user
print(f'{app:-^50}') 
num_chars: int = int(input('| Enter the number of chars : '))
# define the num of chars that should be on the password
amount_chars: int = num_chars / 2
# define the trigger, pass variable
trigger: int  = 0
password: str = ''
# start generating the password 
while trigger < num_chars: 
	while trigger < amount_chars:
		rand_char: str = random.choice(letters_chars)
		password += rand_char
		trigger += 1
	rand_spec: str = random.choice(special_chars)
	password += rand_spec
	trigger += 1
# shell 
console = Console()
tasks = [f"Building password stage {n + 1}" for n in range(6)]

with console.status("[dots2] Working on it ...") as status:
		while tasks:
			task = tasks.pop(0)
			sleep(1)
			console.log(f"{task} complete")

# display the generated password
text = Text()
text.append(f'-> Password Generated is : {password}', 'bold green')
console.print(text)

