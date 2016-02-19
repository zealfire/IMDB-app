from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect
import requests
import json
import re

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            data = {'name': post.text}
            url = 'http://www.imdb.com/search/name'
            r = requests.get(url, params=data)
            superstring = r.text
            list = re.findall(r'<a href="/name/(.*)?/">', superstring)[0]
            new_url = 'http://www.imdb.com/filmosearch?sort=num_votes&explore=title_type&role=%s&ref_=nm_flmg_shw_4'%(list)
            r = (requests.get(new_url)).text
            new_print = re.findall(r'<div class="lister-list">(.*)?</div>',r,re.DOTALL|re.MULTILINE)
            title = re.findall(r'<a href="/title/tt[0-9]+?/\?ref_=filmo_li_tt".*?>(.*?)</a>',r, re.DOTALL|re.MULTILINE)
            data = '\n'.join(title[0:3])
            return render(request, 'blog/imdb.html', {'data': data})
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def imdb(request, data):
	return render(request, 'blog/imdb.html', {'data': data})
