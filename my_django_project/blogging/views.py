from django.shortcuts import render,HttpResponse,redirect
from .models import Post,blog_comment
from django.contrib import messages
from django.contrib.auth.models import User
from blogging.templatetags import extras


def blog_home(request):
    all_post=Post.objects.all()
    context={'all_post':all_post}
    return render(request,'blog/blog_home.html',context)


def blog_post(request,slug):
        post=Post.objects.filter(Slug=slug).first()
        comments=blog_comment.objects.filter(post=post,Parent=None)
        replies=blog_comment.objects.filter(post=post).exclude(Parent=None)
        reply_dict={}
        for reply in replies:
            if reply.Parent.Serial_no not in reply_dict.keys():
                reply_dict[reply.Parent.Serial_no]=[reply]
            else:
                reply_dict[reply.Parent.Serial_no].append(reply)
        context={'post':post,'comments':comments,'user':request.user,'reply_dict': reply_dict}
        return render(request,'blog/blog_post.html',context)

def post_comment(request):
    if request.method=='POST':
        comment=request.POST.get('comment')
        user=request.user
        post_sno=request.POST.get('post_sno')
        post=Post.objects.get(Serial_no=post_sno)
        parent_sno=request.POST.get('parent_sno')
        if parent_sno=='':
            comment=blog_comment(Comment=comment,user=user,post=post)
            comment.save()
            messages.success(request,'Your comment has been posted successfully')
        else:
            parent=blog_comment.objects.get(Serial_no=parent_sno)
            comment=blog_comment(Comment=comment,user=user,post=post,Parent=parent)
            comment.save()
            messages.success(request,'Your reply has been posted successfully')
    return redirect(f"/blog/{post.Slug}")