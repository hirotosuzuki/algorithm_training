# algorithm_training

```sh
python -m unittest tests/tests_sample.py
```

## 環境構築
```sh
# python環境
poetry install


# AtCoder Cliを使ってログインする
# https://github.com/Tatamo/atcoder-cli
# https://github.com/online-judge-tools/oj/tree/master
npm install -g atcoder-cli
acc login
poetry run oj login https://atcoder.jp/
```

## accコマンド集
```bash
# 問題とテストケースのダウンロード
poetry run acc new abc001 --choice all

# コンテストのページリンク取得
poetry run acc contest

# コンテストのタスクリスト
poetry run acc tasks

# テスト実行
poetry run oj t -c "python3 main.py" -d ./tests/

# 提出
# python環境が複数あるので--language 5055をojに渡す
# ojに -l 5055を渡したいので、accとpoetryの引数判定を回避するために -- -- している
poetry run acc submit main.py -- -- -l 5055
```