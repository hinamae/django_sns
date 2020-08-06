# README

## superuserは
meayama
と
password

## なにをつくるか

- 新規登録ページ
- ログインページ
- 新規登録ページ
- いいねボタン(押せば押すほど数が増える)
- 既読ボタン(同じ人が何度も押しても数は1しか増えない)
- ログアウト機能(セッション？)

modelは
タイトル、詳細、ファイル、投稿者


## 準備


### settings.py

- installedappsのところにつくったアプリを加える

- templatesフォルダをプロジェクトのルートディレクトリに作成したため、
DIRSを変更する。

settings.py
```

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
```

↓
```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ BASE_DIR, 'templates' ],
        'APP_DIRS': True,
        'OPTIONS': {

```

### urls.py

urlの繋ぎ込み

## functionbased viewとclassbased view
今回使用するのはfunctionbased view

基本、functionは
- 入力：httpリクエスト
- 出力：レスポンス

### functionbased view
- good:データの流れがわかりやすい
- bad:手間がかかる


### classbased view

- good:template_nameとか属性を設定するだけで簡単に表示をさせることができる。
- bad:データの流れがわかりづらい

### views.py

render関数が引数にとるのは以下3つ。
1. httpリクエスト 
2. classbased viewにおけるtemplate_name(呼び出されるhtmlファイル) 
3. コンテキスト(辞書型データ)(modelからデータを指定することによって、テンプレートを埋め込んでいける。)

```py
from django.shortcuts import render

def signupfunc(request):
    # renderは以下3つを引数にとる
    # 1.httpリクエスト 2.classbased viewにおけるtemplate_name(呼び出されるhtmlファイル) 3.コンテキスト(辞書型データ)
    return render(request,'signup.html',{'some':100}) 
```

### htmlファイル

fuctionの中で3つめの引数で指定したデータを{{}}で使用することができる。

```html
{{ some }}
```


## python

{'some':100} 辞書型データ

## base.html

htmlのブロックを作成。
```
    {% block XXXXX %}
    {% endblock XXXXX %}
```

今回はhtmlファイルそれぞれにカスタムでcssを当てたいため、
customcssのブロックを作成しておく。

## bootstrap

companentsとutilitesがよく使う。

それ以外には、examplesを使用して、完成度の高いテンプレートを使用することができる。


https://getbootstrap.com/docs/4.5/examples/sign-in/

ここから、ページのソースの表示をして、
使える部分を持ってくる。


bodyタグの部分があれば良い。このbootstrapのexampleのsigninページのheadタグの部分はあまりページの見た目とは関係ない。

```html
    <!-- Custom styles for this template -->
    <link href="signin.css" rel="stylesheet">
```
ページのソースにこのような部分がある。
これはカスタムのcssを使用しているということ。
signin.cssを当てる必要がある。

## databaseとの関連

htmlとdatabaseのデータの関連は
タグの中のnameで行われる。


## httpプロトコルについて

ブラウザで情報をもらう場合＝urlを打ち込む

このとき、たくさんの情報をサーバに送っている。


この時に送っている情報の項目の一つが、POST・GET

djangoでリクエストを受け取る方法をPOSTにするのか、GETにするのかわかっていなければいけない。

(djangoにおいては、POSTとGETだけでほぼ事足りる。)

### post

- フォームを送信する場合=POST



### get

- フォームを送信する時以外=GET
- URLを受け取る。など


http://yahoo.co.jp

GET / HTTP/1.1


### リクエストのコントロール
htmlタグの中でmethodを指定する。


views.py
```py
def signupfunc(request):
    #これで、受け取ったリクエストがpostなのかgetなのかをコンソール上に表示することができる。(リクエストの送信は、ブラウザ上で、ボタンを押すなどして送信する。)
    print(request.method)
    return render(request,'signup.html',{'some':100}) 
```
request.methodで表示されるのは、POSTまたはGETなど。。。


view.py

postメソッドのリクエスト受け取ったら、postだよとコンソール上に表示。そうじゃなかったらgetだよとコンソール上に表示。

```py
def signupfunc(request):
    if request.method == 'POST':
        print('this is post method')
    else:
        print('this is get method')
    return render(request,'signup.html',{'some':100}) 
```


## サインアップ

ブラウザ上でうちこまれた名前とパスワードをDBに登録する、という処理を実装する。


### html

formタグの中のaction=フォームが送信された際に次にどこの画面に飛ばすかということ

とりあえずactionはからにする＝同じ画面がかえってくる 
```html
<form class="form-signin" method='POST' action=''>

```

### view.py


ちなみにviews.pyでprintしたものは、runserverしているコンソール上に表示される。


request.POST['username']とすることで、httpリクエストの中で(htmlファイルの中設定)でusernameというnameをもっているデータを取ってくることができる。


```py
def signupfunc(request):
    if request.method == 'POST':
        # POSTでもってきた、'username'(htmlファイルのタグの中のnameの部分)をusername変数に格納
        username = request.POST['username']
        print(request.POST)

```

コンソール上の表示。
```sh
<QueryDict: {'csrfmiddlewaretoken': ['wamX8Cvjf0Aiwwxpi0O1KaQESK0eN20T3yrkN6iaHmHcFLea6wyf7CVXGcS5nzAe'], 'username': ['hina']}>
[05/Aug/2020 10:19:02] "POST /signup/ HTTP/1.1" 200 2013
```

## djangoがデフォルトで用意しているUserテーブルを使用する
```
User.objects
```
によって、ユーザデータをとってくることができる

## ユーザのmodelを作成する(views.pyで)

UserModelというもともとdjangoが用意してくれているモデルを使用する。
(models.pyに記載するまでもない。importすれば使える。)

＜公式＞(ver2.1)
https://docs.djangoproject.com/ja/2.1/topics/auth/default/

views.py
```py
        # create_user関数を使用して、Userオブジェクトを作成する。公式ドキュメントより
        user = User.objects.create_user(username, '', password)

```
作成したら、python manage.py migrateしておかないと、テーブルがありませんという形でエラーになる

## views.pyの関数の中のモデルの取り扱い
- 全データ表示

    {model}.objects.all

view.py
```py
def signupfunc(request):
    #classbasedviewでいうところのobject_list
    #テーブルの中からデータを持ってくる
    user2 = User.objects.all()
    print(user2)


```

コンソール
```
<QuerySet [<User: maeyama>, <User: vzxc>, <User: miwa>, <User: ji>, <User: kako>, <User: hina>]>
```


- 属性を指定して取ってくる

{モデル}.objects.get(username='maeyama')

{モデルのインスタンス}.email

views.py
```py
    #maeyamaという名前をもつユーザを指定。
    user3 = User.objects.get(username='maeyama')
    print(user3.email)

```

コンソール
```
maeyama@example.com
```

### ちなみに

views.py
```
print(request.POST)
```

コンソール
```
<QueryDict: {'csrfmiddlewaretoken': ['VxMLtF7LO4y3UZqDZIdHpVGVtCwAI6dk8RALChk1odsy4rh6DWn7XF3BZYU80338'], 'username': ['a'], 'password': ['a']}>
[05/Aug/2020 11:29:32] "POST /signup/ HTTP/1.1" 200 2031
```


## サインアップの重複を防ぐ

既に登録してある名前でサインアップしようとすると、
エラーが出てしまう。
```
IntegrityError at /signup/
```

重複を防ぐ必要あり。

try,exceptを使用する。(トライキャッチファイナリーみたいなやつ。)


### html

- if文：djangoの文法

エラーが存在した場合
```
    {% if error %}
    {% endif %}
```

- views.pyで指定した、
```
            return render(request, 'signup.html',{'error': 'このユーザは登録されています。'})
```
のrenderの引数の3つめ(コンテキスト)、辞書型の左の部分をhtmlで記載して、表示をする。
```
    {% if error %}
    {{ error }}
    {% endif %}

```

## ログイン機能の実装

オフィシャルドキュメント
https://docs.djangoproject.com/ja/3.0/topics/auth/default/



ログイン関数を使用して、ユーザをログインさせる



- 認証
```py
from django.contrib.auth import authenticate, login


def my_view(request):
    #postメソッドで、usernameとpasswordを受け取る。
    username = request.POST['username']
    password = request.POST['password']
    #authenticate=認証をする
    #ユーザテーブルのデータを読み込んで、そのユーザの権限だったり特徴を認証する必要がある。
    user = authenticate(request, username=username, password=password)
```

- ログイン

認証の後にログイン手続きを行う

```py
 if user is not None:
     #ブラウザから受け取ったリクエストと認証されたユーザを引数にとってログインを行う
        login(request, user)
        # Redirect to a success page.
        ...
    else:
        # Return an 'invalid login' error message.
        ...
```

## functionbasedbview

views.pyでメソッドで処理を書いている。urls.pyでメソッド呼び出ししている。

## renderとredirectの違い

- render : URLはそのままで、画面のみ指定したhtmlファイルの画面を表示する
- redirect : 指定したファイルを表示するURLを再度リクエストする。(url自体がかわる)

## render



受け取ったリクエスト(引数1コめ)をもとに、htmlファイル(引数2コめ)をかえす。その時htmlファイルに埋め込みたいデータ(引数3コめ)がある
場合は指定する。

view.py

```py
    return render(request,'signup.html',{'some': 100}) 
    return render(request,'login.html')

```


## redirect


urls.pyのname属性で指定しているurlの名前を使用して、返すページを指定する。

```py
    return redirect('signup')

```

## マイクロポストを実装する

list.htmlを作成する

マイクロポストのモデルを作成する(models.pyを作成する)

- imageについて
    画像の保存先を決めなければいけない。
    upload_toパラメーターの設定をする必要があるが、ブランクでよい。
    settings.pyのほうでさきに設定しているデフォルトから、さらに細かい設定をする時に使う用のパラメーターのため。

- makemigrationsとmigrateを実行する

- admin.pyにモデルを読み込ませるために記載をする
```py
from django.contrib import admin
from .models import BoardModel

admin.site.register(BoardModel)
```

### imageファイルの設定(staticファイルの設定)

    画像の保存先を決めなければいけない。

    upload_toパラメーターの設定をする必要があるが、ブランクでよい。

    settings.pyのほうでさきに設定しているデフォルトから、さらに細かい設定をする時に使う用のパラメーターのため。
    
    画像はSTATICファイル！！

- settings.pyで2つ設定する
    - 1.MEDIA_ROOT

    settings.py
    ```py
    #画像ファイルをアップロードする場所
    MEDIA_ROOT= os.path.join(BASE_DIR,'media')

    ```

    - 2.画像を表示するURLを指定する
        (webサーバの中で設定をする必要がある。djangoはデータを組み合わせて扱う。画像はurlと1対1の関係になるため、djangoではなく、webサーバ側で扱う必要がある。)

        **ただし今から記載するのは開発環境のみに適用できる！！**

    settings.py
    ```py
    MEDIA_URL = '/medi/'
    ```

- urls.pyでルーティングする

    公式
    https://docs.djangoproject.com/en/3.0/howto/static-files/

    

    urlパターンで、MEDIA_URLというurlが撃ち込まれると、MEDIA_ROOTにある画像が返される。
    ```py
        from django.conf import settings
        from django.conf.urls.static import static

        urlpatterns = [
            # ... the rest of your URLconf goes here ...
        ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    ```

    http://localhost:8000/medi/IMG_5806_rP9bETx.JPG
    をurlとしてブラウザに与えると画像が返される。

## custom cssを読み込ませる設定をする(staticファイルの設定)

cssファイルもimageファイルと同じように設定を進めていくことが可能。(STATICファイルなので！！)

modelの中で指定をしていくのではなく、固有のcssファイルはwebサーバに扱ってもらう領域。

- static_root

    ローカルで作成している場合は使用しない！！

    #static_rootは本番環境で使用する
    #各アプリで使用しているstaticファイルを集約するコマンドを本番環境では使用する。
    STATIC_ROOT 

- staticfile_buildsとstatic_url

settings.py
```py

#cssファイルの場所を知らせる(STATICFILE_BUILDSでで)

STATIC_URL = '/sta/'

STATICFILES_DIRS = [
        os.path.join(BASE_DIR,'static')
]

```

- 固有のstaticファイルの作成

プロジェクトルート/static/〜〜.css

を作成

cssファイルには、

https://getbootstrap.com/docs/4.5/examples/sign-in/

bootstrapのページのソースの表示から、
固有のcssファイルの中身(signin.css)をコピペする


- 作成した固有のcssファイルをtemplateに読み込ませる。
    固有のcssを当てたいhtmlファイルに記載する
    
    
    signin.html
    ```html
        {% extends 'base.html' %}

        {% block customcss %}
        <link rel='stylesheet' type='text/css' href="{% static 'style.css' %}">
        {% endblock customcss %}

    ```
    
    
- urls.pyに記載して、ルーティングする

https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL,STATIC_ROOT

```py
urlpatterns = [
    # ... the rest of your URLconf goes here ...
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
```

- load staticする
hrmlファイルの中で、STATICファイルを読み込ませるためのおまじない、
```html
{% load static %}
```
を記載する

## マイクロポストのデータを表示する機能を実装する


views.py


```py
def listfunc(request):
    # BoardModelのオブジェクトを全てとってくる。
    objects_list = BoardModel.objects.all()
    # list.htmlを返す。とってきたmodelをlist.htmlにobject_listとして渡す。
    return render(request,'list.html',{'object_list':objects_list})

```

list.html
```html
        <!-- 渡された全てのモデル、object_listを表示する -->
        {% for item in object_list %}
            <div class="alert alert-success" role="alert">
                <!-- 各属性ごとに表示 -->
                <p>タイトル：{{item.title}}</p>
                <p>投稿者：{{item.author}}</p>
                <button type="button" class="btn btn-primary btn-sm">Small button</button>
                <button type="button" class="btn btn-secondary btn-sm">Small button</button>
            </div>
        {% endfor %}

```

## ログイン状態の判定機能の実装


- 前提
django adminページの右斜め上のlogoutページからログアウトして、listを見に行っても、すべて見えてしまう。
loginしているか確認して、listを見せる見せないの判断をする機能を使用したい。


- login required デコレータを関数につけてあげる！

https://docs.djangoproject.com/ja/3.0/topics/auth/default/#the-login-required-decorator

もしユーザがログインしていなければ、settings.LOGIN_URL にリダイレクト

```py
from django.contrib.auth.decorators import login_required

@login_required
def my_view(request):
    ...

```

views.pyのlistfuncメソッドの前にlogin requiredデコレータをつけてあげる。

- settings.pyにLOGIN_URLを設定する。

```py
# login requiredデコレータのための設定

LOGIN_URL = '/login/'
```
listfuncを実行する際(localhost:8000/listを表示)、ログインしていなければ、localhost:8000/loginにリダイレクトする


### ちなみに。。。デコレータとは？

```
@~~~~
def ~~~(~~~~)
```
の@の部分。


関数の前につけると、デコレータで指定した処理を実行してくれる。

## ログアウト機能の実装

公式URL
https://docs.djangoproject.com/ja/3.0/topics/auth/default/#the-login-required-decorator


リクエストを投げて、このリクエストを受け取ると、ログアウトされる。

- views.py
logoutfuncの実装

入力：リクエスト
出力：ログアウトする&ログアウトした後のページ

```py
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    # 成功したらloginページに遷移する
    return redirect('login')
```


- list.html
押されると、/logout/を呼び出すリンクをはる。

```html
    <a href="{% url 'logout' %}">ログアウト</a>
```
ログアウトのurlが呼び出される(つまりリクエストが投げられる)ので、logoutfuncが実行され、ログアウトされる。


## 詳細ページの作り込み
投稿の詳細を表示できるようにする。(メソッド呼び出し 又の名をfunctionbased view)

- urls.py
views.pyからメソッドをインポートするのを忘れないようにする。
```py
    path('detail/<int:pk>', detailfunc, name='detail'),


```
- views.py


```py
入力：1.httpリクエスト　2.プライマリーキー
出力：詳細画面(detail.htmlにプライマリーキーで指定されたBoardModelのデータをobjectという名前で渡す)

#個別のurlで呼び出すため、引数にプライマリーキーが必要となる
def detailfunc(request, pk):
    object = BoardModel.objects.get(pk = pk)
    return render(request, 'detail.html', {"object": object})
```

- detail.html

    - object.{modelのカラム名}を使用して、表示させる。


    - 画像は、imgタグの中で　{モデルの名前}.{画像のカラム名}.url　を書く。

```html

                <p>タイトル：{{object.title}}</p>
                <p>投稿者：{{object.author}}</p>
                <p>内容：{{object.content}}</p>
                <!-- 画像の表示の仕方は暗記！{モデルの名前}.{画像のカラム名}.url -->
                <p><img src='{{object.images.url}}'></p>



```

- list.html

一覧の投稿画面(list.html)から、個別投稿に飛べるようにする

aタグを使用して、タイトルをリンクにする

```html
                <a href="{% url 'detail' item.pk %}">タイトル：{{item.title}}</p>

```
個別のurlがある(プライマリーキーを送る必要がある)リクエストを送る場合は、
{%  url    %}で、2つのパラメーターを指定する(detailfuncに2つのパラメーターを与える)
    
    - 1.urls.pyで指定されているnameでview.pyの関数を呼び出す(httpリクエスト)
    - 2.そのmodelの持つ識別子を渡す(プライマリーキー)


## いいね　ボタンの実装
**変な実装。商用にはできない**



＜流れ＞

いいねをクリック→urlがよびだされる→goodのmodelを+1するfunctionを呼び出す

### saveメソッド
views.py
```py
    #save＝オブジェクトを書き換えて新しく保存する
    post.save()
```
### views.pyその他

```py
#いいねボタンの実装
#入力：1.httpリクエスト(いいねボタンを押す) 2.プライマリーキー(どの投稿に対していいねされたのか)
#出力：詳細ページに対していいねの数が追加されたmodelを渡してあげる
def goodfunc(request, pk):
    post = BoardModel.objects.get(pk=pk)
    #goodフィールド(goodカラム)の数字を一つ追加する
    #postオブジェクトの中のフィールド
    post.good = post.good + 1
    #save＝オブジェクトを書き換えて新しく保存する
    post.save()
    #postオブジェクトとして書き換わったオブジェクトをdetail.htmlに渡してあげて、goodメソッドの出力として渡す
    return render(request, 'detail.html', {"object": post})
```

## 既読機能の実装
**変な実装。商用にはできない**


- urls.py
  ```py
    path('read/<int:pk>' , readfunc, name='read'),
  ```
- views.py
```py
#既読機能の実装

def readfunc(request, pk):
    post = BoardModel.objects.get(pk = pk)
    # ログインしているユーザの名前をとってくる。リクエストの中にログインしているユーザ名は含まれる
    post2= request.user.get_username()
    #readtextのなかに、既読した人(ログイン状態で既読ボタンを押した人)の名前を追加していく
    #readtextと参照して、今現在ログインしている人の名前がなければreadを＋１する
    if post2 in post.readtext:
        return redirect('list')

    else:
        # readのmodelに対して、＋１する
        post.read += 1
        #　readtextのmodelに対して、ボタンを押したログインユーザの名前を追加する。
        post.readtext = post.readtext + ' ' + post2
        post.save()
        return redirect('list')
```
- list.html
```html
                <a href="{% url 'read' item.pk %}" class="btn btn-success" role="button" aria-pressed="true">既読:{{item.read}}</a>

```


- detail.html
```html
                <a href="{% url 'read' object.pk %}" class="btn btn-success" role="button" aria-pressed="true">既読:{{object.read}}</a>

```

## createview

fucntionbaseviewで実装するのはちょっと複雑になってしまう。

なので、createviewに関しては今回、classbasedviewで実装する。

### create.html

name属性に、modelのフィールド (カラム名)を入れておくことにより、そのモデルのデータを呼び出すことができる。

```html

            <p>タイトル：<input type='text' name='title'></p>

```

画像をアップロードするために必要。
enctypeの設定。複数のデータを送る場合に必要な設定。(今回、テキストデータとファイルデータを送るため、この設定が必要。)
```html
<form action='' method='POST' enctype="multipart/form-data">
</form>
```

なりすましなどを防ぐために、ログインしているユーザをBoardModelのauthorにデータとして、入れる必要がある。

hiddenタグを使用！（見えないタグ.ソースの表示をすると見える！）
```html
            <p><input type='hidden' name='author' value='{{ user.username }}'></p>


```




### views.py

```py
# createviewの実装
# classbasedviewで実装する
class BoardCreate(CreateView):
    #返すページ
    template_name='create.html'
    #扱うモデル
    model = BoardModel
    #扱うカラム(扱うカラムを制限できる)
    fields = ('title','content', 'author', 'images')
    #データ作成が成功した際にどこの画面に遷移するか
    success_url= reverse_lazy('list')
```


### エラー
```
IntegrityError at /create/
NOT NULL constraint failed: boardapp_boardmodel.good
```

djangoのデフォルトの設定では、全てのデータに何か内容を入れることが必要、(nullにしてはいけない。)


今回、タイトル、内容、ファイル、author以外のデータが入っていないために、

formを送信しようとしたらエラーになった。

### エラーの解消
デフォルトのデータを最初に入れておくことによって、データがnullになることを防ぐ。


models.py
```py
    good = models.IntegerField(null=True,blank=True,default=0)
    #既読した人数
    read = models.IntegerField(null=True,blank=True,default=0)
    #既読をした人の名前を保存するスペース
    readtext = models.CharField(max_length=100,null=True,default="")
```

## ログインしているユーザにのみcreateviewを表示する

createview(classbasedview)の弱点解消

/create/の画面がログインしていないユーザにも見えてしまう


authenticateする！！(認証が完了しているかをチェックして、createviewを表示するのかを決める)

ちなみにlogin requiredというデコードを設定することはできない。(functionbased viewじゃないので！！)

htmlファイルにauthenticateをジャンゴタグで埋め込む


```html
        {% if user.is_authenticated %}
            <form action='' method='POST' enctype="multipart/form-data">{% csrf_token %}
                <p>内容：<input type='text' name='content'></p>
                <p>画像：<input type='file' name='images'></p>
                <p><input type='hidden' name='author' value='{{ user.username }}'></p>
                <input type='submit' value='作成する'>

            </form>
        {% else %}
            ログインしてください
        {% endif %}

```

