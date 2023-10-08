# Setup with Python
## Install dependencies
### Setup virtual environment
```sh
python -m venv venv
./venv/activate
```
### Pip install
```sh
pip install uvicorn fastapi pandas requests
```
## Start Fast API server
```sh
cd py_orl
uvicorn app:app --reload
```
