from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import RegistrationForm, UserEditForm, ProfileEditForm
from .models import Profile
from django.contrib import messages


@login_required
def home(request):
    context = {'tab': 'home'}
    return render(request, 'user_account/home.html', context)

#https://docs.djangoproject.com/en/3.2/topics/forms/#the%20view
def register(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid(): # (method) run validation routines for all its fields
            new_user = user_form.save(commit=False) # Create a new user, avoid saving it
            #https://docs.djangoproject.com/en/3.2/ref/forms/api/#django.forms.Form.clean
            new_user.set_password(user_form.cleaned_data['password']) #set_password() handles hashing
            new_user.save() #Once passed the cleaner validator, save the new user
            Profile.objects.create(user=new_user) ## Create a profile associated to the new_user
            return render(request, 'user_account/success_registration.html', {'new_user': new_user})
    else:
        user_form = RegistrationForm()
    return render(request, 'user_account/registration.html', {'user_form': user_form})


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    context = { 
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'user_account/edit.html', context)


