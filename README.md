<p align="center">
    <br>
    <img src="https://raw.githubusercontent.com/andronikmk/med-cabinet-data-science/master/references/logo.png" width="242"/>
    <br>
<p>

<p align="center">
    <a href="https://github.com/andronikmk/toxic-content-monitoring/blob/master/LICENSE">
        <img alt="GitHub" src="https://img.shields.io/badge/License-MIT-blue.svg">
    </a>
</p>

# Introduction to Med Cabinet
App for new cannabis consumers (especially those trying to get off of pharmaceuticals) who want to use cannabis as a means to battle medical conditions and ailments. Helping patients find the right strains, dosing, intake method and intake schedule!

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
```console
$gunicorn -w 4 src:APP -t 120

[2020-08-05 17:09:34 -0400] [59361] [INFO] Starting gunicorn 20.0.4
[2020-08-05 17:09:34 -0400] [59361] [INFO] Listening at: http://127.0.0.1:8000 (59361)
[2020-08-05 17:09:34 -0400] [59361] [INFO] Using worker: sync
[2020-08-05 17:09:34 -0400] [59364] [INFO] Booting worker with pid: 59364
[2020-08-05 17:09:34 -0400] [59368] [INFO] Booting worker with pid: 59368
[2020-08-05 17:09:34 -0400] [59369] [INFO] Booting worker with pid: 59369
[2020-08-05 17:09:35 -0400] [59376] [INFO] Booting worker with pid: 59376
```