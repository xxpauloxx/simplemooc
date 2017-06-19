# SimpleMOOC - Ensino a distância
[![Build Status](https://travis-ci.org/paulopinda/simplemooc.svg?branch=master)](https://travis-ci.org/paulopinda/simplemooc)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/19176ed01baa477b9221033f85eadfa6)](https://www.codacy.com/app/paulo-pinda/simplemooc?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=paulopinda/simplemooc&amp;utm_campaign=Badge_Grade)

Plataforma de ensino a distância com foco em cursos abertos utilizando embed videos. O projeto é basicamente um painel de controle da instituição onde pode ser cadastrado cursos e aulas em videos podendo ser do youtube ou outros que geram código embed e um painel do aluno para interagir com fórum e as aulas.

### Como desenvolver?

1. Instale o PyEnv utilizando a ferramenta [Pyenv-Installer](https://github.com/yyuu/pyenv-installer).
2. Utilize os seguintes passos abaixo para a configuração do ambiente e execução.

```bash
git clone https://github.com/paulopinda/simplemooc.git
cd simplemooc
./scripts/setup.sh
source .venv/bin/activate
pip install -r requirements.txt
python manage.py test
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
