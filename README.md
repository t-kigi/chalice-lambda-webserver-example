# chalice-lambda-webserver-example

Usage Chalice such as Flask/Bottle web application framework

日本語での説明記事: https://qiita.com/t-kigi/items/418908e290b54732968f

Example site: https://lambdasite.t-kigi.net


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

```bash
# deploy chalice application into API Gateway and Lambda
pipenv run chalice deploy

# deploy static resources into S3 bucket
cd static
aws s3 sync . s3://<your-bucket-name>/
```

After Chalice deployed, you get API Gateway URI such as `https://**********.execute-api.ap-northeast-1.amazonaws.com/v1/`.

You also have to deploy static resources under `static` into your S3 bucket. 


## Collaborate deployed resource by CloudFront

After deployed both, you set CloudFront as your service endpoint. 

- static resources go to S3 origin (`/images/*`, `/css/*`, and more )
- other accesses go to API Gateway Origin. 

Note that Website allows to `/` access when you set `Origin Path` as `API Gateway Stage`.
The example access to https://lambdasite.t-kigi.net/ goes to API Gateway with stage path (like `https://**********.execute-api.ap-northeast-1.amazonaws.com/v1/`).

