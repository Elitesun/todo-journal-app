from django.shortcuts import render , redirect
from django.contrib.auth.mixins import  LoginRequiredMixin
from django.views.generic import ListView , DetailView , CreateView , UpdateView , DeleteView , FormView 
from django.urls import reverse_lazy
from .models import Task , Journal
from django.contrib.auth import login , authenticate
from django.contrib.auth.views import LoginView 
from django.contrib.auth.forms import UserCreationForm

# CustomLoginView to handle user login
class CustomLoginView(LoginView):
    template_name='todo/login.html'
    redirect_authenticated_user=True
    
    def get_success_url(self):
        # Redirect to the task list after successful login
        return reverse_lazy('todo:tasks')
    
# RegisterPage view to handle user registration
class RegisterPage(FormView):
    # Template for the registration page
    template_name='todo/register.html'
    # Use Django's built-in UserCreationForm for registration
    form_class=UserCreationForm
    # Redirect authenticated users who try to access this page
    redirect_authenticated_user=True
    success_url=reverse_lazy('todo:tasks') 
    
    def form_valid(self, form):
        user = form.save()  # Save the new user
        login(self.request, user)  # Log the user in after registration
        return super().form_valid(form)  # Redirect to success_url
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            # Redirect authenticated users to the task list
            return redirect('todo:tasks')
        return super(RegisterPage,self).get(*args, **kwargs)
    
    
# TaskList view to display a list of tasks for a logged-in user
class TaskList(LoginRequiredMixin, ListView):
    model=Task
    context_object_name='tasks'
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        # Filter tasks to only include those belonging to the current user
        context['tasks']=context['tasks'].filter(user=self.request.user)
        # Count the number of incomplete tasks for the current user
        context['count']=context['tasks'].filter(complete=False).count()
        
        # Handle search functionality
        search_input=self.request.GET.get('search-area') or ''
        if search_input:
            # Filter tasks based on search input
            context['tasks']=context['tasks'].filter(title__icontains=search_input) 
        context['search_input']=search_input
        return context

# TaskDetail view to display the details of a single task
class TaskDetail(LoginRequiredMixin,DetailView):
    model=Task
    context_object_name='task'
    template_name='todo/task_detail.html'

# TaskCreate view to handle the creation of a new task
class TaskCreate(LoginRequiredMixin,CreateView):
    model=Task
    fields=['title','description','complete']       
    success_url=reverse_lazy('todo:tasks')
    template_name='todo/task_form.html'
    
    def form_valid(self, form):
        # Associate the task with the current user
        form.instance.user=self.request.user
        return super(TaskCreate,self).form_valid(form)
    
# TaskUpdate view to handle the update of an existing task
class TaskUpdate(LoginRequiredMixin,UpdateView):
    model=Task
    fields=['title','description','complete'] 
    template_name='todo/task_form.html'
    success_url=reverse_lazy('todo:tasks')
    

# TaskDelete view to handle the deletion of a task
class TaskDelete(LoginRequiredMixin,DeleteView):
    model=Task
    context_object_name='task'
    success_url=reverse_lazy('todo:tasks')
    template_name='todo/task_delete.html'
    









class JournalList(LoginRequiredMixin,ListView):
    model=Journal
    context_object_name='journals'
    template_name='todo/journal_page.html'
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['journals']=context['journals'].filter(user=self.request.user)
        return context

class JournalCreate(LoginRequiredMixin,CreateView):
    model=Journal
    fields=['title','content']
    template_name='todo/journal_form.html'
    success_url=reverse_lazy('todo:journal')
    
    def form_valid(self, form):
        form.instance.user=self.request.user
        return super(JournalCreate,self).form_valid(form)


class JournalUpdate(LoginRequiredMixin,UpdateView):
    model=Journal
    fields=['title','content']
    template_name='todo/journal_form.html'
    success_url=reverse_lazy('todo:journal')
    
class JournalDelete(LoginRequiredMixin,DeleteView):
    model=Journal
    context_object_name='journal'
    template_name='todo/journal_delete.html'
    success_url=reverse_lazy('todo:journal')
    

