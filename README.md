# Dashboard

Sample code for Smashing Magazine Django Highlights: Templating Saves Lines

Visit [Smashing Magazine](https://smashingmagazine.com) for the full article.

### Setup

```
pip install django
git clone https://github.com/philipkiely/sm_dh_2_dashboard.git
cd sm_dh_2_dashboard
python manage.py migrate
python manage.py createsuperuser
python manage.py loaddata employee_fixture.json
python manage.py runserver
```