from django.shortcuts import render, redirect
from .models import Customer
from .send import sendEmail


def dashboard(request):
    
    emails = request.GET.getlist('emails')
    text = request.GET.get('textt')
    #print("text = " ,text)

    for e in emails:
        sendEmail(e,text)

    if(emails != []):
        return redirect('/')

    return render(request, 'customer/index.html', {'Customers':Customer.objects.all()})





def crud_operations(request):
    firstName = request.GET.get('first_name')
    secondName = request.GET.get('second_name')
    email = request.GET.get('email')
    if firstName is not None:
        c = Customer()
        c.FirstName = firstName
        c.SecondName = secondName
        c.Email = email
        c.save()
        return redirect('/crud')

    return render(request,"customer/crudPage.html", {'Customers':Customer.objects.all()})

    
def delete(request, ids):
    
    x = ids.split(',')
    for C_id in x:
        customer = Customer.objects.get(id=int(C_id))
        customer.delete()

    return redirect('/crud')



def update(request, id, fname, sname, email):
    
    c = Customer.objects.get(id=id)
    c.FirstName = fname
    c.SecondName = sname
    c.Email = email
    c.save()

    return redirect('/crud')

