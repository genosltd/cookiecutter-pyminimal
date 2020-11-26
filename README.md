# cookiecutter-pyminimal

A minimalistic python project
[cookiecutter](https://cookiecutter.readthedocs.io/) template equipped with:

* [venv virtual environment](https://docs.python.org/3/library/venv.html)
* [EditorConfig](https://editorconfig.org/)
* [Sphinx documentation project](https://www.sphinx-doc.org/)
* [pytest testing](https://docs.pytest.org/)

## Requirements

Please install [Python](https://www.python.org/) version 3.5 or higher.

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install *cookiecutter*:

```bash
$ pip install -U cookiecutter
```

## Usage

To create python project in the current directory, please use:

```bash
$ cookiecutter https://github.com/genosltd/cookiecutter-pyminimal
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to
discuss what you would like to change.

Please make sure to update documentation and tests as appropriate.

### Installing

Please install *cookiecutter-pyminimal*:

```bash
$ pip install -U cookiecutter-pyminimal
```

### Testing

For testing purposes please pip install it with [test] option:

```bash
$ pip install -U cookiecutter-pyminimal[test]
```

Tests are run with [pytest](https://docs.pytest.org/en/latest/index.html):

```bash
$ pytest
```

## License
MIT
