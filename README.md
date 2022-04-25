# SIMPLE BOILERPLATE - PIP VERSION

Copyright (c) 2022 - present

> Template boilerplate code used by [engcs](https://github.com/engcs/) to generate generics simple projects:

<br />

- `Backend`: Folder Structure
- `Deployment`: Local

<br />

> Links

- 👉 [Link 1](https://www.google.com/) - Link description page

<br />

## ✨ Quick Start in `Docker`

> Get the code

```bash
$ git clone https://github.com/engcs/my-boilerplate-pip.git
$ cd boilerplate-code-flask-dashboard
```

> Start the app in Docker

```bash
$ docker-compose up --build 
```

Visit `http://localhost:85` in your browser. The app should be up & running.

<br />

## ✨ **[Product Roadmap](https://github.com/app-generator/boilerplate-code-flask-dashboard/blob/master/SPECS.md)**

- [x] **Updated boilerplate**
- [WIP] `Deployment`:
  - [X] Python 
  - [ ] Docker 
  - [ ] *HEROKU* 

<br />

## ✨ How to use it in python deployment

> 👉 **Clone Sources** (this repository)

```bash
$ git clone https://github.com/engcs/my-boilerplate-pip.git
$ cd my-boilerplate-pip
```

<br />

> 👉 **Install Dependencies** using Virtualenv

For **Linux-based Systems**

```bash
$ virtualenv env
$ source env/bin/activate
$
$ pip3 install -r requirements.txt
```

Or for **Windows-based Systems**

```bash
$ virtualenv env
$ .\env\Scripts\activate
$
$ pip3 install -r requirements.txt
```

<br />

> 👉 **Set up the environment** if they exist

For **Linux-based Systems**

```bash
$ export VAR_ENV=VALUE
```

Or for **Windows-based Systems**

```bash
$ # CMD terminal
$ set VAR_ENV=VALUE
$
$ # Powershell
$ $env:VAR_ENV = VALUE
```

<br />

> 👉 **Start the APP**

```bash
$ python run.py 
```

<br />

## ✨ Code-base structure

The project is coded with a simple and intuitive structure presented bellow:

> Simplified version

```bash
< PROJECT ROOT >
   |
   |-- apps/
   |   __init__.py                         # Initialize the app
   |
   |-- docs/
   |   index.md                            # Documentation index
   |
   |-- tests/
   |   __init__.py                         # Suite test
   |
   |-- requirements.txt                     # Development modules
   |
   |-- .gitignore                           # Files to git ignore
   |-- README.md                               # Makefile (scripts)
   |-- LICENSE.md                               # Makefile (scripts)
   |-- CHAGELOG.md                               # Makefile (scripts)
   |-- SPECS.md                               # Makefile (scripts)
   |-- Makefile                               # Makefile (scripts)
   |-- run.py                               # Start the app
   |
   |-- ************************************************************************
```

<br />

> The bootstrap flow

- `run.py` initilize the application

<br />


## ✨ Deployment

Visit `http://localhost:8001` in your browser. The app should be up & running.

<br />

---
[Simple Boilerplate](https://github.com/engcs/my-boilerplate-pip) - Provided by **Eng. Cristian Sousa** ([engcs](https://github.com/engcs/)).
