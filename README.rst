URL shortener django
==============================

.. image:: http://i.imgur.com/feMpZ7P.png
    :alt: Screenshot of result
    :width: 600
    :height: 400
    :align: center

URL shortener similar to http://bit.ly.


Getting up and running
----------------------

The steps below will get you up and running with a local environment. I assume you have the following installed:

* pip
* virtualenv


First make sure to create and activate a virtualenv

    $ virtualenv env

Install the requirements for local development::

    $ pip install -r requirements/local.txt

Add execution bit to manage.py:

    $ chmod +x manage.py

Migrate database:

    $ ./manage.py migrate

Import words into database:

    $ ./manage.py import_words -f words.txt


You can now run the ``runserver`` command::

    $ ./manage.py runserver

Running tests
-------------

    $  ./manage.py test


Further Development
-------------------

The base app will run but you'll need to carry out a few steps to make the sign-up and login forms work. These are currently detailed in `issue #39`_.

.. _issue #39: https://github.com/pydanny/cookiecutter-django/issues/39

**Live reloading and Sass CSS compilation**

If you'd like to take advantage of live reloading and Sass / Compass CSS compilation you can do so with the included Grunt task.

Make sure that nodejs_ is installed. Then in the project root run::

    $ npm install grunt

.. _nodejs: http://nodejs.org/download/

Now you just need::

    $ grunt serve

The base app will now run as it would with the usual ``manage.py runserver`` but with live reloading and Sass compilation enabled.

To get live reloading to work you'll probably need to install an `appropriate browser extension`_

.. _appropriate browser extension: http://feedback.livereload.com/knowledgebase/articles/86242-how-do-i-install-and-use-the-browser-extensions-


