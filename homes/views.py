from django.shortcuts import render,redirect,get_object_or_404
from .models import HomeDetails
from .forms import HomeForm
from django.contrib.auth.decorators import login_required

# Create your views here.




#Add property
# def create(request):
#     frm = HomeImage()
#     if request.POST:
#         frm = HomeImage(request.Files)
#         frm.save()
#         owner=request.POST.get('owner_name')
#         description=request.POST.get('description')
#         location=request.POST.get('location')
#         price_per_month=request.POST.get('price_per_month')
#         number_of_bedrooms=request.POST.get('number_of_bedrooms')
#         number_of_bathrooms=request.POST.get('number_of_bathrooms')
#         square_footage=request.POST.get('square_footage')
#         available_from=request.POST.get('available_from')
#         # image=request.FILES['image']
#         my_data=HomeDetails(owner=owner,description=description,location=location,price_per_month=price_per_month,number_of_bathrooms=number_of_bathrooms,number_of_bedrooms=number_of_bedrooms,square_footage=square_footage,available_from=available_from,image=image)
#         my_data.save()
    
#     return render(request,'create.html',{'frm':frm})
@login_required(login_url='/login/')
def create(request):
    frm = HomeForm()
    if request.POST:
        frm = HomeForm(request.POST,request.FILES)
        if frm.is_valid():
            frm.save()
            return redirect('index')
            
    else:
        frm = HomeForm()
    return render(request,'create2.html',{'frm':frm})


def details(request,pk):
    data_set = HomeDetails.objects.get(pk=pk)
    return render(request,'details.html',{'data':data_set})


def chat(request,pk):
    data_set = HomeDetails.objects.get(pk=pk)
    contact_number = int(data_set.contact_number)
    
    return render(request,'chat.html',{'contact_number':contact_number,'data':data_set})



def index(request):
    data_set = HomeDetails.objects.all()
    return render(request,'index.html',{'data':data_set})




def search(request):
    query = request.GET.get('q')  # Get the search query from the form
    results = HomeDetails.objects.filter(location__icontains=query) if query else []
    
    return render(request, 'search_result.html', {'query': query, 'results': results})

def user_properties(request):
    # Ensure the user is authenticated
    if request.user.is_authenticated:
        # Retrieve properties belonging to the current user
        properties = HomeDetails.objects.filter(owner=request.user)
        # Pass the properties to the template for rendering
        return render(request, 'browse.html', {'properties': properties})
    else:
        # Redirect or show an error if the user is not logged in
        return redirect('login_page')
    

def delete(request,pk):
    instance = HomeDetails.objects.get(pk=pk)
    instance.delete()
    data_set = HomeDetails.objects.all() 
    return render(request,'browse.html',{'data':data_set})
    


# from .models import Owner
# from django.contrib.auth.models import User

# def owner_properties(request, owner_id):
    # owner = get_object_or_404(User, id=owner_id)
    # properties = owner.properties.all()  # Retrieve all properties of the owner
    # context = {
    #     'owner': owner,
    #     'properties':properties,
    # }
    # return render(request, 'browse.html', context)
    