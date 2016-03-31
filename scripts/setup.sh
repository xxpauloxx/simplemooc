#!/bin/bash

# Verificando se existe o pyenv.
if ! [ -x "$(command -v pyenv)" ]; then
	curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
	source ~/.bashrc
	pyenv update
fi

# Instalando Python
pyenv install 3.5.1
pyenv local 3.5.1

pip install virtualenv

rm -rf .venv 
virtualenv --no-site-packages .venv

source .venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt 
