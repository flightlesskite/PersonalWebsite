from django.shortcuts import render
from django.http import HttpResponse

from calvin.models import Category, Page
from calvin.forms import CategoryForm, PageForm


def index(request):
    # Query the db for a list of ALL categories currently stored.
    # Place the list in the context_dict
    # that will be passed to the template engine.

    category_list= Category.objects.all()
    page_list= Page.objects.all()

    context_dict = {'categories': category_list, 'pages': page_list}
    
    # Return a rendered response to send to client
    # We make use of shortcut func to make life easier
    # Note that the 1st param is the template we wish to use
    return render(request, 'calvin/index.html', context_dict)

def about(request):
    print(request.method)
    print(request.user)
    
    return render(request, 'calvin/about.html',{})

def projects(request):

    category_list = Category.objects.all()
    context_dict = {'categories': category_list}

    return render(request, 'calvin/projects.html', context_dict)

def contact(request):

    return render(request, 'calvin/contact.html',{})

def cv(request):

    return render(request, 'calvin/cv.html')

def show_category(request, category_name_slug):
    # Create a context dictionary which we can pass
    # to the template render engine.
    context_dict= {}

    try:
        # Can we find a category name slug with the given name?
        # If we can't, the get() method raises exception.
        # So the .get() method returns one model instance or raises an exception.
        category = Category.objects.get(slug=category_name_slug)

        # Retrieve all of the associated pages.
        # Note that filter() will return a list of page objects or empty list.
        pages = Page.objects.filter(category=category)

        # Adds our results list to the template context under name pages.
        context_dict['pages'] = pages
        # We also add the category object from db to context dictionary
        # Use this in the template to verify that the category exists.
        context_dict['category'] = category

    except Category.DoesNotExist:
        # We get here if we didn't find the specifiec category.
        # DON'T do anything...
        # Template will display "no category" message for us.
        context_dict['category'] = None
        context_dict['pages'] = None

    # Go render the response and return it to client.
    return render(request, 'calvin/category.html', context_dict)







