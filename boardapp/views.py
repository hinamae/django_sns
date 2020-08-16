from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from .models import BoardModel
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
#createview
from django.views.generic  import CreateView
from django.urls import reverse_lazy

def signupfunc(request):
    #classbasedviewでいうところのobject_list
    #テーブルの中からデータを持ってくる
    user2 = User.objects.all()
    print(user2)

    user3 = User.objects.get(username='maeyama')
    print(user3.email)

    if request.method == 'POST':
        # POSTでもってきた、'username'(htmlファイルのタグの中のnameの部分)をusername2変数に格納
        username2 = request.POST['username']
        password = request.POST['password']
        try:
            #すでにusername2の名前で登録がなされている時
            User.objects.get(username=username2)
            return render(request, 'signup.html',{'error': 'このユーザは登録されています。'})
        except:
            # create_user関数を使用して、Userオブジェクトを作成する。公式ドキュメントより
            user = User.objects.create_user(username2, '', password)
            return redirect('login')

    # renderは以下3つを引数にとる
    # 1.httpリクエスト 2.classbased viewにおけるtemplate_name(呼び出されるhtmlファイル) 3.コンテキスト(辞書型データ)
    return render(request,'signup.html',{'some': 100}) 


def loginfunc(request):
    if request.method == 'POST':
        username2 = request.POST['username']
        password2 = request.POST['password']
        user = authenticate(request, username=username2, password=password2)
        if user is not None:
            #認証が成功した場合、ログインする
            login(request, user)
            #ページの返し方は、renderメソッドでも良いが、今回はredirectメソッドを使用。
            #ここで返しているページの名前は、ulrs.pyで名前をつけたもの。
            return redirect('list')
        else:
            #authenticateが失敗した場合、loginページにリダイレクト
            return redirect('login')
    else:
        #GETメソッドをもらった際(=urlにhttp://localhost:8000/loginが入力された際)
        return render(request,'login.html')

@login_required
def listfunc(request):
    objects_list = BoardModel.objects.all()
    return render(request,'list.html',{'object_list':objects_list})

def logoutfunc(request):
    logout(request)
    return redirect('login')


#個別のurlで呼び出すため、引数にプライマリーキーが必要となる
def detailfunc(request, pk):
    object = BoardModel.objects.get(pk = pk)
    return render(request, 'detail.html', {"object": object})


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