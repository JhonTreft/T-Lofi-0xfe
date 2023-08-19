
#!/usr/bin/env bash
# exit on error
set -o errexit

pip install --upgrade pip
pip install uvicorn
pip install -r requirements.txt

python ./bin/manage.py makemigrations
python ./bin/manage.py migrate

python ./bin/manage.py tailwind start