from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
import forms
from fot.models import *
def home(request):
	if request.method=='POST':
		return HttpResponseRedirect('/compare1/')
	return render(request,'temp.html')


"""def compare(request):
	f = PlayerForm()
	return render(request,'page.html',{'form':f})"""
i =10

def compare1(request):
 	
 	if request.method=='POST':
 		f = PlayerForm(request.POST)
 		if f.is_valid():
 			cd = f.cleaned_data
 			name = cd['name'] 
 			speed = cd['speed']
 			dribble=cd['driblle_ability']
 			age=cd['age']
 			nation = cd['nationality']
 			ft = Player1(name=name,speed=speed,driblle_ability=dribble,age=age,nationality=nation)
 			ft.save()
 			global i
 			i += 1
 			return HttpResponseRedirect('/compare2/')



 	else:
 		f = PlayerForm()		
 	return render(request,'page.html',{'form':f})		


def compare2(request):
 	
 	if request.method=='POST':
 		f = PlayerForm(request.POST)
 		if f.is_valid():
 			c = f.cleaned_data
 			name = c['name'] 
 			speed = c['speed']
 			dribble=c['driblle_ability']
 			age=c['age']
 			nation = c['nationality']
 			f = Player1(name=name,speed=speed,driblle_ability=dribble,age=age,nationality=nation)
 			f.save()
 			global i
 			i +=1
 			return HttpResponseRedirect('/results/')
 	else:
 		f = PlayerForm()		
 	return render(request,'page2.html',{'form':f})		
 	
def results(request):
	global i
 	p1 = Player1.objects.get(id=i)
 	i -= 1 	
 	p2 = Player1.objects.get(id=i)
 	power1 = p1.speed + p1.driblle_ability
 	power2 = p2.speed + p2.driblle_ability	
 	if power1 > power2:
 		message = "%s is better than %s" %(p1.name,p2.name)
 	else:
 		message = "%s is better than %s" %(p2.name,p1.name)	
 	return render(request,'results.html',{'message':message})	



  
			    

