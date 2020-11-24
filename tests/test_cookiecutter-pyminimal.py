import subprocess
import pathlib
import venv
import sys


def process(args, cwd=None):
    return subprocess.run(args, stdin=None, input=None, capture_output=False,
                          cwd=cwd, timeout=None, check=False, encoding=None,
                          errors=None, text=None, env=None)


def test_bake_project(cookies):
    result = cookies.bake(extra_context={'project_name': 'helloworld'})

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == 'helloworld'
    assert result.project.isdir()


def venv_activate():
    if sys.platform == 'win32':
        return str(pathlib.Path('.') / 'venv/Scripts/activate.bat')

    elif sys.platform in {'linux', 'darvin'}:
        return 'source ./venv/bin/activate'


def test_pip_install_pytest(cookies):
    result = cookies.bake(extra_context=dict(project_name='proba'))

    assert result.exit_code == 0
    assert result.exception is None

    venv.create(pathlib.Path(result.project) / 'venv', with_pip=True)

    pr = process(' && '.join((
        venv_activate(),
        'pip install .[test]',
        'pytest'
    )), cwd=result.project)
    assert pr.returncode == 0
