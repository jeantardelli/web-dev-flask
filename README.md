[![MIT](https://img.shields.io/github/license/jeantardelli/web-dev-flask)](https://choosealicense.com/)
[![Python](https://img.shields.io/badge/Python-3.8-blue)](https://www.python.org/)

Web Development with Flask
==========================
This repository contains the source code of a web application using Flask.


The website can be accessed clicking [here](https://talita-arqueros.herokuapp.com)

Requirements
============
The list of Python packages to run this application can be found in [requirements.txt](requirements/common.txt) 

Just run:

```bash
$ pip install -r requirements.txt
```

To build a perfect replica of the packages.

Docker Deployment 
=================

Clone the project into your local machine using the command:

```bash
$ git clone https://github.com/jeantardelli/web-dev-flask.git
```

Change to the directory where the project was cloned:

```bash
$ cd web-dev-flask
```

Make sure Docker is up and running and you have docker-compose installed. Then run:

```bash
docker-compose up
```

Open your browser and paste the below url:

```bash
http://localhost:5000
```

License
=======
[MIT](LICENSE)
