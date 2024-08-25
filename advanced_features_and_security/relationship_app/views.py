from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Library
from .models import Book
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import BookForm

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'

class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'

class RegisterView(CreateView):
    model = User
    template_name = 'relationship_app/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        form = UserCreationForm() 
        return render(request, self.template_name, {'form': form})

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)  
        return super().form_valid(form)
    
def check_admin(user):
    return user.userprofile.role == 'Admin'

def check_librarian(user):
    return user.userprofile.role == 'Librarian'

def check_member(user):
    return user.userprofile.role == 'Member'

@user_passes_test(check_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(check_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(check_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

@permission_required('relationship_app.can_add_book')
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Adjust to your book list view name
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})

@permission_required('relationship_app.can_change_book')
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Adjust to your book list view name
    else:
        form = BookForm(instance=book)
    return render(request, 'edit_book.html', {'form': form})

@permission_required('relationship_app.can_delete_book')
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect('book_list')  # Adjust to your book list view name
    return render(request, 'delete_book.html', {'book': book})