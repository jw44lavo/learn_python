learn_python
============
Welcome to **learn_python** - a small repository about learning python or programming in general. This is a guide for absolute, brutal, complete beginners. So see this as an onset to finally start to learn programming.  

This is work in progress.  

# Table of Contents
* [Terminology](#terminology)
* [General Advice](#general-advice)
* [Getting Started](#getting-started)
    * [Windows](#windows)
    * [Ubuntu](#ubuntu)
    * [Hello World!](#hello-world)

# Terminology
At first we need to know about some technical terms, which are used commonly when talking about programming.  

**Script**: A script is a file, which contains assignments and instructions you wrote there. It includes all of your code in a certain language and forms a kind of protocol of tasks.  

**Language**: A language is a certain type of speaking to your computer. There are hundreds of programming languages and several language types as well. Details are not important at the beginning, but you should know following: Here you can see an introduction to Python.  

**Python**: Python is the programming language presented here. It focuses on code readability, why it is often used as an entry-language. There are Python 2.7 and Python 3.x. This guide is about Python 3.x. You will probably learn about the difference later on.


# General Advice
The process of learning to program comes with an advantage and disadvantage at the same time. You just need to do it. And you will fail frequently. By learning from a book solely or without making mistakes on your own, you won't proceed.  

## Practice
The best way to practice programming is by giving yourself little problems or tasks. A very fun approach is [**Advent of Code**](https://adventofcode.com/) - just try it out. Alternatively you can get creative and design your own challenges.

## Help
Some would say, that programming is just about searching for the right stuff at Google. If you are stuck at a problem or never programmed what you want to program, just ask your favorite search engine. Most time of programming is about looking for the right thread at [**stack overflow**](https://stackoverflow.com/).  


# Getting Started
After sorting out the general stuff, we can come the programming itself. Nearly. At first you need to install Python, if you never done it before. Additionally, you need a software for text editing (not mandatory but recommended).  

## Windows
### Install Python
Visit Pythons download for the latest release (click [here](https://www.python.org/downloads/release/python-391/) for 3.9.1), scroll down to the bottom of the page and download the right installer according to your operating system. Execeute the downloaded .exe file and follow the instructions. Check the installed version in the CMD with ```python --version``` or ```python3 --version```.  

### Install VSCode
Using [Visual Studio Code](https://code.visualstudio.com/) for text editing is just a recommendation. You can also use any other text editor such as [Atom](https://atom.io/), [Sublime](https://www.sublimetext.com/) or preinstalled software.  

Download the right installer according to your operating system from https://code.visualstudio.com/Download (Windows, 32- or 64-bit, User Installer). Execute the downloaded .exe file and follow the instructions.  

### Execute your first Script
Create a new directory on your Desktop named 'learning_python'. Open VSCode and create a new file in the new directory named 'hello_world.py'. Copy following code to the file and save the progress:
```python
print('Hello World!')
```
Open a CMD (Windows+R, type 'cmd', press Enter), navigate to your python script and execute it by following code:
```cmd
cd Desktop\learning_python
python hello_world.py
```
Alternatively, try ```python3 hello_world.py```.  

Congratulations, you executed your first python script! You are ready to go further steps.  

## Ubuntu
### Install Python
Python 3.x comes preinstalled in the latest versions of Ubuntu. Check the version by opening a terminal and executing ```python --version```. If Python 3.x is not installed, execute ```sudo apt install python3.9``` (3.9 is the latest version). Check the version again with ```python --version``` or ```python3 --version```.  

### Install VSCode
Open the Ubuntu Software Center. Type 'vscode', select 'Visual Studio Code', install it. Done.

### Execute your first Script
Create a new directory on your Desktop named 'learning_python'. Open VSCode and create a new file in the new directory named 'hello_world.py'. Copy following code to the file and save the progress:
```python
print('Hello World!')
```
Open a terminal (Ctrl+Alt+T), navigate to your python script and execute it by following code:
```bash
cd Desktop/learning_python
python hello_world.py
```
Alternatively, try ```python3 hello_world.py```.  

Congratulations, you executed your first python script! You are ready to go further steps.  

## Hello World!
The mother of learning a new programming language is about learning how to print out "Hello World!". It's holy programmers' codex. So just do it!  