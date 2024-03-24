from django.http import HttpResponse
from django.shortcuts import render,  redirect, get_object_or_404
import markdown
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    content = util.get_entry(title)
    if content:
        html_content = markdown.markdown(content)
        return render(request, 'encyclopedia/entry.html', {'title': title, 'content': html_content})
    else:
        return render(request, 'encyclopedia/not_found.html', {'title': title})
    
def search(request):
    entries = util.list_entries()
    query = request.GET.get('q').lower()
    for entry in entries:
        if query == entry.lower():
            return redirect('entry', title=entry)
    else:
        results = []
        for entry in entries:
            if query.lower() in entry.lower():
                results.append(entry)
        return render(request, 'encyclopedia/search_results.html', {'results': results})
    
def create(request):
    return render(request, 'encyclopedia/create-page.html')

def new_entry(request):
    entry_content = request.POST.get('new_entry')
    html_content = markdown.markdown(entry_content)
    lines = html_content.split('\n', 1)
    title = ""

    if lines and lines[0].startswith('<h1>'):
        title_line = lines[0].lstrip('<h1>').rstrip('</h1>').strip()
        title = title_line if title_line else title

    if title != "":
        if util.get_entry(title):
            return HttpResponse('Entry already exists')
        util.save_entry(title, html_content)
        return redirect('entry', title)
    else:
        return render(request, 'encyclopedia/not_found.html', {'title': 'REKT'})