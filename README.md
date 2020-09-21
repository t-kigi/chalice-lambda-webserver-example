# chalice-lambda-webserver-example

Usage Chalice such as Flask/Bottle web application framework

日本語での説明記事: https://


## How to use

Require `pipenv` command and Python 3.8 by `pyenv` . 

```bash
# setup
git clone git@github.com:t-kigi/chalice-lambda-webserver-example.git
cd chalice-lambda-webserver-example
pipenv install

# run server on local server
cd server
pipenv run chalice local --stage local
```

You can access `http://localhost:8000/` after run `chalice local` .


## Deploy
