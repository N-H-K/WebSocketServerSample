# WebSocketServerSample

## 構築手順
debian系Linuxの使用を想定しています。

virtualenvを使った構築手順

0. pipのインストール

```
$ sudo apt-get install python-pip
```

1. virtualenvのインストール
```
$ sudo pip install virtualenv
```

2. 環境構築
```
$ git clone https://github.com/N-H-K/WebSocketServerSample.git
$ cd WebSocketServerSample
$ virtualenv venv
$ . ./venv/bin/activate
$ pip install -r requirements.txt
```

3. 起動
```
$ python application/app.py
```
