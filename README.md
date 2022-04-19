# python-tutorials

This repository contains
- *installation instructions* for a minimal python environment
- *Jupyter notebooks* to introduce the basic concepts of python
- *quizzes* to test the understanding of said concepts

It is related to my follow-up repository [data-science-tutorials](https://github.com/zieglerk/data-science-tutorials).

## Prerequisites
- access to a computing environment with installation rights
- programming experience, i.e. familiarity with basic concepts like
  control flow and data structures

## Leitfaden for a possible course

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

# Setup

## Choosing the proper installation candidate

We use [Python 3](https://www.python.org/) via the [Anaconda distribution](https://www.anaconda.com/).

## Installation Recipe (linux)

1. download the latest (64-bit) Anaconda3-installer from
   http://continuum.io/download and launch it with

	   $ bash Anaconda3-1.9.1-Linux-x86_64.sh

2. The installer will then ask ...
   - for your agreement on the license agreement
   - for a target directory (this is optional; default is `~/anaconda3`, my choice is `~/local/share/anaconda3`)
   - to run the `conda init` script to check/set some paths (obviously also optional) and if necessary add them to `.bashrc` (You may already have this, e.g. via .profile)
   
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

## Updating

The installer is for the full package coming with the `anaconda`
meta-package. Let's update it with :

    $ conda update anaconda



# Modules/Packages

Here's the full [package list](https://docs.anaconda.com/anaconda/packages/py3.6_linux-64/).

Anaconda is not only the name of the python-distribution, but also the
name of its largest meta-package. To maximize compatibility (and
minimize maintenance effort), we have the following priorities

1. packages from the standard library (see below)
2. packages from the anaconda meta-package (?packages marked as "In
   Installer"
   [here](https://docs.anaconda.com/anaconda/packages/py3.6_linux-64/ ?)
3. packages from conda's `default` channel, like `keras` (but not in the
   default installer's full list of packages?)
4. ONLY IF NECESSARY packages from selected additional conda channels
   (`r`, `bioconda`)

## Minimal Package List
   (for reference, when you have to reproduce your environment outside
   of anaconda, e.g. in `SageMath`)

### favorites from the standard library
   - `datetime`
   - `csv`

### non-standard packages in conda's default installation
    marked "In Installer" (I)

   - interface
     - `conda` (I)
     - `jupyter` (I)
   - math
     - `numpy` (I)
     - `scipy` (I)
	 - `statsmodels` (I)
   - data analysis
     - `pandas` (I)
     - `scikit-learn` `sklearn` (I)
   - visualization
     - `matplotlib` (I)
     - `seaborn` (I)

### non-standard packages in the default channel

   - `keras`


### OUTOFSCOPE alternative packages
    merely listed here for reference, because they might pop up repeatedly

   - [pybrain](http://pybrain.org/) by Jürgen Schmidhuber et.al. (latest release 0.3 dates from 18
     Nov 2009)


## Update

 :

     $ conda update conda
	 $ conda update anaconda

this confuses me (and others), so the current recommendation in
anaconda's blog[1] for "What 95% of People Want" is :

    $ conda update --all
	$ conda

[1]: https://www.anaconda.com/blog/developer-blog/keeping-anaconda-date/

Optionally :

    $ conda remove anaconda

And if things break :

    $ conda clean --all

# Development

## Command-Line Interface

- (default) python interactive shell
- MYCHOICE ipython shell

## Jupyter Notebook

web-application for interactive python worksheets

## Integrated Development Environment

- MYCOICE spyder, a quick [introduction](https://www.linuxjournal.com/content/introducing-spyder-scientific-python-development-environment) by Joey Bernard
- pycharm
- Eclipse with PyDev plugin
- Emacs with ...

Note: Spyder is already available in the standard installation, but if
   we want/need more advanced profiling, there's

   	   $ conda config --add channels spyder-ide
	   $ conda install -c spyder-ide spyder-line-profiler
	   $ conda install -c spyder-ide spyder-memory-profiler



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

### scikit-learn scikit-learn-intelex
machine learning, built to work well with NumPy and SciPy -- along with the [Intel extension](https://intel.github.io/scikit-learn-intelex/) for acceleration

### pandas
Pandas is a Python package providing fast, flexible, and expressive data structures designed to make working with “relational” or “labeled” data both easy and intuitive

### matplotlib
Matplotlib is a Python 2D plotting library which produces publication
quality figures in a variety of hardcopy formats and interactive
environments across platforms. Here's a short [introduction](http://pbpython.com/effective-matplotlib.html).

### keras
Keras is a high-level neural networks API, written in Python and
capable of running on top of either TensorFlow or Theano. It was
developed with a focus on enabling fast experimentation. Being able to
go from idea to result with the least possible delay is key to doing
good research.


## Further Non-Standard Libraries

### qutip

to simulate quantum systems. Very short
[introduction](https://www.linuxjournal.com/content/taking-python-next-level)
by Joey Bernard.


## Standard Library (Batteries Included)
see the complete list at https://docs.python.org/3/library/

### array
This module defines an object type which can compactly represent an array of basic values: characters, integers, floating point numbers. Arrays are sequence types and behave very much like lists, except that the type of objects stored in them is constrained.

### collections
This module implements specialized container datatypes providing
alternatives to Python’s general purpose built-in containers, dict,
list, set, and tuple.

### csv
import/export of csv-files

### itertools
This module implements a number of iterator building blocks inspired by constructs from APL, Haskell, and SML. Each has been recast in a form suitable for Python.

### math
It provides access to the mathematical functions defined by the C standard.

### multiprocessing
multiprocessing is a package that supports spawning processes using an API similar to the threading module.

### os
This module provides a portable way of using operating system dependent functionality.

### sys
This module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter. It is always available.

### time
This module provides various time-related functions.

### traceback
This module provides a standard interface to extract, format and print stack traces of Python programs. It exactly mimics the behavior of the Python interpreter when it prints a stack trace.



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
- [https://unsupervisedmethods.com/over-150-of-the-best-machine-learning-nlp-and-python-tutorials-ive-found-ffce2939bd78](Over 150 of the Best Machine Learning, NLP, and Python Tutorials I’ve Found)



# Books

- Swaroop, [A Byte of Python](https://python.swaroopch.com/), CC-BY-SA.
  (Free pdf and epub download, audience: programming beginners)
- Allen B. Downey, [Think
  Python](http://greenteapress.com/wp/think-python-2e/), 2nd edition,
  2015. (Cave: 1st edition uses python2. Free pdf and html download,
  sample code available on webpage and github, audience: python
  beginners with programming experience)
- Idris2016
- McKinney2012


# (Free) Courses

- Codecademy's [Python track](https://www.codecademy.com/learn/python)
- Udacity's [Intro to Computer
  Science](https://www.udacity.com/course/intro-to-computer-science--cs101)
- MIT's 6.001
  [Introduction to Computer Science and Programming in Python](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/)
  by Ana Bell, Eric Grimson, and John Guttag; "for students with little
  or no programming experience"; available on [edX](https://www.edx.org/course/introduction-computer-science-mitx-6-00-1x-10?utm_source=OCW&utm_medium=CHP&utm_campaign=OCW)
- MIT's 6.002
  [Introduction to Computational Thinking and Data Science](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/)
  by Ana Bell, Eric Grimson, and John Guttag; continuation of MIT
  6.001; archived on [edX](https://www.edx.org/course/introduction-computational-thinking-data-mitx-6-00-2x-5?utm_source=OCW&utm_medium=CHP&utm_campaign=OCW)



# Quizzes/Exercises/Generic Projects

- [15 single-choice questions](https://quiz.triplebyte.com/) by TripleByte
- [Mega Project List](https://github.com/karan/Projects) by Karan Goel
- [100 days of algorithms](https://medium.com/100-days-of-algorithms)
  by Tomáš Bouda with [github repository](https://github.com/coells/100days)



# TODOs
- [ ] check the setup part for anaconda & friends (let's say as number
  0)
- [ ] split every notebook into mandatory/optional part
- [ ] for numpy: improve didactical structures. Parts are redundant
  (e.g. operations), parts dont follow perfect logic order
  (broadcasting)
