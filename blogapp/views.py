from django.shortcuts import render,redirect
from django.views.generic import DetailView
from .models import Post,Comment
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from .forms import CommentForm, SignupForms,Createform,Updateuser
from django.contrib.auth import logout

# Create your views here.
def post_list_view(request):
    post_list=Post.objects.all()
    paginator=Paginator(post_list,3)
    page_number=request.GET.get('page')
    try:
        post_list=paginator.page(page_number)
    except PageNotAnInteger:
        post_list=paginator.page(1)
    except EmptyPage:
        post_list=paginator.page(paginator.num_page)
    return render(request,'blogapp/post_list.html',{'post_list':post_list})

class BlogDetailView(DetailView):
    model=Post
    template_name='blogapp/detail.html'
    def get_context_data(self, **kwargs):
        context=super(BlogDetailView,self).get_context_data(**kwargs)
        context['form']=CommentForm
        context['comments']=Comment.objects.filter(post=self.get_object())
        return context

    def post(self,request,*args,**kwarg):
        form=CommentForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.post = self.get_object()
            instance.user = request.user
            instance.save()
            redir_url="/detail/{}".format(self.get_object().id)
            return redirect(redir_url)


def signup_view(request):
    form=SignupForms()
    if request.method=='POST':
        form=SignupForms(request.POST)
        if form.is_valid():
            form.save();
            user=form.save();
            user.set_password(user.password)
            user.save();
            return HttpResponseRedirect('/accounts/login')
    return render(request,'blogapp/signup.html',{'form':form})

def logout_view(request):
    #logout(request)
    return render(request,'blogapp/logout.html')

def dashboard_view(request):
    loggedin_user = request.user
    posts=Post.objects.filter(author=loggedin_user)
    return render(request,'blogapp/dasboard.html', {'posts': posts})

def update_view(request,pk):
    update = Post.objects.get(id=pk)
    if request.method == 'POST':
        print('ok')
        form = Updateuser(request.POST, instance=update)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'blogapp/update.html',{'update':update})

def delete_view(request,pk):
    d = Post.objects.get(id=pk).delete()
    return redirect('/')

def createview(request):
    form=Createform()
    if request.method == 'POST':
        form = Createform(request.POST)
        if form.is_valid():
            blog=form.save(commit=False)
            blog.author=request.user
            blog.save()
            return redirect('/')
    return render(request ,'blogapp/create.html',{'form':form})
