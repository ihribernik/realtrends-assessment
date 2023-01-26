# realtrends-assessment

## create a virtual env

```shell
python -m venv env
```

## install dev depencencies (with virtualenv activated)
```shell
pip install -r dev-requirements.txt
```

## use help in makefile
```shell
make help
```

## to run the app in dev mode

```shell
make run-dev
make run-docker
```

## to  run test use:
```shell
make test
```

## to see coverage use
```shell
make see-coverage
```

pd: en el .env.example estan las app_id y el app_secret que use para el chalenge.
la parte de auth la arme a medias, hace el redirect al login de mercado libre pero cuando vuelve esta fallando.