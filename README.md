# 0x00. AirBnB clone - The console
## Brief
|  **This** _README_ **will contain all the information about this project, the tasks, the study material...<br>
We will do our best to explain everything that went into this project in great details.**  |
## Description
****
  -  By: GUILLAUME
  -  Weight: 5
  -  Project to be done in teams of 2 people (your team: OUALID ELHADIM , Asmaa Hadar)
****
## General
- How to create a Python package
- How to create a command interpreter in Python using the `cmd` module
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- How to manage `datetime`
- What is an `UUID`
- What is `*args` and how to use it
- What is `**kwargs` and how to use it
- How to handle named arguments in a function
****
### PACKAGES
- **Dotted method**<br>
		We use the doted notation to do the import.<br>
			```import my_math.abs```<br>
			```my_math.abs.my_abs(89)```<br>
		Let's say the structure of our folder is the following:
			```script.py```<br>
			```model/```<br>
			```|__ add.py```<br>
		in order to import our function from the add.py file, we need to do the following statements.
			```import model.add```
		In this case we need to use our function like this :<br>
			```model.add.add(9)```<br>
		But the best way to do it is the following :<br>
			```from model.add import add
			add(9)```
