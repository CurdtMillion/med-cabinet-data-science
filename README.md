<p align="center">
    <br>
    <img src="https://raw.githubusercontent.com/andronikmk/med-cabinet-data-science/master/references/logo.png" width="242"/>
    <br>
<p>

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/andronikmk/med-cabinet-data-science/master)

# Introduction to Med Cabinet
Med Cabinet is an application for new cannabis consumers who want to use cannabis as a means to battle medical conditions and ailments. In addition, Med Cabinet helps patients find the right strain, dosing, intake methods and scheduale. This application is built using Flask, along with a PostgreSQL database hosted database. The API is deployed to Heroku at which point a front-end team is tasked to build a user interface. This is a cross functional project during which my team was tasked to build a Flask app and PostgreSQL database. An additional data science team was responisble to the model used for this app as well as choosing the metrics to measure our models success.

# Install
This repo is tested on Python 3.7+, PyTorch 1.0.0+ (PyTorch 1.3.1+ for examples) and TensorFlow 2.0.

You can install Med Cabinet using [pipenv](https://pipenv-fork.readthedocs.io/en/latest/). If you're unfamiliar with Pipenv, check out the [user guide](https://pipenv-fork.readthedocs.io/en/latest/install.html#installing-pipenv).
This project was created using [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html), if you are familier with [Anaconda](https://www.anaconda.com/), please reference this [cheat sheet](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf) after you install you choice of Anaconda distrubution.

## From source using pipenv
```bash
git clone https://github.com/andronikmk/med-cabinet-data-science.git
cd med-cabinet-data-science
```
### Create an enviornment using Pipenv
Make sure to be in the correct directory and specify specific versions of Python 3.7.
```bash
# install dependencies
pipenv install

# activate shell
pipenv shell
```

### Create enviornment with conda and pip
Make sure to be in the correct directory.
```bash
# create conda env.
conda create -n med-cabinet python==3.7

# activate env
conda activate medi-cabinet

# pip install dependencies
pip install -r requirements.txt

# add JSON object to an iPython file.
python -m ipykernel install --user --name med-cabinet --display "med-cabinet (Python3)"
```

# Run it
```bash
$ gunicorn -w 4 src:APP -t 240
```
```console
[2020-08-05 17:09:34 -0400] [59361] [INFO] Starting gunicorn 20.0.4
[2020-08-05 17:09:34 -0400] [59361] [INFO] Listening at: http://127.0.0.1:8000 (59361)
[2020-08-05 17:09:34 -0400] [59361] [INFO] Using worker: sync
[2020-08-05 17:09:34 -0400] [59364] [INFO] Booting worker with pid: 59364
[2020-08-05 17:09:34 -0400] [59368] [INFO] Booting worker with pid: 59368
[2020-08-05 17:09:34 -0400] [59369] [INFO] Booting worker with pid: 59369
[2020-08-05 17:09:35 -0400] [59376] [INFO] Booting worker with pid: 59376
```