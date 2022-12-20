from django.shortcuts import render, get_object_or_404

from .models import Post, Group


def index(request):
    NUMBER_OF_POSTS = 10
    template = 'posts/index.html'
    posts = Post.objects.order_by('-pub_date')[:NUMBER_OF_POSTS]
    title = 'Последние обновления на сайте'
    context = {
        'posts': posts,
        'title': title,
    }
    return render(request, template, context)


def group_posts(request, slug):
    NUMBER_OF_POSTS = 10
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    # posts = Post.objects.filter(group=group)[:NUMBER_OF_POSTS]
    posts = group.posts.all()[:NUMBER_OF_POSTS]
    title = 'Записи сообщества ' + group.title
    context = {
        'group': group,
        'posts': posts,
        'title': title,
    }
    return render(request, template, context)



def groups(request):
    template = 'posts/groups.html'
    group = Group.objects.order_by()
    title = "Все группы"
    context = {
        'groups': group,
        'title': title,
    }
    return render(request, template, context)