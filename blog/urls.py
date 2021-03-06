from django.urls import path
from . import views

""""
これはDjangoの path 関数と、blog アプリの全ての ビュー
（といっても、今は一つもありません。すぐに作りますけど！）
をインポートするという意味です。"""
urlpatterns = [
    path('', views.post_list, name='post_list'),
]

"""post_list という名前の ビュー をルートURLに割り当てています。
 このURLパターンは空の文字列に一致します。
 Djangoはビューを見つけるとき、URLのパス(path)の前にくっつくドメイン名（つまり、http://127.0.0.1:8000/ の部分）を無視します。 
 このパターンは誰かがあなたのWebサイトの 'http://127.0.0.1:8000/' というアドレスにアクセスしてきたら views.post_list が正しい行き先だということをDjangoに伝えます。

最後の name='post_list' は、ビューを識別するために使われるURL の名前です。 
これはビューと同じ名前にすることもできますが、全然別の名前にすることもできます。 
プロジェクトでは名前づけされたURLを後で使うことになるので、アプリのそれぞれのURLに名前をつけておくのは重要です。
また、URLの名前はユニークで覚えやすいものにしておきましょう。"""

""""ビューはアプリのロジックを書いていくところです
 ビューは、以前あなたが作った モデル に情報を要求し、それを テンプレート に渡します。 
 テンプレートは、次の章で作ります。 ビューはただのPythonの関数です。"""