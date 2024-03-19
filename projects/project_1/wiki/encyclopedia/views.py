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
    query = request.GET.get('q')
    if query in entries:
        return redirect('entry', title=query)
    else:
        return render(request, 'encyclopedia/search_results.html', {'entries': entries, 'query': query})