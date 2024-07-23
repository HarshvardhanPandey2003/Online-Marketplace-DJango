from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Item


def detail(request, pk):
    item = get_object_or_404(Item, pk=pk) #pk=pk means by the URL you'll know which item is cliked and its identified by its id
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3] 
    # exclude(pk=pk) means the item that is clicked will not be in the list

    return render(request, 'item/detail.html', {
        'item': item,
        'related_items': related_items
    })
