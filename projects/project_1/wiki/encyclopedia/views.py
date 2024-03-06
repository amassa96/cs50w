from django.shortcuts import render, get_object_or_404
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