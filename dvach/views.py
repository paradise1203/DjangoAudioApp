from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from dvach.models import Post
from dvach.models import Comment
from datetime import datetime
from django.core.urlresolvers import reverse


def show_dvach(request):
    if request.method == 'POST':
        p = Post()
        p.text = request.POST['text']
        p.pub_date = datetime.now()
        p.save()
        return HttpResponseRedirect(reverse("show_dvach"))
    else:
        posts = Post.objects.order_by("-pub_date")
        return render(request, "index.html", {'title': 'Hi there',
                                              'posts': posts})


def comment(request, post_id):
    if request.method == 'POST':
        c = Comment()
        c.text = request.POST['text']
        c.pub_date = datetime.now()
        c.post_id = post_id
        c.save()
        return HttpResponseRedirect(reverse('comment', args=(post_id,)))
    else:
        post = Post.objects.get(id=post_id)
        comments = post.comment_set.all()
        return render(request, "comment.html", {'title': 'Hi there',
                                                'post': post,
                                                'comments': comments})
