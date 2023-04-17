from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate,logout,update_session_auth_hash
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm,LoginForm,ChatForm,ChatLoginForm,ChangePasswordForm
from .models import Chat,Message
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.


def index(request):
    return render(request,"index.html")

def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            useremail = form.cleaned_data.get('email')
            user = User.objects.filter(username=username).first()
            email = User.objects.filter(email=useremail).first()
            if user is not None:
                messages.warning(request,"Username is already taken")
                return redirect("register")
            if email is not None:
                messages.warning(request,"Email is already taken")
                return redirect("register")
            password = form.cleaned_data.get('password')
            
            newUser = User(username = username,email=useremail)
            newUser.set_password(password)
            
            newUser.save()
            auth_login(request,newUser)
            messages.success(request,"You Have Registered Successfully...")
            return redirect("index")
        else:
            form = RegisterForm()
            context = {
                'form' : form
            }  
            return render(request,"register.html",context)
    else:
        context = {
            'form':form
        }
        return render(request,"register.html",context)

def login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            context = {
                'form':form
            }
            if user is None:
                messages.warning(request,"Username or Password is wrong!")
                return render(request,"login.html",context)
            auth_login(request,user)
            messages.info(request,"You have Logged In")
            return redirect("index")
        else:
            messages.warning(request,"Form is not valid")
            return redirect("login")
    return render(request,"login.html",{'form':form})

def loggedout(request):
    logout(request)
    messages.info(request,"You have Logged Out")
    return redirect("index")

@login_required(login_url="/login/")
def chats(request):
    keyword = request.GET.get('keyword')
    if keyword:
        chats = Chat.objects.filter(chat_name__contains=keyword)
        return render(request,"chats.html",{'chats':chats})
    chats = Chat.objects.all()
    return render(request,"chats.html",{'chats':chats})

@login_required(login_url="/login/")
def createchat(request):
    form = ChatForm()
    if request.method == "POST":
        form = ChatForm(request.POST)
        if form.is_valid():
            chat_name = form.cleaned_data.get('chat_name')
            password = form.cleaned_data.get('password')
            newchat = Chat(chat_name=chat_name,chat_password=password,chat_admin=request.user.username)
            newchat.save()
            return redirect("msg:chat",newchat.id)
    return render(request,"create.html",{'form':form})

@login_required(login_url="/login/")
def loginchat(request,chat_id):
    chat = get_object_or_404(Chat,id=chat_id)
    form = ChatLoginForm()
    if request.method == "POST":
        form = ChatLoginForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data.get('password')
            if password != chat.chat_password:
                messages.warning(request,"Password is wrong!")
                return redirect("msg:loginchat",chat_id)
            return redirect("msg:chat",chat_id)
    return render(request,"loginchat.html",{'form':form,'chat':chat})

@login_required(login_url="/login/")
def chat(request,chat_id):
    chat = get_object_or_404(Chat,id=chat_id)
    messages = chat.messages.all()
    """if request.method == "POST":
        msg = request.POST.get('msg')
        if msg:
            newmsg = Message(author=request.user.username,message=msg)
            newmsg.chat = chat
            newmsg.save()
            return redirect("msg:chat",id)
        return redirect("msg:chat",id)"""
    return render(request,"chat.html",{'chat':chat,'message':messages})

@login_required(login_url="/login/")
def deletechat(request,chat_id):
    if request.method == "POST":
        chat = get_object_or_404(Chat,id=chat_id)
        chat.delete()
        messages.info(request,"Chat has been deleted successfully!")
        return redirect("msg:chats")
    return render(request,"deletechat.html",{'id':chat_id})

@login_required(login_url="/login/")
def profile(request,slug):
    
    return render(request,"profile.html")

@login_required(login_url="/login/")
def allchats(request):
    if not request.user.is_staff:
        messages.warning(request,"Just admins can visit")
        return redirect("msg:chats")
    keyword = request.GET.get('keyword')
    if keyword:
        chats = Chat.objects.filter(chat_name__contains=keyword)
        return render(request,"chats.html",{'chats':chats})
    chats = Chat.objects.all()
    return render(request,"chats.html",{'chats':chats})

def changepassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.warning(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'changepassword.html', {
        'form': form
    })
    
    
def about(request):
    return render(request,"about.html")