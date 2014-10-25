# Socialhome

Socialhome is a Django application that acts as a social homepage for a user. The plan is to allow adding boxes or similar containers which contain information or a feed from an external site.

External site information will be synced as background jobs to minimize outgoing queries to sites.

[See an example here](http://jasonrobinson.me).

## Tech stack

* Built with [Django](http://djangoproject.com).
* [South](http://south.aeracode.org/) for database migrations.

## Installation

Installation example for Ubuntu 13.10. Either do it your preferred way or follow the following guide.

### Prerequisites

#### Database

SQLite can be used for development. For production installations, we can use for example [MariaDB](https://mariadb.org/).

```
sudo apt-get install software-properties-common
sudo apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0xcbcb082a1bb943db
sudo add-apt-repository 'deb http://mirror.netinch.com/pub/mariadb/repo/10.0/ubuntu saucy main'
sudo apt-get update
sudo apt-get install mariadb-server
```

#### Python

Python 2.7 has been used while developing. Python 3.x might work but no guarantees at the moment. [Pythonz](https://github.com/saghul/pythonz) is a nice Python version manager, though totally *optional*;

`curl -kL https://raw.github.com/saghul/pythonz/master/pythonz-install | bash`

> Please add the following line to the end of your ~/.bashrc:

`[[ -s $HOME/.pythonz/etc/bashrc ]] && source $HOME/.pythonz/etc/bashrc`

#### PIP

PIP needs to be installed;

`sudo easy_install pip`

#### Virtualenvwrapper

Suggested way to do development is to use [virtualenvwrapper](https://pypi.python.org/pypi/virtualenvwrapper).

```
sudo pip install virtualenv virtualenvwrapper
mkdir $HOME/.virtualenvs
```

### Python environment

```
pythonz install -t cpython 2.7.6
mkvirtualenv -p $HOME/.pythonz/pythons/CPython-2.7.6/bin/python socialhome
```

The environment will be automatically activated. In the future before starting development, do;

`workon socialhome`

### Get code

```
cd /path/to/local/git/repos
git clone git@github.com:jaywink/socialhome.git
cd socialhome
```

### Install packages

`pip install -r requirements.txt`

### Setup application

DB:

`python manage.py createdb`

Configuration

`cp socialhome/local_settings.py.example socialhome/local_settings.py`

## Running application

For development, you can run the application locally with the following;

`python manage.py runserver`

To run in production mode, *TBD*..

## Development

*TBD*

## License

BSD
