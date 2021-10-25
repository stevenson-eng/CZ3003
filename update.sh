git restore admin_ui/src/sql_app.db
git restore --staged admin_ui/src/sql_app.db
git pull

# uvicorn main:app --reload --port 8080 --host 0.0.0.0