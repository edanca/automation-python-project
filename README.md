# AUTOMATION TEST FRAMEWORK BY EDUARDO CARDENAS

This project was made as a demonstration of how to build an automation framework.

The Web been tested is `https://www.aliexpress.com/`.

## Use case

- As a Customer we want to see if the second Iphone related ad from the second results page from www.aliexpress.com has at least 1 item to be bought.

## Techonologies used

- Python
- Pytest
- Selenium
- Docker

## How to run test

Two ways of run are available.

Need to have .env file shared via email. This file contains credentials for login.

### With Pytest from command line

Need to have installed python and pipenv.

```bash
pip install pipenv
```

Then install dependencies

```bash
pipenv install
```

From command line execute:

```bash
pipenv run pytest -vv
```

Results are displayed in console.

### With docker compose

Need to install docker and docker-compose.

Then run from command line:

```bash
docker-compose up --build
```

Results are displayed in console.
