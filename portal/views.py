from django.http import HttpResponse
import random
def hello_world(request):
    return HttpResponse("Hello World")

def root_page(request):
    return HttpResponse("Root page")

def random_number(request,max_num=100):
    random_num = random.randrange(0, int(max_num))

    msg = "Random number b/w 0 and %s = %d" %(max_num,random_num)

    return HttpResponse(msg)
