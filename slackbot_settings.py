# coding: utf-8
import os

# botアカウントのトークンを指定
API_TOKEN = ""

# このbot宛のメッセージで、どの応答にも当てはまらない場合の応答文字列
DEFAULT_REPLY = "こんにちは"

# プラグインスクリプトを置いてあるサブディレクトリ名のリスト
PLUGINS = ['plugins']

#テストだけど
PORT = int(os.environ.get("PORT", 5000))