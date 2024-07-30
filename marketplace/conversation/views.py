from django.contrib.auth import login_required
from item.models import Item 
from django.shortcuts import render , get_object_or_404,redirect


def new_conversation(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)
    
    if item.created_by == request.user:
        return redirect('dashboard:index')
    
    conversations = 