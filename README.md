# cookiecutter-pyminimal

A minimalistic python project cookicutter template

## Installation

Please install [Python](https://www.python.org/) version 3.5 or higher.

Then create [virtual environment](https://docs.python.org/3/library/venv.html):

```bash
$ python -m venv --prompt python_project_template venv
```

On Linux/MacOS activate it with:

```bash
$ source ./venv/bin/activate
```

If on Windows activate it with:

```msdos
> .\venv\Scripts\activate.bat
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install *cookiecutter-pyminimal*

```bash
$ pip install cookiecutter-pyminimal
```

## Testing

For testing purposes please pip install it with [test] option:

```bash
$ pip install cookiecutter-pyminimal[test]
```

Tests are run with [pytest](https://docs.pytest.org/en/latest/index.html):

```bash
$ pytest
```

## Usage

```bash
$ cookiecutter cookiecutter-pyminimal
```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update documentation and tests as appropriate.

## License
All rights reserved.
