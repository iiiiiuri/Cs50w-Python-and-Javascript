import random
from django import forms
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponse
from markdown2 import Markdown
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, title):

    get_title = util.get_entry(title)

    if get_title != None:
        entry_HTML = Markdown().convert(get_title)
        return render(request, "encyclopedia/entry.html", {
          "title": title,
          "entry": entry_HTML,

          })
    else:
        return render(request, "encyclopedia/error.html", {
          "title": title,
          "message" : "Error Page Not Found"
          })
    

def search(request):
    if request.method == "POST":
        query = request.POST.get('q')
        
        if query:
            entry = util.get_entry(query)
            
            if entry is not None:
                entry_html = Markdown().convert(entry)
                return render(request, "encyclopedia/entry.html", {
                    "title": query,
                    "entry": entry_html,
                })
            else:
                all_entries = util.list_entries()
                recommendations = [entry for entry in all_entries if query.lower() in entry.lower()]
                return render(request, "encyclopedia/search.html", {
                    "recommendations": recommendations
                })




def new(request):
    if request.method == "GET":
        return render(request, "encyclopedia/new.html")
    else:
        title = request.POST['title']
        content = request.POST['content']
        titleFill = util.get_entry(title)
        if titleFill !=None:
            return render(request, "encyclopedia/error.html",{
                "message" : "This page already exists"
            })
        else:
            util.save_entry(title, content)
            entry_html = Markdown().convert(content)
            return render(request, "encyclopedia/entry.html", {
              "title": title,
              "entry": entry_html,
        
              })
            

def edit(request):    
    if request.method == "POST":
        title = request.POST['entry_title']
        content = util.get_entry(title)
        
    return render(request, "encyclopedia/edit.html",{
        "title": title,
        "content": content,
    }    ) 
            
            
def data_change(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        util.save_entry(title,content)
        entry_html = Markdown().convert(content)
        return render(request, "encyclopedia/entry.html", {
              "title": title,
              "entry": entry_html,
        
              })
        
def randomize(request):
    full_list = util.list_entries()
    rand_entry = random.choice(full_list)
    content= util.get_entry(rand_entry)
    content = Markdown().convert(content)
    return render(request, "encyclopedia/entry.html",{
        "title" : rand_entry,
        "entry" : content,
    }) 
    