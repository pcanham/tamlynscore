TamlynScore
===

Django-based responsive archery scoring web application.

## Requirements

The requirements for the project are as follows:
* Python 3
* PIP
* PostgreSQL

On top of these, if you want to modify/recompile the CSS you're going to need:
* Compass

## Installation

Assuming that the requirements have been fulfilled, the installation procedure is as follows:

1. Clone the repository,
2. Run `pip install -r requirements.txt` from the repositories root,
3. Set up the config file (scoring/settings.py),
  * This should include a secret key and the correct database access URI.
4. Run the program using `make run`

It's thoroughly recommended that you use a virtual environment for python to run this project.

## Contributors
* [Marc Tamlyn](https://twitter.com/mjtamlyn)
* [David Richardson](https://twitter.com/tankski_dr)
