from django.shortcuts import render
from . import util
from django import forms
from markdown2 import Markdown
from django.http import HttpResponseRedirect
from django import forms
from django.urls import reverse
import random2


def index(request):
    if (request.method == "POST"):
        input = request.POST
        query = input['q']
        if (util.get_entry(query) != None):
            return HttpResponseRedirect(f"/{query}")
        if (query == None or query == ""):
            return HttpResponseRedirect(reverse("index"))
        entries = util.list_entries()
        results = []
        for entry in entries:
            if query.lower() in entry.lower():
                results.append(entry)
        return render(request, "encyclopedia/search.html", {
            "results": results ,
            "query": query
        })

        return render(request, "encyclopedia/search.html", {
            "query": query
        })
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def create(request):
    if (request.method == "POST"):
        input = request.POST
        titlesss = input['title']
        entries = util.list_entries()
        if titlesss in entries:
            return render(request, "encyclopedia/error.html", {
                "message" : "Entry with this title already exists. Try again with a new title."
            })
        entrysss = input['entry']
        util.save_entry(titlesss, entrysss)
        return HttpResponseRedirect(reverse("index"))
    return render(request, "encyclopedia/create.html",{})

def edit(request):
    if (request.method == "POST"):
        input = request.POST
        titless = input['title']
        entryss = input['entry']
        util.save_entry(titless, entryss)
        return HttpResponseRedirect(f"/{titless}")

def page(request, title):
    
    if (request.method == "POST"):
        input = request.POST
        titles = input['title']
        texts = util.get_entry(titles)
        return render(request, "encyclopedia/edit.html", {
            "title" : titles, 
            "entry" : texts
        })

    if (util.get_entry(title) == None):
        return render(request, "encyclopedia/error.html", {
                "message" : "Requested Entry not found. Please try again."
            })
    else:
        markdowner = Markdown()
        text = markdowner.convert(util.get_entry(title))
        return render(request, "encyclopedia/page.html", {
            "title": title , 
            "text": text
        })

def random(request):
    entries = util.list_entries()
    randtitle = random2.choice(entries)
    return HttpResponseRedirect(f"/{randtitle}")




