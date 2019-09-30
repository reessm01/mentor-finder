# mentor-finder

## Installation instructions
- clone repo `git clone {repo_link}`
- `pipenv install`
- `pipenv shell`
- `python manage.py makemigrations` 
- `python manage.py migrate`

## Commands
### bootstrap_model
- Run `python manage.py bootstrap_model model_name_here` to initialize new model
- Creates new folder & files common for models and adds the url_patterns to baseapps urls.py folder

## Templates
Add: {% extends 'base.html' %} {% load crispy_forms_tags %} {% block content %} your_content_here {% endblock %}<br>
to all new template html files.