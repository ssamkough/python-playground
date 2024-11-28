# playground

## getting started

1. `python3.11 -m venv venv`

2. `source venv/bin/activate`

3. `pip install -r requirements.txt`

4. `python main.py`

## commands

`python3.11 -m venv venv`

### venv

`source venv/bin/activate`
`deactivate`
`rm -r venv`

### pip

`pip install [package]`
`pip install requests`
`pip install -r requirements.txt`

`pip uninstall [package]`
`pip freeze | xargs pip uninstall -y`: uninstallls all packages

`pip freeze`: shows dependencies installed

### helper

you can use `python` or `pip` in venv:

`which python`
`python -V`

### vscode keyboard shortcuts

`ctrl` + \``\`: switch to terminal

`ctrl` + `1`: switch to editor

## resources

https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html