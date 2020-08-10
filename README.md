## Python-env-template

DockerによるPythonの仮想環境とVSCodeによる開発環境構築

```bash
# pyvenvと記載部分はお好きな名前でOK
docker build -t pyvenv .
docker run pyvenv
```

###### VSCode Setup

- Install "Python" extension
- Install "Remote Development" extension
- VSCodeの左下に配置された緑色の「><」マークをクリック
- Remote-Containers: Open Folder in Containerをクリック
- From 'Dockerfile'をクリック

###### Docker HubにPush

```bash
docker login
# <イメージID> <アカウント名><リポジトリ名>:<タグ名>
docker tag ce88b3185047 nmrmasakazu/pyvenv:latest
docker push nmrmasakazu/pyvenv:latest
# 実行（Hubからダウンロード）
docker run nmrmasakazu/pyvenv:latest
```

###### Tips

```bash
# コンテナ全削除
docker ps -aq | xargs docker rm
# イメージ全削除
docker images -aq | xargs docker rmi -f
```

###### Dockerによらないvenv環境（Dockerではlintが使えない）

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

