# mentor-finder

## Installation instructions
- clone repo `git clone {repo_link}`
- `pipenv install`
- `pipenv shell`
- `python manage.py bootstrap_personality`
- `python manage.py bootstrap_industry`
- `python manage.py makemigrations` 
- `python manage.py migrate`

## Commands
### bootstrap_model
- Run `python manage.py bootstrap_model model_name_here` to initialize new model
- Creates new folder & files common for models and adds the url_patterns to baseapps urls.py folder

### bootstrap_personality
- Run `python manage.py bootstrap_personality` to populate the Personality table with predefined values

### 
- Run `python manage.py bootstrap_industry` to populate the Industry table with predefined values

## Templates
Add: {% extends 'base.html' %} {% load crispy_forms_tags %} {% block content %} your_content_here {% endblock %}<br>
to all new template html files.