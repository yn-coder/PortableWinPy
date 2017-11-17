# PortableWinPy
Portable server for python web development and testing

# Goals

Goals of this project is
* Run your Python web application locally
* Test some issues of web development and deploy tasks with production web server - on your desktop. Test real web server static files serving configuration, paths and urls in your application
* Base for building and shipping portable web applications

Version 0.0 (15.11.2017)

# Installation

Download the zip archive from [Sourceforge page](https://sourceforge.net/projects/portablewinpy/?source=navbar), unzip to any folder (on hard disk or to USB-stick), and run `run_apache.cmd`

If all is ok, then open the `http://localhost:8080/` in your browser

# Build from source

## Binaries

Apache binaries was taken from [ApacheHaus](https://www.apachehaus.com/cgi-bin/download.plx) (httpd-2.4.28-x86-vc11)

Python Windows x86 binaries from [Python.org](https://www.python.org/downloads/windows/) (python-3.6.3.exe)

# Folders

* Apache
* Python
  * Bottle - demo wsgi application
  * env - configured virtual enviroinment
  * Python36 - python binaries
