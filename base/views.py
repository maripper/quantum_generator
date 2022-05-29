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
    sender= req.post('http://127.0.0.1:8000/measurements/restart/',data={ }) 
    while(n<1000):
        Q = [0, 1]
        print(random.choice(Q))
        Q = random.choice(Q)
        sender= req.post('http://127.0.0.1:8000/measurements/receiver/',data={'bit':Q})
        receiver= req.post('http://127.0.0.1:8000/measurements/sender/',data={'bit':Q})
        n = n+1 
        print(Q)
    compare,crypto_key_ind,compare_data_R,compare_data_S,compare_msg,cryptokey_data_R,cryptokey_data_d,cryptokey_msg = req.post('http://127.0.0.1:8000/measurements/compare/',data={'size':1000})
    return JsonResponse({'compare':compare,'cryptographic':crypto_key_ind,'compare_data_R':compare_data_R,'compare_data_S':compare_data_S,'compare_msg':compare_msg,'cryptokey_data_R':cryptokey_data_R,'cryptokey_data_d':cryptokey_data_d,'cryptokey_msg':cryptokey_msg})