# python-tutorials

This repository contains
- *installation instructions* for a minimal python environment
- *Jupyter notebooks* to introduce the basic concepts of python
- *Quizzes* to test the understanding of said concepts

Prerequisites
- access to a computing environment with installation rights
- programming experience, i.e. familiarity with basic concepts like
  control flow and data structures

# Leitfaden/Guideline

  :

    +--Motivation
       Installation Instruction
       Programming Environments
    +--Data Types
       Control Flow
       Modules
    +--package NumPy
    +--package SciPy
    +--package scikit-learn
    +--package matplotlib (Python plotting, object-oriented)
    +--package pandas (Python Data Analysis Library)


# Version

There are currently two major versions of Python. The older Python2 and
the newer Python3. We use Python3, where the latest stable release is
3.6.0 (as of 12 Mar 2017).

1. download latest Anacond3-installer from
   http://continuum.io/downloads and :

	   $ bash Anaconda3-1.9.1-Linux-x86_64.sh

(optionally) with target `~/local/share/anaconda3`.

2. the installer then suggests to prepend the path in .bashrc. (You
   may already have this, e.g. via .profile)
3. Next, we'll add three channels to the default one (in this order) :

    $ conda config --add channels conda-forge
	$ conda config --add channels defaults
	$ conda config --add channels r
	$ conda config --add channels bioconda

   `bioconda` is for bioinformatics (what's your requirement?) and
   will receive the highest priority. `r` is
   required for bioinformatics and contains moduls for the GNU R
   programming language. The `defaults` channel already contains
   plenty of packages (?TODO list?). Finally, `conda-forge` contains
   several community-build packages that are not already in the
   `default` channel.

Here's the full [package list](https://docs.continuum.io/anaconda/pkg-docs).

The installer is for the full package coming with the `anaconda`
meta-package. Let's update it with :

    $ conda update anaconda

Anaconda is not only the name of the python-distribution, but also the
name of its largest meta-package. To maximize compatibility (and
minimize maintenance effort), we have the following priorities

1. packages from the standard library (see below)
2. packages from the anaconda meta-package (?packages marked as "In
   Installer" [here](https://docs.continuum.io/anaconda/pkg-docs)?)
3. packages from conda's default channel, like `keras` (but not in the
   default installer's full list of packages?)
4. packages from selected additional conda channels (`r`, `bioconda`)

## Update

 :

     $ conda update conda
	 $ conda update anaconda

# Packages
are called *modules* in python

## Favorite Non-Standard Packages

### NumPy
fast numerical computing, in particular with large arrays and matrices; is part of SciPy, but can also be loaded individually

References:
- Nicolas P. Rougier, [From Python to
  Numpy](http://www.labri.fr/perso/nrougier/from-python-to-numpy/)

### SciPy
(large) scientific computing library, based on NumPy arrays (and including NumPy)

### scikit-learn
machine learning, built to work well with NumPy and SciPy

### pandas
Pandas is a Python package providing fast, flexible, and expressive data structures designed to make working with “relational” or “labeled” data both easy and intuitive

### matplotlib
Matplotlib is a Python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms.

### keras
Keras is a high-level neural networks API, written in Python and capable of running on top of either TensorFlow or Theano. It was developed with a focus on enabling fast experimentation. Being able to go from idea to result with the least possible delay is key to doing good research.

## Standard Library (Batteries Included)
### math
It provides access to the mathematical functions defined by the C standard.

### sys
This module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter. It is always available.

### traceback
This module provides a standard interface to extract, format and print stack traces of Python programs. It exactly mimics the behavior of the Python interpreter when it prints a stack trace.

### array
This module defines an object type which can compactly represent an array of basic values: characters, integers, floating point numbers. Arrays are sequence types and behave very much like lists, except that the type of objects stored in them is constrained.

### time
This module provides various time-related functions.

### os
This module provides a portable way of using operating system dependent functionality.

### collections
This module implements specialized container datatypes providing alternatives to Python’s general purpose built-in containers, dict, list, set, and tuple.

### itertools
This module implements a number of iterator building blocks inspired by constructs from APL, Haskell, and SML. Each has been recast in a form suitable for Python.

### multiprocessing
multiprocessing is a package that supports spawning processes using an API similar to the threading module.

# Other Tutorials/Exercises

- [Scipy Lecture Notes](http://www.scipy-lectures.org/) for Python,
  NumPy, Matplotlib, Scipy (with exercises)
- [Code Challenge](https://github.com/pybites/challenges/tree/master/01)
- [Python Tutorial](https://docs.python.org/3.6/tutorial/index.html) at
  python.org (quite complete and extensive; probably to read
  selectively)
- basic [Python Class](https://developers.google.com/edu/python/) by Google
- DataCamp has two Python Courses (for Data Science):
  [Intro](https://www.datacamp.com/courses/intro-to-python-for-data-science)
  and
  [Intermediate](https://www.datacamp.com/courses/intermediate-python-for-data-science)
- After Hours Programming has an interactive [Python
  Tutorial](http://www.afterhoursprogramming.com/tutorial/Python/Overview/)
- LearnPython.org has an interactive [Python
  Tutorial](http://www.learnpython.org/)

# Books
- Swaroop, [A Byte of Python](https://python.swaroopch.com/), CC-BY-SA.
  (Free pdf and epub download, audience: programming beginners)
- Allen B. Downey, [Think
  Python](http://greenteapress.com/wp/think-python-2e/), 2nd edition,
  2015. (Cave: 1st edition uses python2. Free pdf and html download,
  sample code available on webpage and github, audience: python
  beginners with programming experience)

# Free Online Courses
- Codecademy's [Python track](https://www.codecademy.com/learn/python)
- Udacity's [Intro to Computer
  Science](https://www.udacity.com/course/intro-to-computer-science--cs101)

# Exercises/Generic Projects
- Karan Goel's [Mega Project List](https://github.com/karan/Projects)


# TODOs
- [X] pull every jupyter notebook with number from python-for-data-science
- [ ] check the setup part for anaconda & friends (let's say as number 0)

for numpy
- improve didactical structures. Parts are redundant (e.g. operations), parts dont follow perfect logic order (broadcasting)
