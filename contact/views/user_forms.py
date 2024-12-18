from django.shortcuts import render
from contact.forms import RegisterForm
def register(requets):
    form = RegisterForm()

    if requets.method == 'POST':
        form = RegisterForm(requets.POST)

        if form.is_valid():
            form.save()

    return render(
        requets,
        'contact/register.html',
        {
            'form': form
        }
    )