from django.shortcuts import render


def post_list(request):
    return render(request, 'blog/post_list.html', {})

    #post_list という関数（def から始まる部分のことです）を作りました。これは request を引数に取ります。
    #blog/post_list.html テンプレートを（色々なものを合わせて）組み立てる render という関数を呼び出して得た値を return しています。
# Create your views here.
