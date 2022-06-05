from django.shortcuts import render

import requests as req

from django.http import JsonResponse,HttpResponse  

import random

from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt

import json

import ast

# perform business logic

@csrf_exempt

def quantum_computer(request):

    return render(request,"home.html",{})

    # perform business logic

@csrf_exempt

def testing(request):

    return render(request,"test.html",{})

@csrf_exempt

def doc(request):

    return render(request,"doc.html",{})

@csrf_exempt  

def start(request):

    n = request.POST

    n = 100

    # response= req.post('https://qubit-operators.herokuapp.com/qubit_operators/receiver/',data={'size':n})

    # response= req.post('https://qubit-operators.herokuapp.com/qubit_operators/safe_poc/',data={'size':n})

    # response= req.post('https://qubit-operators.herokuapp.com/qubit_operators/safe_poc/',data={'size':n}).json()['context']
    response= req.post('https://qubit-operators.herokuapp.com/qubit_operators/safe_poc/',data={'size':n}).json()['context']

    # response = response.replace("'", '"')

    response = json.loads(response)

    # response = ast.literal_eval(response)

    print('RESPONSE: -------------------------------------\n',response)

    file = open("sender_key.txt","w")
    file.write(json.dumps({'key':response['sender_key']}))
    file.close()

    file = open("receiver_key.txt","w")
    file.write(json.dumps({'key':response['receiver_key']}))
    file.close()

    return JsonResponse({'sender_and_receiver_comparing_sample_equivalent':response['status'],'message':response['sender_data'],'sender_key':response['sender_key'],'receiver_key':response['receiver_key'],'receiver_base':response['receiver_base'],'sender_base':response['sender_base'],'receiver_results':response['receiver_data'],'sender_results':response['sender_data'],'tests_size':response['n']})

@csrf_exempt  

def start_eve(request):

    n = request.POST

    n = 100

    # response= req.post('https://qubit-operators.herokuapp.com/qubit_operators/receiver/',data={'size':n})

    # response= req.post('https://qubit-operators.herokuapp.com/qubit_operators/safe_poc/',data={'size':n})

    # response= req.post('https://qubit-operators.herokuapp.com/qubit_operators/safe_poc/',data={'size':n}).json()['context']
    response= req.post('https://qubit-operators.herokuapp.com/qubit_operators/eve_poc/',data={'size':n}).json()['context']

    # response = response.replace("'", '"')

    response = json.loads(response)

    # response = ast.literal_eval(response)

    print('RESPONSE: -------------------------------------\n',response)

 
    file = open("sender_key.txt","w")
    file.write(json.dumps({'key':response['sender_key']}))
    file.close()

    file = open("receiver_key.txt","w")
    file.write(json.dumps({'key':response['receiver_key']}))
    file.close()
    return JsonResponse({'sender_and_receiver_comparing_sample_equivalent':response['status'],'sender_key':response['sender_key'],'receiver_key':response['receiver_key'],'receiver_base':response['receiver_base'],'sender_base':response['sender_base'],'tests_size':response['n'],'message':response['sender_bits'],'receiver_results':response['receiver_data'],'sender_results':response['sender_data'],'intercepted_message':response['intercepted_message']})

@csrf_exempt  

def test(request):

    n = request.POST
    receiver_key = []
    sender_key = []
    # with open("receiver_key.txt") as file:
    #     for line in file:
    #         print(line)
    #         receiver_key.append(json.loads(line)['key'])
    # with open("sender_key.txt") as file:
    #     for line in file:
    #         print(line)
    #         sender_key.append(json.loads(line)['key'])
    #     print({'sender_key':sender_key})

    files_sender = {'upload': open('receiver_key.txt','rb')}
    files_receiver = {'upload': open('sender_key.txt','rb')}

    response= req.post('https://qubit-operators.herokuapp.com/qubit_operators/encrypt/',files=files_sender).json()
    resp_decr = req.post('https://qubit-operators.herokuapp.com/qubit_operators/decrypt/',files=files_receiver,data={'msg':response['encrypted_msg']}).json()
    state = response['msg'] == resp_decr['decrypt_msg']
    context = {'are_the_msgs_equal':state,'msg':response['msg'],'encrypted_msg':response['encrypted_msg'],'decrypted_msg':resp_decr['decrypt_msg']}
    print(context)
    return JsonResponse(context)

# @csrf_exempt

# def start(request):

#     n=0

#     sender= req.post('https://qubit-operators.herokuapp.com/qubit_operators/restart/',data={ })

#     while(n<32):

#         Q = [0, 1]

#         print(random.choice(Q))

#         Q = random.choice(Q)

#         sender= req.post('https://qubit-operators.herokuapp.com/qubit_operators/receiver/',data={'bit':Q})

#         receiver= req.post('https://qubit-operators.herokuapp.com/qubit_operators/sender/',data={'bit':Q})

#         print(sender,receiver)

#         n = n+1

#         print(Q,n)

#     dict = req.post('https://qubit-operators.herokuapp.com/qubit_operators/compare/',data={'size':32})

#     # print(type(dict))  

 

#     return JsonResponse(dict.json())
