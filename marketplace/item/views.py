from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from item.models import  Item,Category
from .forms import NewItemForm
from .forms import NewItemForm, EditItemForm
from django.db.models import Q

def items(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    items = Item.objects.filter(is_sold=False)

    if category_id:
        items = items.filter(category_id=category_id)

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, "item/items.html", {
        'items': items,
        'query': query,
        'categories': categories,
        'category_id': int(category_id)
    })
def detail(request, pk):
    item = get_object_or_404(Item, pk=pk) #pk=pk means by the URL you'll know which item is cliked and its identified by its id
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3] 
    # exclude(pk=pk) means the item that is clicked will not be in the list
    # (request , directory_name/html_page)
    return render(request, 'item/detail.html', {
        'item': item,
        'related_items': related_items
    })
@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        # What this function des is it creates a form ,does not save it yet
        # Stored the created by field nand then saves it in the database
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            # The request.use is saved in the django authentication middleware
            item.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = NewItemForm()
        #If the request method is not POST (i.e., it's a GET request), it creates an empty NewItemForm

    return render(request, 'item/forms.html', {
        'form': form,
        'title': 'New item',
    })

@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)

    return render(request, 'item/forms.html', {
        'form': form,
        'title': 'Edit item',
    })

@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()

    return redirect('dashboard:index')


