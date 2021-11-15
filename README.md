# AirBnB clone - The console

![HNBN](https://github.com/zye7ert/AirBnB_clone/picture/HBNB-HolbertonAirbnb.png)

## First step and GOAl of this repository: Write a command interpreter to manage your AirBnB objects.

This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

### What’s a command interpreter?

Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object

### Resources
Read or watch:

* cmd module
* packages concept page
* uuid module
* datetime
* unittest module
* args/kwargs
* Python test cheatsheet

### Learning Objectives
* How to create a Python package
* How to create a command interpreter in Python using the cmd module
* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* How to manage datetime
* What is an UUID
* What is *args and how to use it
* What is **kwargs and how to use it
* How to handle named arguments in a function

###  Execution
***
Your shell should work like this in interactive mode:
```bash
$ ./console.py
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
(hbnb) 
(hbnb) quit
$
```
But also in non-interactive mode:
```bash
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
All tests should also pass in non-interactive mode:
`$ echo "python3 -m unittest discover tests" | bash`

![HNBN](https://github.com/zye7ert/AirBnB_clone/picture/SERVERSIDE.png)


### Authors
***
*Holberton School Students*

Edgar Flores - [zye7ert](https://github.com/zye7ert)
Giuliano Flores - [mrgiulls](https://github.com/mrgiulls)