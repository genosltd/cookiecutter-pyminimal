import subprocess
import sys
import pathlib
import venv
import shutil
import os


here = pathlib.Path('.')


def venv_activate():
    if sys.platform == 'win32':
        return str(here / '..' / 'venv' / 'Scripts' / 'activate.bat')

    elif sys.platform in {'linux', 'darwin'}:
        return 'source ' + str(here / '..' / 'bin' / 'activate')


def venv_install():
    venv.create('venv', with_pip=True,
                prompt='{{ cookiecutter.project_slug }}')


def mv(src, dst):
    os.remove(dst)
    os.replace(src, dst)


try:
    subprocess.run(' && '.join((
        venv_activate(),
        'pip install Sphinx',
    )))
    subprocess.run(' && '.join((
        venv_activate(),
        'sphinx-quickstart -q --project="{{ cookiecutter.project_name }}" --author="{{ cookiecutter.full_name }}" docs',
    )))

    for dirpath, _, filenames in os.walk(here / '_docs'):
        dirpath = pathlib.Path(dirpath)
        dst = here / 'docs'
        for part in dirpath.parts[1:]:
            dst /= part

        for filename in filenames:
            os.remove(here / 'docs' / filename)
            os.replace(dirpath / filename, dst / filename)

    shutil.rmtree(here / '_docs')

except Exception:
    sys.exit(1)
