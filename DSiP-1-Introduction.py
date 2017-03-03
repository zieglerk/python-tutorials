
# coding: utf-8

# # Data Science in Python
# 
# by 
# 
# [__Michael Granitzer__ (michael.granitzer@uni-passau.de)]( http://www.mendeley.com/profiles/michael-granitzer/)
# 
# [__Konstantin Ziegler__ (konstantin.ziegler@uni-passau.de)](http://zieglerk.net)
# 
# based on the following sources
# 
# * [J.R. Johansson (robert@riken.jp)](http://dml.riken.jp/~rob/): http://github.com/jrjohansson/scientific-python-lectures
# 
# __License__
# 
# This work is licensed under a [Creative Commons Attribution 3.0 Unported License](http://creativecommons.org/licenses/by/3.0/)
# 

# # Data Science

# <div class="alert alert-success">
# **Data Science** is the study of the generalizable extraction of knowledge from data; knowledge used for answering (scientific) questions through gathering, storing, processing and analysing large amounts of data. (Dhar, 2013)
# </div>
# 
# Data Science is neither about a particular set of tools like NoSQL Databases, Hadoop etc., nor about storing Google-scale amount of data, it is simply about the **Scientific questions that can be answered with (big) data**. (Leek, 2013)
# 

# Data Science is also an umbrella term covering a number of different disciplines
# - Statistics and statistical inferencig
# - Stochastics as mathematical modelling approach
# - Databases as methods/tools for data storage
# - Parallel Computing as methods for scaling up using multiple machines
# - Machine Learning/Data Mining for providing algorithms
# - Social Network Analysis as application area
# - Human Computing Interfaces and Visual Analytics
# - Engineering
# - ....

# ** Let other people talk... **

# In[2]:

from IPython.display import YouTubeVideo
YouTubeVideo("GXjjMSn2Nws")


# ## Big Data

# <div class="alert alert-success">
# **Big Data** is yet another umbrella term bringing togehter all methods and discipline involved in analysing, capturing, curating, searching, sharing, storing, transfering, visualising large data sets. The term has been created out of the enormous increase of available data due to the Internet and subequent phenomas. 
# </div>
# 
# Big Data is "defined" (in a non-mathematical sense) via 4 V's, namely Volume, Velocity, Variety, Veracity. It stems out of characterisation by Gartner (Gartner, 2011) who used 3V's, refined from IBM. 

# <img src="files/images/4-Vs-of-big-data.jpg"/>
# Original Source: http://www.ibmbigdatahub.com/infographic/four-vs-big-data 

# ## The KDD Process

# <img src="files/images/600px-Fayyad96kdd-process.png"/>
# according to (Fayyad et al. 1996).
# 
# 
# 

# # What is Python?

# <img src="http://img-9gag-lol.9cache.com/photo/aKgj6M3_460s_v1.jpg">
# Source: http://m.9gag.com/gag/aKgj6M3/harry-potter-talking-to-snakes

# [Python](http://www.python.org/) is a modern, general-purpose, object-oriented, high-level programming language.
# 
# General characteristics of Python:
# 
# * **clean and simple language:** Easy-to-read and intuitive code, easy-to-learn minimalistic syntax, maintainability scales well with size of projects.
# * **expressive language:** Fewer lines of code, fewer bugs, easier to maintain.
# 
# Technical details:
# 
# * **dynamically typed:** No need to define the type of variables, function arguments or return types.
# * **automatic memory management:** No need to explicitly allocate and deallocate memory for variables and data arrays. No memory leak bugs. 
# * **interpreted:** No need to compile the code. The Python interpreter reads and executes the python code directly.

# ## Python: Pros and Cons

# 
# Advantages:
# 
# * The main advantage is __ease of programming__ and __minimizing development time__
# * __Modular and object-oriented programming__, good system for __packaging and  code re-use__. 
# 
# * Documentation tightly integrated with the code.
# * A __large standard library__, and a __huge number of libraries__
# 
# Disadvantages:
# 
# * Since Python is an interpreted and dynamically typed programming language, the execution of python code __can be slow__ compared to compiled statically typed programming languages, such as C and Fortran. However, exentsion like [Cython](http://cython.org/) allow to integrate fast C Code (e.g. for inner loops)
# * Somewhat decentralized, with __different environment, packages and documentation__ spread out at different places. Can make it harder to get started.

# # What makes python suitable for Data Science?

# <img src="files/images/optimizing-what.png" width="600">
# 
# 

# 
# * Python has a strong position in scientific computing: 
#     * **Large community of users**, easy to find help and documentation.
# 
# 
# * Extensive ecosystem of important libraries and environments
#    * **scipy**: http://www.scipy.org -  Scientific Python
#    * **numpy**: http://numpy.scipy.org - Numerical Python
#    * **matplotlib**: http://www.matplotlib.org - graphics library
#   Note: these libraries are bundled in the popular `pylab` which puts them all in one namespace in a Matlab-like interface. We don't want that (the matplotlib developers give an elaborate argument for this). 
# 
# * Great performance due to close integration with time-tested and highly optimized codes written in C and Fortran:
#     * blas, altas blas, lapack, arpack, Intel MKL, ...
# 
# 
# * Good support for 
#     * Parallel processing with processes and threads
#     * Interprocess communication (MPI)
#     * GPU computing (OpenCL and CUDA)
# 
# 
# * Readily available and suitable for use on high-performance computing clusters. 
# 
# 
# * Free and Open License

# ## The scientific python software stack

# <img src="files/images/scientific-python-stack.svg" width="300">

# # Python Environments

# 
# 
# - Python also refers to the __standard implementation of the interpreter__
#   - (technically referred to as [CPython](http://en.wikipedia.org/wiki/CPython))  
#   - The interpreter runs the python code on a computer.
# 
# 
# - __Different environments__ through wich Python can be used allowing different workflows
# 
# 
# - One strength of python is that it __versatile__ and can be used in __complementary ways__, but it can be confusing for beginners so we will start with a brief survey of python environments that are useful for scientific computing.

# ## Python interpreter

# The standard way to use the Python programming language is to use the Python interpreter to run python code. The python interpreter is a program that read and execute the python code in files passed to it as arguments. At the command prompt, the command ``python`` is used to invoke the Python interpreter.
# 
# For example, to run a file ``my-program.py`` that contains python code from the command prompt, use::
# 
#     $ python my-program.py
# 
# We can also start the interpreter by simply typing ``python`` at the command line, and interactively type python code into the interpreter. 
# 
# <img src="files/images/python-screenshot.jpg" width="600"> 
# 
# This is often how we want to work when developing scientific applications, or when doing small calculations. But the standard python interpreter is not very convenient for this kind of work, due to a number of limitations.

# ## IPython

# [IPython](http://ipython.org/) is an interactive shell that addresses the limitation of the standard python interpreter, and it is a work-horse for scientific use of python. It provides an interactive prompt to the python interpreter with a greatly improved user-friendliness.
# 
# <img src="files/images/ipython-screenshot.jpg" width="600">
# <!--<img src="https://raw.github.com/jrjohansson/scientific-python-lectures/master/images/ipython-screenshot.jpg" width="600">
# -->
# 

# Some of the many useful features of IPython includes:
# 
# * Command history, which can be browsed with the up and down arrows on the keyboard.
# * Tab auto-completion.
# * In-line editing of code.
# * Object introspection, and automatic extract of documentation strings from python objects like classes and functions.
# * Good interaction with operating system shell.
# * Support for multiple parallel back-end processes, that can run on computing clusters or cloud services like Amazon EE2.
# 

# ## Jupyter notebook

# [Jupyter notebook](http://jupyter.org) is an HTML-based notebook environment for Python, similar to Mathematica or Maple. It evolved from the IPython shell via IPython notebooks and provides a cell-based environment with great interactivity, where calculations can be organized documented in a structured way.
# 
#  <img src="files/images/ipython-notebook-screenshot.jpg" width="800"> 
# <!--<img src="https://raw.github.com/jrjohansson/scientific-python-lectures/master/images/ipython-notebook-screenshot.jpg" width="800">
# -->
# 

# #### Local Jupyter Notebook
# 
# Although using the a web browser as graphical interface, Jupyter notebooks are usually run locally, from the same computer that run the browser. To start a new Jupyter notebook session, run the following command:
# 
#     $ jupyter notebook
# 
# from a directory where you want the notebooks to be stored. This will open a new browser window (or a new tab in an existing window) with an index page where existing notebooks are shown and from which new notebooks can be created.

# #### Jupyter Notebooks on a Server (JupyterHub)
# 
# Organizations might decide to run a Jupyter server as a service, then called a JupyterHub. A popular public one is [Try Jupyter!](http://try.jupyter.org) (although increasingly busy). This course has its own JupyterHub at http://jupyter.dimis.fim.uni-passau.de .

# ### Why and when to use Jupyter Notebook?
# 
# - This lecture notes have been developed using Jupyter notebooks
# - All exercises can be done using Jupyter notebooks
# - There is a special introduction to Jupyter notebooks
# - Very useful for exploring unknown solutions
#   - REPL Cycle - Read, Evaluate, Print, Loop
#   - Document your work while working
#   - Great resource for learning
# - Not very useful for large scale industry project
#   - No project management
#   - Missing refactoring
#   - Use IDE's in this case ([Eclipse based PyDev](http://pydev.org/), [Intellij's Pycharm](http://www.jetbrains.com/pycharm/))
# 

# ## IDE: Spyder

# [Spyder](http://code.google.com/p/spyderlib/) is a MATLAB-like IDE for scientific computing with python. It has the many advantages of a traditional IDE environment, for example that everything from code editing, execution and debugging is carried out in a single environment, and work on different calculations can be organized as projects in the IDE environment.
# 
# <img src="files/images/spyder-screenshot.jpg" width="800"> 
# <!--<img src="https://raw.github.com/jrjohansson/scientific-python-lectures/master/images/spyder-screenshot.jpg" width="800">
# -->
# Some advantages of Spyder:
# 
# * Powerful code editor, with syntax high-lighting, dynamic code introspection and integration with the python debugger.
# * Variable explorer, IPython command prompt.
# * Integrated documentation and help.

# # Versions of Python

# Two Version of Python
# 
#   * Python 2 (2.7 still contains the majority of libraries)
#   * Python 3 (not backward compatible)
#  
# We will use Python 3.5 for this lecture
# 
# To see which version of Python you have, run
#     
#     $ python --version
#     Python 3.5.1 :: Anaconda 4.0.0 (64-bit)
#  
#     
#     $ python2 --version
#     Python 2.7.6
# 
# Several versions of Python can be installed in parallel, as shown above.
# 

# # Installation
# 
# We recommend the [Anaconda](https://www.continuum.io/downloads) python distribution which
# - includes most of our favorite packages in its default installation 
# - comes with a package-/environment-manager
# 
# Here our choice is 64-bit python3. 
# 
# After installation (or upgradeng from miniconda) check that your favorites are installed.
# 
#     $ conda install jupyter scipy numpy matplotlib pandas
# 
# 
# ## add an R kernel
# 
# If you want an R kernel for your Jupyter notebook, you install
# 
#     $ conda install -c r r-essentials r-irkernel
#     

# ### Linux
# In Ubuntu Linux, to installing python and all the requirements run:
# 
#     
#     $ sudo apt-get install python ipython ipython-notebook
#     
#     $ sudo apt-get install python-numpy python-scipy python-matplotlib python-sympy
#     
#     $ sudo apt-get install spyder
# 

# ### MacOS X
# 
# *Macports*
# 
# Python is included by default in Mac OS X, but for our purposes it will be useful to install a new python environment using [Macports](http://www.macports.org/), because it makes it much easier to install all the required additional packages. Using Macports, we can install what we need with:
# 
#     $ sudo port install py27-ipython +pyside+notebook+parallel+scientific
#     
#     $ sudo port install py27-scipy py27-matplotlib py27-sympy
#     
#     $ sudo port install py27-spyder
# 
# These will associate the commands `python` and `ipython` with the versions installed via macports (instead of the one that is shipped with Mac OS X), run the following commands:
# 
#     $ sudo port select python python27
#     
#     $ sudo port select ipython ipython27
# 
# *Fink*
# 
# Or, alternatively, you can use the [Fink](http://www.finkproject.org/) package manager. After installing Fink, use the following command to install python and the packages that we need:
# 
#     $ sudo fink install python27 ipython-py27 numpy-py27 matplotlib-py27 scipy-py27 sympy-py27
#     
#     $ sudo fink install spyder-mac-py27

# ### Windows 
# 
# Windows lacks a good packaging system, so the easiest way to setup a Python environment is to install a pre-packaged distribution. Some good alternatives are:
# 
#  * [Enthought Python Distribution](http://www.enthought.com/products/epd.php). EPD is a commercial product but is available free for academic use.
#  * [Anaconda CE](http://continuum.io/downloads.html). Anaconda Pro is a commercial product, but Anaconda Community Edition is free.
#  * [Python(x,y)](http://code.google.com/p/pythonxy/). Fully open source.
# 
# 
# 
# #### Note
# 
# EPD and Anaconda CE are also available for Linux and Max OS X.

# # Further reading

# 
# * [Python](http://www.python.org>). The official Python web site.
# * [Python tutorials](http://docs.python.org/2/tutorial/). The official Python tutorials.
# * [Think Python](http://www.greenteapress.com/thinkpython/). A free book on Python.
# * **[Learn Python the Hard Way](http://learnpythonthehardway.org/book/). An exercise book. The only way to learn programming is to do it!**
# * Vasant Dhar. 2013. Data science and prediction. Commun. ACM 56, 12 (December 2013), 64-73. DOI=10.1145/2500499 http://doi.acm.org/10.1145/2500499
# * Jeff Leek (2013-12-12). "The key word in "Data Science" is not Data, it is Science". http://simplystatistics.org/2013/12/12/the-key-word-in-data-science-is-not-data-it-is-science/
# * Beyer, Mark (2011). "Gartner Says Solving 'Big Data' Challenge Involves More Than Just Managing Volumes of Data". Gartner. [Archived](http://web.archive.org/web/20110710043533/http://www.gartner.com/it/page.jsp?id=1731916), http://www.gartner.com/newsroom/id/1731916, last accessed 10/2014
# * U. Fayyad, G. P.-Shapiro, and P. Smyth. From data mining to knowledge discovery in databases. AI Magazine, 17(3):37-54, Fall 1996. http://citeseer.ist.psu.edu/fayyad96from.html
# 
