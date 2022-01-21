from asyncio.windows_events import NULL
from django.shortcuts import render, HttpResponse,redirect
from blog.models import BlogComment, Post
from django.contrib import messages
# Create your views here.

#this is to display all the "posts" available on blog   -->blog/
def blogHome(request):     
    allPosts=Post.objects.all()  
    context={'allPost':allPosts}
    return render(request, 'blog/blogHome.html',context)

# This is to display all the "blog comments" and "replies" asscociated with blog post
def blogPost(request,slug):        
    post=Post.objects.filter(slug=slug).first()
    post.views= post.views +1
    post.save()
    comments= BlogComment.objects.filter(post=post,parent=None)
    replies= BlogComment.objects.filter(post=post).exclude(parent=None)
    
    replydict={}
    for reply in replies:        
        if reply.parent.sno not in replydict.keys():
            replydict[reply.parent.sno]=[reply]
            #key--parent number #val--reply
        else:
            replydict[reply.parent.sno].append(reply)
    context={'post':post, 'comments': comments, 'user': request.user,'replydict':replydict}
    return render(request, "blog/blogPost.html", context)
    
    
#this is to submit a comment for that post
def postComment(request):
    if request.method == "POST":
        comment=request.POST.get('comment')
        user=request.user
        postSno =request.POST.get('postSno')
        post= Post.objects.get(sno=postSno)
        parentSno=request.POST.get('parentSno')
        if parentSno=="": #blank string, it means that the user is trying to post a new comment
                comment=BlogComment(comment= comment, user=user, post=post)
                comment.save()
                messages.success(request, "Your comment has been posted successfully")
        else: 
            # user is trying to post a reply because a parentSno will be sent to the back-end when the user submits the reply form
            parent= BlogComment.objects.get(sno=parentSno)
            comment=BlogComment(comment= comment, user=user, post=post , parent=parent)
            comment.save()
            messages.success(request, "Your reply has been posted successfully")
    return redirect(f"/blog/{post.slug}")