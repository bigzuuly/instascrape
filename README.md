# About
The purpose of this project is to get a list of followers from a specific instagram account and then get the number of followers for each of those followers.

There are some utility scripts to turn the data into .csv files for sorting and searching

# Requirements

This project is based on Python 3.9, and all Python requirements are managed using the [poetry package](https://github.com/python-poetry/poetry).

To install the project, start with a clean virtual python virtual environment and install (as specified in the [requirements.txt](../requirements.txt) file:

```bash
pip install -r requirements.txt
```

# Configuration
Grab and enter the following from your Instagram Session

```
COOKIE = 'GRAB ENTIRE COOKIE'
X_IG_APP_ID = "IG APP ID"
X_ASBD_ID = "IG ASBD ID"
X_IG_WWW_CLAIM = "IG WWW CLAIM"
```

# Running
Get .json files of followers and store in `data` folder

```
python main.py
```
