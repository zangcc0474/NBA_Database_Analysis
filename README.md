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

#Parsing Tools

In our project we use [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup) to parse static web source and combine [Selenium](http://www.seleniumhq.org) and [PhantomJS](http://phantomjs.org) to scrape dynamic webpage. 

#Sample Django Project Layout


```
myproject/
    manage.py
    myproject/
        __init__.py
        urls.py
        wsgi.py
        settings/
            __init__.py
            base.py
            dev.py
            prod.py
    myapp/
        __init__.py
        models.py
        managers.py
        views.py
        urls.py
        templates/
            myapp/
                base.html
                list.html
                detail.html
        static/
           …
        tests/
            __init__.py
            test_models.py
            test_managers.py
            test_views.py

```
The advantage of using this layout is the flexiable setting structure.

Well for local development you want DEBUG=True, but it’s pretty easy to accidentally push out production code with it on, after the initial import from base just add DEBUG=False. Now if your production site is safe from that silly mistake.

base.py dev.py prod.py could seperately defined three running settings. 

Switch setting could use a commandline option like this:

`./manage.py migrate —settings=foo.settings.production`

#How to install the project

###Set up a database


OS X.  
The recommended way for installing MySQL on OS X is to use the OS X installer package. See [Installing MySQL on OS X Using Native Packages](http://dev.mysql.com/doc/refman/5.7/en/osx-installation-pkg.html) on how to download and run the installer package, and how to start the MySQL server afterward. 

Detailed information regarding installation on OS X can be found in [Installing MySQL on OS X](http://dev.mysql.com/doc/refman/5.7/en/osx-installation.html).


###Install Django


####Step 1: Verify that you have Python on your computer

Django requires Python to work.  Django can work with different versions of Python.

`python --version`

If your computer doesn’t have Python, you should download it from:

https://www.python.org/downloads/

You should either download the 2.7 version or 3.4 version. Since I am using 3.4 in this tutorial, 3.4 is recommended.


####Step 2: Install pip

If you don’t have pip on your computer, you have to get the get-pip.py installation file. Download the following:

https://bootstrap.pypa.io/get-pip.py

`curl -O https://bootstrap.pypa.io/get-pip.py`

Afterwards, change directory to the location get-pip.py, go to your terminal, and enter:

`python get-pip.py`


####Step 3: Using pip to install Django

After you make sure you have pip installed on your computer, go to the terminal and enter:

`sudo pip install Django`


###Configure Django setting

modify the base.py in
```
 					   --NBA_Database_Analysis
						/nba
						/nba
						/settings
						/base.py


```
In Session 

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'NBA_Database',
        'USER': 'root',
        'PASSWORD' : '12345678',
        'HOST': 'localhost',
        'PORT': '',
    }
}

Change  'USER': 'root',
        'PASSWORD' : '12345678',
        'HOST': 'localhost',

to your local mysql setting
```




