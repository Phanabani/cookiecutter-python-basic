# {{ cookiecutter.project_name }}

[![release](https://img.shields.io/github/v/release/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug_github }})](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug_github }}/releases)
[![license](https://img.shields.io/github/license/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug_github }})](LICENSE)

{{ cookiecutter.project_short_description }}

## Table of Contents

- [Install](#install)
- [Usage](#usage)
- [Developers](#developers)
- [License](#license)

## Install

### Prerequisites

- [Poetry](https://python-poetry.org/docs/#installation) – dependency manager
- (Optional) pyenv – Python version manager
    - [pyenv](https://github.com/pyenv/pyenv) (Linux, Mac)
    - [pyenv-win](https://github.com/pyenv-win/pyenv-win) (Windows)

### Install {{ cookiecutter.project_name }}

To get started, clone the repo.

```shell
git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug_github }}.git
cd {{ cookiecutter.project_slug_github }}
```

Install the dependencies with Poetry. {{ cookiecutter.project_name }} requires Python {{ cookiecutter.python_version }}+.

```shell
poetry install --no-root --no-dev
```

## Usage

In the top level directory, simply run {{ cookiecutter.project_name }} as a Python module with Poetry.

```shell
poetry run python -m {{ cookiecutter.project_slug }}
```

## Developers

### Installation

Follow the installation steps in [install](#install) and use Poetry to 
install the development dependencies:

```shell
poetry install --no-root
```

## License

[MIT © {{ cookiecutter.full_name }}.](LICENSE)
