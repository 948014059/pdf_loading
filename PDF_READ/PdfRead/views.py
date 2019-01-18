from django.db.models import Q
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import  os
from PdfRead import models
from django.contrib.auth.hashers import make_password, check_password
import  random
from PdfRead.sendemil import  sendemils
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def pdfread(requset):
    if requset.method=="GET":
        pdfname=requset.GET.get('pdfname')
        return render(requset,'pdf_)read.html',{'pdfname':pdfname})
    if requset.method=='POST':
        pdfname=requset.POST.get('pdfname')
        if requset.session.get('name'):
            role=models.User.objects.filter(username= requset.session.get('name'))[0].role
            if role=='vip':
                state={'state':pdfname,'role':'vip'}

            else:
                state={'state':'','role':role}
        else:
            state={'state':'','role':''}
        return JsonResponse(state)
def pdflist(request):
    if request.method=="GET":
        pdflists=[]

        for name in os.listdir(r'%s/Pdfs'%(BASE_DIR)):
            pdflists.append(name)
        if request.session.get('name'):
            role=models.User.objects.filter(username=request.session.get('name'))[0].role

            return render(request,'pdf_list.html',{'pdflist':pdflists,'name':request.session.get('name'),'role':role})

        return render(request,'pdf_list.html',{'pdflist':pdflists})
def login(request):
    if request.method=='GET':
        request.session.flush()
        return  render(request,'Login_Reg.html')
    if request.method=="POST":
        state = {}
        name = request.POST.get('name')
        password = request.POST.get('password')
        print(name,password)
        # 查询密码
        md5_password = models.User.objects.filter(Q(username=name) | Q(emil=name))
        if md5_password.count() == 0:
            state = {'state': '用户不存在'}
        else:

            # 判断密码是否一致
            is_or_no = check_password(password, md5_password[0].password)

            if is_or_no:
                request.session['name'] = md5_password[0].username
                request.session['email'] = md5_password[0].emil

                state = {'state': '登录成功'}
            else:
                state = {'state': '用户名或者密码错误'}
        return JsonResponse(state)

def reg(request):
    if request.method=='POST':
        name=request.POST.get('name')
        password=request.POST.get('password')
        emil=request.POST.get('emil')

        state = {}
        # 判断数据库是否存在用户
        seam_in_models = models.User.objects.filter(username=name)
        if seam_in_models.count() != 0:
            state = {'state': '用户已存在'}
            return JsonResponse(state)

        seam_in_models = models.User.objects.filter(emil=emil)
        if seam_in_models.count() != 0:
            state = {'state': '该邮箱已经被注册'}
            return JsonResponse(state)

        # md5加密密码
        password_md5 = make_password(password, None, 'pbkdf2_sha256')
        try:
            models.User.objects.create(
                username=name,
                emil=emil,
                password=password_md5
            )
            state = {'state': '注册成功'}
        except:
            state = {'state': '系统错误'}
        return JsonResponse(state)

def ssendemil(requsest):
    if requsest.method=='GET':
        emil=requsest.GET.get('emil')
        code=random.randint(100000,999999)
        sendemils(emil,code)
        state={'state':'验证码已经发送到邮箱','code':code}
        return JsonResponse(state)
