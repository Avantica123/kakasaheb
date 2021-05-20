from django.shortcuts import render,HttpResponseRedirect,redirect

import sys
from subprocess import run,PIPE
from django.contrib.auth.decorators import login_required
# from instamojo_wrapper import Instamojo
# from newproject.settings import API_KEY,AUTH_TOKEN
# api = Instamojo(api_key=API_KEY, auth_token=AUTH_TOKEN, endpoint='https://test.instamojo.com/api/1.1/');
import speech_recognition as sr

import pyttsx3,webbrowser,os,random,pyautogui,requests
import pywhatkit,sys,time
import datetime
import wikipedia
import bs4
import os

from datetime import date
import subprocess

# Create your views here.
def avantica(request):
    # return render(request,'dodo.html')
    run([sys.executable,"C:\\Users\\Datta Landge\Desktop\pythonhost\\avantica.py"],shell=False,stdout=PIPE)
    return redirect("home")
def index(request):
    return render(request,"index.html")


# Create your views here.
