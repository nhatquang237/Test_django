from django.http import HttpResponse
from django.shortcuts import render

big_dict = {
    'Quang': 'Handsome',
    'okay' : 'Được chứ',
    'admit': 'Thừa nhận',
    'enable': 'Cho phép',
    'courses ': 'các khóa học',
    'flood': 'lụt',
    'normally': 'thông thường',
    'conventionally': 'thông thường',
}

def index(request):
    return HttpResponse('<h1> Hey guys, </h1>')

def index_new(request):
    name = "Master"
    context = {
        'name': 'Quang',
        'age': 26,
        'nationality': 'British',
    }
    return render(request, 'index.html')
#GET is used to request data from a specified resource.
##Note that the query string (name/value pairs) is sent in the URL of a GET request:
#POST is used to send data to a server to create/update a resource.
##The data sent to the server with POST is stored in the request body of the HTTP request:
###https://www.w3schools.com/tags/ref_httpmethods.asp
def counter(request):
    text = request.POST['text']
    # print(text)
    # mean_of_word = ""
    # if text in big_dict.keys():
    #     print("Found")
    #     mean_of_word = big_dict[text]
    character_number = len(text.split())
    return render(request, 'counter.html',{'amount': character_number})
    # return render(request, 'index.html', {'mean': mean_of_word})