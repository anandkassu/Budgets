from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import DetailView, UpdateView, DeleteView
from .models import ExpenseItem, Message
from .form import ContactForm
from django.contrib.auth.decorators import login_required


@csrf_exempt
def home(request):
    return render(request, 'home.html')


class AddItemView(CreateView):
    queryset = ExpenseItem.objects.all()
    template_name = 'add_new.html'
    fields = ['title', 'date', 'amount', 'description', 'account', 'category']
    success_url = '/'


class ListItemView(ListView):
    queryset = ExpenseItem.objects.all()
    template_name = 'view_expense.html'


class DetailItemView(DetailView):
    queryset = ExpenseItem.objects.all()
    template_name = 'budgets/expenseitem_detail.html'


class UpdateItemView(UpdateView):
    queryset = ExpenseItem.objects.all()
    fields = ['title', 'date', 'amount', 'description', 'account', 'category']
    template_name = 'budgets/expenseitem_form.html'

    def get_success_url(self):
        return '/view/' + str(self.object.id)


class DeleteItemView(DeleteView):
    queryset = ExpenseItem.objects.all()
    fields = ['title', 'date', 'amount', 'description', 'account', 'category']
    template_name = 'budgets/expenseitem_confirm_delete.html'

    def get_success_url(self):
        return '/'


@login_required
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            print('validated')
            Message.objects.create(title=request.POST.get('title'), email=request.POST.get('email'),
                                   message=request.POST.get('message'))
            return HttpResponseRedirect('/')

    else:
        form = ContactForm()
    context = {'form': form}
    return render(request, 'contact_form.html', context)
