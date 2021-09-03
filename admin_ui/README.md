# FastAPI Tutorial

https://www.youtube.com/watch?v=-ykeT6kk4bk

# Development

1. cd admin_ui
2. python -m venv env/ (create your virtual environment)
3. source env/bin/activate (activate your virtual environment. google the command if you're on windows)
4. pip install -r src/requirements.txt (install required dependencies)
5. cd src && uvicorn main:app --reload
6. http://127.0.0.1:8000 or localhost:8000

# Pull Requests

[FOR GAME DEV TEAM] You can use `git commit --no-verify` to bypass these checks.
 
1. Git hooks are set on all commits. You won't be able to commit changes that fail **any** of these tests
   - black (formatter)
   - pylint (linter)
   - mypy (static type checker)
2. To fix it, ensure black, pylint, and mypy are installed (otherwise, `pip install black pylint mypy`)
3. Fix the warnings raised
   - black (formatter) - `black path/to/directory/` - formats all .py files in the directory, recursively
   - pylint (linter) - lints all .py files in the directory, recursively. Fix the errors manually.
   - mypy (static type checker) - checks for wrong types in all .py files in the directory, recursively. Fix the errors manually.

# Deployment

1. https://fastapi.tiangolo.com/deployment/deta/
2. Ping Wei Lun for deployment after every merge - https://0kftyn.deta.dev
3. In future, we'll setup automatic deployment via `cd admin_ui/src && deta watch .`
