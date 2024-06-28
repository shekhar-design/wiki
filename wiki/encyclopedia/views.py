from django.shortcuts import render
from . import util
from markdown2 import markdown


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry_page(request, title):
    if util.get_entry(title) is None:
        return render(request, "encyclopedia/error.html", {
            "message": "The requested page was not found."
        })
    else:
        return render(request, "encyclopedia/entrypage.html",{
            "content": markdown(util.get_entry(title)),
            "title": title
        })