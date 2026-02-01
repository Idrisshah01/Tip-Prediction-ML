Deployment notes — Heroku / Render

1) Install dependencies

   pip install -r requirements.txt

2) Set environment variables on the host:
   - `DJANGO_SETTINGS_MODULE=tip_prediction.settings`
   - `SECRET_KEY` (override the one in settings)
   - `DEBUG=0`

3) Heroku
   - git init
   - heroku create
   - git add . && git commit -m "deploy"
   - git push heroku main
   - heroku config:set DISABLE_COLLECTSTATIC=0
   - heroku run python manage.py migrate

4) Render
   - Create a new Web Service: `Environment: Python`
   - Build command: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
   - Start command: `gunicorn tip_prediction.wsgi`

Notes:
- `xgboost` may require a longer build time or a pre-built wheel; if build fails on Heroku, consider using Render or providing a prebuilt wheel.
- Ensure the `ML_project/models/xgb_model.joblib` file is included in your repository (it is currently in the project). If it's large, consider storing it in an external object storage and downloading at startup.
