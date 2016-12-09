# NBA_Database_Analysis

In this project, we plan to multiple things:

Firstly, creating a crawler to scrap player data and team stats from Basketball-Reference website.

Secondly, creating a data pipeline for the all of these data.

Thirdly, creating a website allowing user to do querry search.

Fourthly, visualizing some interesting results.

Lastly, appling some machine learning algorithms to do predictions.

#FrameWorks

Using [Django](https://www.djangoproject.com) as our project frameworks

Django is a free and open-source web framework, written in Python, which follows the model-view-template (MVT) architectural pattern.

Django's primary goal is to ease the creation of complex, database-driven websites.

In our project we scraping data from an online basketball database website http://www.basketball-reference.com, and use the data to populate our own database. Eventually we will implement analysis method to evaluate the data, and generate tables and graphs for visualization purpose. 

#How to install the project

Set up a database
=================

OS X.  
The recommended way for installing MySQL on OS X is to use the OS X installer package. See [Installing MySQL on OS X Using Native Packages](http://dev.mysql.com/doc/refman/5.7/en/osx-installation-pkg.html) on how to download and run the installer package, and how to start the MySQL server afterward. 

Detailed information regarding installation on OS X can be found in [Installing MySQL on OS X](http://dev.mysql.com/doc/refman/5.7/en/osx-installation.html).


Install Django
==============

Step 1: Verify that you have Python on your computer

Django requires Python to work.  Django can work with different versions of Python.

`python --version`

If your computer doesn’t have Python, you should download it from:

https://www.python.org/downloads/

You should either download the 2.7 version or 3.4 version. Since I am using 3.4 in this tutorial, 3.4 is recommended.

Step 2: Install pip

If you don’t have pip on your computer, you have to get the get-pip.py installation file. Download the following:

https://bootstrap.pypa.io/get-pip.py

`curl -O https://bootstrap.pypa.io/get-pip.py`

Afterwards, change directory to the location get-pip.py, go to your terminal, and enter:

`python get-pip.py`


Step 3: Using pip to install Django

After you make sure you have pip installed on your computer, go to the terminal and enter:

`sudo pip install Django`



