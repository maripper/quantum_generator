from django.shortcuts import render
import requests as req
from django.http import JsonResponse,HttpResponse   
import random
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# perform business logic
@csrf_exempt
def quantum_computer(request):
    return render(request,"home.html",{})
    # perform business logic
@csrf_exempt
def start(requests):
    n=0
    sender= req.post('https://qubit-operators.herokuapp.com/measurements/restart/',data={ }) 
    while(n<32):
        Q = [0, 1]
        print(random.choice(Q))
        Q = random.choice(Q)
        sender= req.post('https://qubit-operators.herokuapp.com/measurements/receiver/',data={'bit':Q})
        receiver= req.post('https://qubit-operators.herokuapp.com/measurements/sender/',data={'bit':Q})
        print(sender,receiver)
        n = n+1 
        print(Q,n)
    dict = req.post('https://qubit-operators.herokuapp.com/measurements/compare/',data={'size':32})
    # print(type(dict))  

    return JsonResponse(dict.json())