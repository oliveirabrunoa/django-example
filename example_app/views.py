from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
import requests
import json
# Create your views here.


def teste_requisicao(request):

    response = requests.get('https://portalusebens-homolo.websiteseguro.com/api/vehicles?q=honda+civic+exs+1.8', headers={'access_token': '6dd187a4f4419d6beaba8743e8d2b023a258e9d2'},  verify=False)
    response_json = json.loads(response.text)
    return HttpResponse(json.dumps(response_json, indent=4, sort_keys=True), content_type="application/json")
