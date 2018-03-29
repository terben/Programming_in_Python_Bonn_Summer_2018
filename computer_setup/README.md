# Installation of a Python system

## Python 2 vs. Python 3
There are two major *Python* versions currently in use. *Python 2.7* and
*Python 3.6*. Unfortunately the two versions are *imcompatible* and
we will use *Python 3.6* in our course.

*Python 2.7* is the last version in the *Python 2.X* series and it
will only be maintained with bug fixes in the future. All new
developments will happen in the *Python 3.X* branch and I strongly
recommend to only use that in the future - especially for new scripts
and programs.

## Python 3.6 usage at AIfA and the AIfA CIP-Pool
- *Python 3.6* and all necessary modules for our course are accesible from all
  AIfA computers **but** you need to
  explicitely activate them! To do so on an AIfA computer, you need to type

  ```bash
  user$ module load anaconda/36
  ```

  and *Python 3.6* is activated in your current shell. Putting the above command
  into your `.cshrc` or `.bashrc` configuration file (depending on the *Unix*
  shell that you are using) activates *Python 3.6* automatically within each
  shell that you open.

- In the AIfA CIP-Pool, you need to launch the two following commands to obtain
  a working *Python 3.6*-environment:

  ```bash
  user$ source /usr/share/modules/init/bash  # everybody should use bash
                                             # in the CIP-Pool
  user$ module load anaconda/36
  ```

  I recommend that you put these commands into your `.bashrc` configuration file
  for the duration of the course.

- It seems that Google-Chrome is the standard browser on new accounts in the
  AIfA CIP-Pool. We experienced problems with this browser in connection
  with Jupyter-Notebooks last year.

  If Google-Chrome is the default browser on your account, please change
  it to *Firefox*. This can be done within the
  ```Applications -> Settings -> Settings Manager -> Preferred Applications```
  menu.

## Python 3.X installation on own computers
Python consists of a *core language* (see
[here](https://www.python.org/)) and many optional modules and
packages. For sceintific computing essential modules are
[numpy](http://www.numpy.org/) (data structures optimised for science
applications), [scipy](https://www.scipy.org/) (large collection of
software packages for science applications) and
[matplotlib](http://matplotlib.org/) (plotting package for scientific
data).

As the Python core and all major modules undergo permanent and quick
development, maintaining a coherent system manually can become
cumbersome. For scientific computing, well-maintained *distributions*
allow a very quick setup for *Python* in a scientific environment.
Updates are managed comfortably with dedicated *package managers*.

- I made very good experience with the [Anaconda
  distribution](https://www.continuum.io/) and I strongly recommend you
  to install its current *3.6* version. It contains all packages we need in
  class and it is available for the *Windows*, *Linux* and *Mac* operating
  systems.

- I also recommend you to register with [Anaconda](https://anaconda.org/).
  As a student you profit from free, high performance mathematical libraries.
  I will discuss the merits of them in class.

  **Important: Register with your student university E-Mail address!**

## Installation test
Please run the script ```check_bonn_python.py``` on your computer to
check whether you have a well-installed setup:

```bash
user$ python3 check_bonn_python.py
............
----------------------------------------------------------------------
Ran 12 tests in 1.107s

OK
user$
```
Please contact me if you run into problems that you cannot solve yourself.
