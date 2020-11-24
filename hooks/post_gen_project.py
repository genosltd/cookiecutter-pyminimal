import subprocess
import sys
import pathlib
import venv
import shutil
import os


here = pathlib.Path('.')


def venv_activate():
    if sys.platform == 'win32':
        return str(here / 'venv' / 'Scripts' / 'activate.bat')

    elif sys.platform in {'linux', 'darwin'}:
        return 'source ' + str(here / 'bin' / 'activate')


try:
    print('Python virtual environment installing...', end=' ')
    venv.create('venv', with_pip=True,
                prompt='{{ cookiecutter.project_slug }}')
    print('done.')

    print('Pip installing requirements...', end=' ')
    subprocess.run(' && '.join((
        venv_activate(),
        'pip install -q -e .[doc,test]',
    )),
        shell=True
    )
    print('done.')

    print('Sphinx project setting up...', end=' ')
    subprocess.run(' && '.join((
        venv_activate(),
        'sphinx-quickstart' +
        ' -q --project="{{ cookiecutter.project_name }}'
        '" --author="{{ cookiecutter.full_name }}" docs',
    )),
        shell=True
    )
    for dirpath, _, filenames in os.walk(here / '_docs'):
        dirpath = pathlib.Path(dirpath)
        dst = here / 'docs'
        for part in dirpath.parts[1:]:
            dst /= part

        for filename in filenames:
            os.remove(here / 'docs' / filename)
            os.replace(dirpath / filename, dst / filename)

    shutil.rmtree(here / '_docs')
    print('done.')

except Exception:
    sys.exit(1)
