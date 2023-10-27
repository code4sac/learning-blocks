# <p align="center"> Stand Alone FastAPI Setup </p>

<p align="center">
<strong>This documentation is for those of you who are interested in loading just the back end of Learning Blocks.</strong>
</p>

## Run the server locally

This documentation describes how to install and run the FastAPI server.

### Python virtual environment

Set up a Python [virtual environment](https://docs.python.org/3/library/venv.html) and install the project dependencies.

> Make sure the venv folder is in the root of the [py_orl](.) folder.

```shell
cd py_orl
python -m venv venv
source ./venv/bin/activate # venv\Scripts\Activate.ps1 on Windows
pip install -r requirements.txt
```

### Run the FastAPI server

While in the py_orl folder, start the FastAPI server with the following command.

```shell
uvicorn app:app --reload
```

## FastAPI examples

FastAPI is configured in the [app.py](/Learning-Blocks-No-Docker/py_orl/app.py) file.
Routes are configured in the [api](/Learning-Blocks-No-Docker/py_orl/api) folder.

Routes can also be defined in the app.py file.

### Basic FastAPI server

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()
# Make sure origins http is the local host url your using. This can be found after you click npm run dev on frontend.
origins = [
    'http://localhost:8080',
    # '*',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class TeamOut(BaseModel):
    name: str
    city: str
    wins: int = 0
    losses: int = 0


class Team(TeamOut):
    id: int


teams = [
    Team(id=0, name="Magic", city="Orlando"),
    Team(id=1, name="Heat", city="Miami"),
]


@app.get("/")
async def root():
    return {"message": "Hello World"}


# Create the url name for the page.
@app.get("/teams", response_model=list[TeamOut])
# Create a method that will return value you want to the browser to see.
async def getTeams():
    return teams


@app.post("/team/{name}", response_model=TeamOut)
async def scoreTeam(name: str, win: bool = True):
    for team in teams:
        if team.name == name:
            if win:
                team.wins += 1
            else:
                team.losses += 1
            return team
```