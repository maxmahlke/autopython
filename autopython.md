---
title: The Astronomer's Guide to python
author: Max Mahlke
date: 2021-09-02
extensions:
  - image_ueberzug
---
.


![20](gfx/astronomy_status_board.png)

.

Astronomy reduced to the realm of booleans. Credit: [xkcd](https://xkcd.com/2469/)

---

# Before we begin

- Hi, I'm Max


- How do you open the terminal on your computer?


- What's a boolean?


- What is the boolean value of 1.4 in python?


- What is the difference between a list and a set in python?


- Lecture notes are at https://github.com/maxmahlke/autopython


---

# Motivation

## The Age of Digital Astronomy

- Astronomy today is a digital world: the CCD has replaced the human eye at the lower end of the telescope


- There are terabytes of observations produced each night and evaluated in real-time


- A new set of skills is required for today's astronomer: digital data processing and analysis


- This is true for all fields (planetary astronomy, stellar physics, galaxies and the Universe) and all stages of the career (Master student, PhD, postdoc, permanent)


- Yet: most astronomers do _not_ have a computer science qualification. They are in general self-taught.

---

# Motivation

## Learn to code

- Programming is the day-to-day work of an astronomer: process data, analyse data, create figures, ...


- Being skilled in a programming language makes your daily tasks more efficient and enjoyable


- Coding is fun


Keep in mind:


- Learning to code is not a one-off task: it takes years and never really stops. Languages develop and new tools show up.

---

# Motivation

## Learn to code *python*

There are many programming languages: Fortran, C, C#, C++, JavaScript, IDL, R, python, Julia, Go, and more. Some are better suited for certain tasks than others.

Subjective reasons to learn `python`:

1\. `python` is easy to read and write.

```python

    colours = ["blue", "black", "red"]

    for colour in colours:
        print(f"My favourite colour is {colour}")
```

Output:

```shell
    My favourite colour is blue
    My favourite colour is black
    My favourite colour is red
```

This makes it easier to learn.

---

# Motivation

## Learn to code *python*

There are many programming languages: Fortran, C, C#, C++, JavaScript, IDL, R, python, Julia, Go, and more. Some are better suited for certain tasks than others.

Subjective reasons to learn `python`:

2\. There is a rich package ecosystem: most of the work has been done for you already.

- You want to analye the data in a CSV file? The ``pandas`` package helps
  you out.

- You are observing stars and want to extract their absolute magnitudes
  from FITS images? The ``photutils`` package has functions for this.

- You have to convert the equatorial coordinates of a source to galactic ones while
  precessing the equinox of the coordinate frame from ``J1975`` to ``J2000``? Try
  ``astropy.coordinates``.

---

# Motivation

## Learn to code *python*

There are many programming languages: Fortran, C, C#, C++, JavaScript, IDL, R, python, Julia, Go, and more. Some are better suited for certain tasks than others.

Subjective reasons to learn `python`:

3\. It has a large user base, meaning it will continue to progress and develop.

Results from the 2020 *StackOverflow Developer Survey*: What programming language do you use [multiple answers possible]?: `python` is the number one for data analysis (42% of developers use it).

---

# Motivation

## Learn to code *python*

There are many programming languages: Fortran, C, C#, C++, JavaScript, IDL, R, python, Julia, Go, and more. Some are better suited for certain tasks than others.

Subjective reasons to learn `python`:

4\. It's free. It's accessible. All the code you have can be inspected on your computer.

---

# Motivation

## Learn to code *python*

There are many programming languages: Fortran, C, C#, C++, JavaScript, IDL, R, python, Julia, Go, and more. Some are better suited for certain tasks than others.

Objective reason to **not** learn `python`:

It is slow compared to languages like FORTRAN, C, C++. Personally: my time is
more valuable than the CPU time. If I can write code quicker, I don't mind if it
takes longer to execute.

And it's really not that slow.

---

# Scope of the course

## Today

- ~~Why you should learn to code~~


- ~~Why learn python over other languages~~


- A minimal introduction to `python`


- `python` on your system: what is installed and how to execute it


- When things go wrong: understanding error messages


- The quick look at the `python` standard library


- Highlight of third-party `python` packages


- Best Practices for coding in general and `python` in particular


- Tools for coding: editors, `jupyter notebooks`, `ipython`


- Exercises for the following week

---

# Scope of this course

## Next Thursday

- Discussion of exercises: you present your solutions, I present mine


- ?


Q&A, advanced topics, live exercises, the command line and UNIX...


## Not covered

- `python` syntax: too much to cover in 3 hours (and would make for boring lectures)


- Basic UNIX commands: `cd`, `ls`, `mkdir`, `grep`, `sed`, `awk`, ... Again, too much to cover, but I highly recommend learning how to navigate the command line!

---

# A minimal introduction to `python`

## What is `python`?

Three key properties define `python`:

1\. _interpreted language_: executed line by line rather than compiling a binary executable


2\. _high-level_: no need for memory allocation or variable typing, `python` does it for you


3\. _object-oriented_: coding revolves around classes which are well separated from each other

---

# A minimal introduction to `python`

## Data Types

Used to store data in variables and to run operations on these
variables. A subset of existing data types are:

```python
x = 4                                               # int    (integer)
y = 4.3                                             # float  (floating point value)
z = "hello world"                                   # str  (string)
today_is_thursday = True                            # bool (boolean)
chars_and_numbers = ["a", "b", "c", "c", 1, 2, 3]   # list
phonebook = {"Alice": 61234567, "Bob": 68765432}    # dict (dictionary)
first_four_of_alphabet = {"a", "b", "c", "d"}       # set
```

To get the type of a variable, use the `type()` function:

``` python
>>> type(y)
<class 'float'>
```

`python` supports _dynamic typing_:

``` python
a = 3
a = "now I'm a string"
```

This makes `python` easier to write at the cost of execution time.

---

# A minimal introduction to `python`

## Control Flow

To control the order of execution of your `python` commands. The most basic two cases: `if`-clause and `for`-loop

### `if`-clause

``` python
today_is_thursday = True

if today_is_thursday:
    print("Today is not Friday.")

else:
    print("Today might be Friday.")

    print("I will go to the beach.")  # executed if today_is_thursday is False

print("I will study some python.")    # always executed
```

Note:

- The two clauses (`if` and `else`) are terminated with colons.
- Their context is indicated by the indentation of the line.
- Consistent levels of indentation (2 or 4 spaces) have to be used.
- Nesting clauses require an extra level of indendation
- `python` is super readable

---

# A minimal introduction to `python`

## Control Flow

To control the order of execution of your `python` commands. The most basic two cases: `if`-clause and `for`-loop

### `for`-loop

A common pattern is to iterate over the elements in a `list`.

``` python
weekdays = ["monday", "tuesday", "wednesday", "thursday", "friday"]

for day in weekdays:

    if day == "tuesday":
        print("Today is Tuesday.")

    else:
        print(f"Today is not Tuesday. It is {day}.")
```

Over the execution of the `for`-loop, the `day` variable stores the value of the elements of the list one-by-one.

---

# A minimal introduction to `python`

## Where to continue from here?

There  are _lots_ of resources online to help you learn `python`. Some of the better ones are:

- The official tutorial from the `python` documentation: Extensive, often a bit too detailed for a beginner

- Codecademy's course on `python3`: Interactive, step-by-step guide to the language. This is how I learnt the basics.

- Automate the Boring Stuff with `python`: a popular beginner's guide to the language

The links are in the course notes.

Finally, I recommend YouTube: search for _pyCon_ ("python conference") and pick a talk which sounds interesting to you. It is my preferred way to learn more about
`python` and keep up with new developments.

---

# `python` on your system

## `python2` versus `python3`


Use `python3`. `python2` was already outdated when I started to learn `python` 10 years ago.

---

# `python` on your system

## Which `python3` version?

You will already have `python` installed on your system. Run the following in the command line to get the version.

``` bash
$ python3 --version
```

I like to stay on the latest stable release (`3.9`), and I recommend a version `>=3.7`.

Several versions can be installed simultaneously: `python3.7`, `python3.8`, ...
Only one is referred to as `python3` by your system. When in doubt: type the complete executable name.

---

# `python` on your system

## `python` files

- `python` scripts carry the `.py` suffix


- `python` may create a directory called `__pycache__/`, which serves to speed up the execution of a script in later runs. Feel free to leave it or delete it.

---

# `python` on your system

## Executing `python`

As `python` is an interpreted language, there are two ways to run code:

- Using the interactive interpreter

  ``` bash
  $ python3
  ```

- Passing the path to a script to the interpreter

  ``` bash
  $ python3 my_script.py
  ```

`python` executes code line-by-line and stops if it finds an error

---

# `python` on your system

## Packages and modules

`python` code is separated into _modules_. Modules are `python` files on your system containing functions, classes, and other functionality.

To use a function from a module in your script, you `import` it.

``` python
>>> import math
```

You access the `python` objects in a module through the _dot notation_.

``` python
>>> math.pi
3.141592653589793
>>> math.sin(math.pi / 2)
1.0
```

Some modules have submodules (i.e. more `python` files) which are again accessed via the dot notation.

``` python
>>> import os.path
```


---

# `python` on your system

## Installing packages

`python` has a _standard library_ of modules such as the `math` and `os` modules.
To extend your library, you can install third-party _packages_. A package is a collection of modules.

To install a package, you use `pip` ("pip installs packages").
To install `pip` itself, execute

``` python
$ wget https://bootstrap.pypa.io/get-pip.py  # download an installer script
$ python3 get-pip.py # execute the installer script
$ rm get-pip.py # delete the installer script
```

Now, to install a package, run

``` python
$ python3 -m pip install [package_name]
```

A good first package to install is the `numpy` package, which contains many mathematical and numerical calculation functions for `python`.

``` python
$ python3 -m pip install numpy
```

Ensure that this worked by running

``` python
>>> import numpy
```

If a module is missing on your system, `python` will raise the `ModuleNotFoundError` on the `import` line.

---

# When things go wrong

## Understanding `python` error messages

The most common opportunity to learn something new.

`python` error messages are generally easy to understand.

``` python
>>> 4 / 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
```

The message contains three parts: _traceback_, _error type_, and _error message_

- traceback: rundown of the error's origin in the script. Includes the filename of the script and the line where the error occurred.

  ```
  $ python3 my_script.py
  Traceback (most recent call last):
    File "my_script.py", line 4, in <module>
      x = math.sqrt(-3)
  ValueError: math domain error
  ```

It may point to the wrong line if you edit the script while it is executing (which is perfectly fine).

---

# When things go wrong

## Understanding `python` error messages

The most common opportunity to learn something new.

`python` error messages are generally easy to understand.

``` python
>>> 4 / 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
```

The message contains three parts: _traceback_, _error type_, and _error message_

- _error type_: first part of last line. These are `python` objects with descriptive names (e.g. `FileNotFoundError`). Quite common are also

  - `SyntaxError`: you made a typo

  - `ValueError`: passing a variable with an invalid value

  - `TypeError`: passing a variable with an invalid type

  - `IndexError`: for example, trying to access the fifth element in a list with four
entries

---

# When things go wrong

## Understanding `python` error messages

The most common opportunity to learn something new.

`python` error messages are generally easy to understand.

``` python
>>> 4 / 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
```

The message contains three parts: _traceback_, _error type_, and _error message_

- _error message_: Written by the developer. This is what you put into google if you cannot fix the error yourself.

---

# When things go wrong

## Fixing the error

Three steps to resolve your error:

1. Are you calling the function correctly? In the interactive interpreter, import the module and use the `help()` function to show the documentation.

    ```python
    >>> import math
    >>> help(math.sqrt)
    ```

2. Are you variables what you think they are? Place a `breakpoint()` just before the offending line and execute the script. This will trigger the interactive interpreter at the line of the `breakpoint()`, with all the variables available as in the interactive interpreter. Use `n` to execute the next line of code, `c` to continue, and `q` to quit.

    ```python
    breakpoint()
    ```

3. Google the error message. Typically, someone has had this issue before you and was nice enough to post the solution to a page like [StackOverflow](https://stackoverflow.com).

---

# The `python` standard library

The _standard library_ refers to the classes and functions which are distributed with `python` and maintained
by the `python` core developers. It comes equipped with many modules for system management, network management, debugging, and more.

Some modules and functions which I use frequently are given below.

- `os`: This modules contains many functions for interacting with your operating system.

  ```python
  >>> import os
  >>> dir_home = os.path.expanduser("~/")  # get the path to the home directory
  >>> os.listdir(dir_home)  # list the contents of the home directory
  ...
  ```


- `collections.Counter()`: Given an iterable (e.g. a `list`), it returns a `dict` with the elements as keys and the number of times they appear in the iterable as values.

  ```python
  >>> from collections import Counter
  >>> zoo = ["monkey", "elephant", "giraffe", "monkey", "tiger", "elephant", "monkey", "lion"]
  >>> Counter(zoo)
  Counter({"monkey": 3, "elephant": 2, "giraffe": 1, "tiger": 1, "lion": 1})
  ```


- `time.time()`: Get the current system time. Useful to time the execution of your scripts.


- `sys.exit()`: Used to gracefully exit a script.

---

# Third-party packages

## `numpy`

- `numpy` is likely the most popular third-party package in `python`


- It completely replaces the standard `math` module and adds new data types such as the `array`


- The `numpy.array` is everywhere in `python` and is frequently used as replacement of the `list`, as it behaves more like a vector


```python
>>> import numpy as np
>>> vector1 = np.array([1, 2, 3])
>>> vector2 = np.array([1, 2, 3])
>>> vector1 + vector2      # arrays
array([2, 4, 6])
>>> [1, 2, 3] + [1, 2, 3]  # lists
[1, 2, 3, 1, 2, 3]
```
---

# Third-party packages

## `matplotlib`

- _The_ gold-standard for creating figures in `python`


- Create quick-look plots of data or publication-ready works-of-art


- Watch out: creating and perfectioning figures is addictive.


- Highly recommend: https://github.com/matplotlib/cheatsheets


```python
>>> import matplotlib.pyplot as plt
>>> import numpy as np
>>> x = np.linspace(0, 2*np.pi, 100)  # get 100 points evenly spaced between 0 and 2 pi
>>> plt.plot(x, np.sin(x), color="blue", label="Sine")
>>> plt.plot(x, np.cos(x), color="red", label="Cosine")
>>> plt.legend()
>>> plt.show()
```

---

# Third-party packages

## `pandas`

- Whenever you have a table of data, such as a `CSV` file


- Adds the `pandas.DataFrame`


- There's a bit of a learning curve and some unintuitive quirks, but then it's irreplacable


```python
>>> import pandas as pd
```
---

# Third-party packages

## `scipy`

- For your higher mathematical needs: fast-fourier transform, curve fitting, integration, linear algebra, and more.

```python
>>> from scipy import integrate
```

---

# Third-party packages

## `astropy`


- The astronomer's toolbox in `python`


- Computing astronomical source coordinates in different systems at different epochs, analyze observations with time series, common astronomical models


- Plenty of functionality to read and edit `FITS` files.


```python
>>> from astropy.io import fits
```

- Get started at https://learn.astropy.org

---

# Best practices

The earlier you stick to this, the better.

## Writing _pythonic_ code

- "pythonic" code refers to code which makes use of `python`'s unique and built-in features


- Example: people coming from C-languages will overuse indices when writing `python`

```python
colours = ["blue", "black", "red"]

i = 0  # don't do this

for colour in colours:
    i += 1 # don't do this
    print(f"{i}: My favourite colour is {colour}")
```

```python
colours = ["blue", "black", "red"]

for i, colour in enumerate(colours):  # do this instead
    print(f"{i}: My favourite colour is {colour}")
```

- Recommended talk: Raymond Hettinger - _Transforming Code into Beautiful, Idiomatic Python_

---

# Best practices

The earlier you stick to this, the better.

## Comment everything // it's a great idea

- You will write code on Friday which you cannot understand on Monday


- Comment the meta-level of your code: not details, but what is it achieving


- Avoid obvious comments:

![15](gfx/comment.png)


---

# Best practices

The earlier you stick to this, the better.

## Choose meaningful variable names

Compare

```python
et = 50  # in s
```

to

```python
exposure_time = 50  # in s
exp_time = 50  # in s
```

---

# Best practices

The earlier you stick to this, the better.

## Avoid magic numbers

- Similar to meaningful variable names

```python
electrons = 5 * 30  # ?
```

versus

```python
exposure_time = 30  # in s
rate = 5  # in electrons / s
electrons = rate * exposure_time
```

---

# Best practices

The earlier you stick to this, the better.

## Properly format your code

- Apart from indentation, `python` is quite liberal with the syntax: `'` or `"` for strings are accepted, whitespaces and newlines can vary


- There is a style-guide, referred to as PEP8. It is the standard and leads to pretty code.


- Personal recommendation: I use an autoformatter called `black` which formats the code on every save. I never have to worry about it. You can get autoformatters for almost any code editor.

---

# Tools for developing `python`

## Your editor

- A subjective decision and often topic of heated debates: your favourite editor


- There are many good options to choose from. In the beginning, I recommend editors which have supporting features like code completion, documentation lookups, variable inspection.


- These are popular choices:

  - [Atom](https://atom.io)

  - [Sublime Text 4](https://www.sublimetext.com)

  - [Visual Studio Code](https://code.visualstudio.com)

  - [PyCharm](https://www.jetbrains.com/pycharm/)

---

# Tools for developing `python`

## Your interactive interpreter

`ipython` is a common replacement for the standard `python` interpreter. It has
some nice features like TAB-completion of commands and syntax highlighting.

```bash
$ python3 -m pip install ipython
```

Remember: when you stumble over a new `python` package, software, tool, anything, take some time to look through the documentation. You will see what it offers, how to use it, and save yourself time in the long run!

---

# Tools for developing `python`

## `jupyter` and its notebooks

- Popular tool for developing `python`, running in your browser


- Based on cells which can have different content: `python` code, LaTeX, markdown text. Good for documenting and "telling a story" with your code


- Cells can be executed separately, which saves execution time


```bash
$ python3 -m pip install jupyter
$ jupyter notebook
```

---

# Exercises

Aim: to simulate (1) common tasks like simulating, fitting, plotting data, and (2) realizing that an existing solution is suboptimal and improving it

# Task 1: Simulating, fitting, and displaying data

- Take 100 random samples of a sine curve with an amplitude and a period of your choosing
- Add Gaussian noise to the samples. The noise should have a mean of 0 and a standard deviation equal to 10% of the sine curve signal
- Fit your simulated data with a sine curve
- Create a figure which displays the simulated data and the fitted sine curve
- In the figure, add the best fit parameters and their errors

# Task 2: The Fibonacci Numbers

- Define a function which accepts an integer `n` as argument and returns the value of the `n`th Fibonacci number `F_n`.
- Compute `F_{40}`. Print its value and the time it took to compute it.
- It takes a while. As Raymond Hettinger would say, "there must be a better way"! Get the computation time to less than one second.
