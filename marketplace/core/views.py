from django.shortcuts import render, redirect
from item.models import Category, Item
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse
from .forms import SignupForm
from django.shortcuts import render, get_object_or_404
from item.models import Category, Item
from django.db.models import Count

def index(request):
    categories = Category.objects.annotate(item_count=Count('items'))
    # So '<a href="{% url 'core:index' %}?category={{ category.id }}">' this send a request with category_id
    # and we take that as an input and store only those category item in the item variables  
    category_id = request.GET.get('category')
    if category_id:
        category = get_object_or_404(Category, id=category_id)
        items = Item.objects.filter(category=category, is_sold=False)
    else:
        category = None
        items = Item.objects.filter(is_sold=False)

    total_items = Item.objects.filter(is_sold=False).count()

    return render(request, 'core/index.html', {
        'items': items,
        'categories': categories,
        'category': category,
        'total_items': total_items,
    })
def contact(request):
    return render(request, 'core/contact.html')
def about(request):
    return render(request, 'core/about.html')

def logout_view(request):
    logout(request)
    return redirect(reverse('core:index'))

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })