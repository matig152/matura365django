from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .forms import BaseForm, TestForm, ContactForm
from django.contrib import messages
from .utility import Zadanie, parsujZadania, filtrujZadania, losujZad, dzialText, trudnoscText, dzialTematy, generujTest, tematyText, przegladajBaze
from .arkusze import generuj2023, generuj2015, generujMalaMatura, losujZadGlowna
from django.core.mail import send_mail

# Create your views here.
def home(request):
    zadanie = losujZadGlowna()
    context={
        "zadanie":zadanie
    }
    return render(request, 'home.html', context)


def losujzadanie(request):
    form = BaseForm()
    context = {"form":form, "action":"/losujzadanie"}
    if (request.method == 'POST'):
        form = BaseForm(request.POST)
        form.is_valid()
        if (True):
            dzial = form.cleaned_data['dzial']
            tematylista = request.POST.getlist('tematy')
            trudnosci = form.cleaned_data['trudnosc']
            if(len(tematylista)==0 or len(trudnosci)==0):
                messages.error(request, 'Wprowadź parametry!')
                return HttpResponseRedirect("/losujzadanie")
            trudn = []
            for x in trudnosci:
                trudn.append(int(x))
            try:
                zadanie = losujZad(dzial, tematylista, trudn)
            except ValueError:
                messages.error(request, 'Nieprawidłowe tematy!')
                return HttpResponseRedirect("/losujzadanie")
            meta = f"Dział: {dzialText(dzial)}<br>Temat: {zadanie.temat}<br>Poziom trudności: {trudnoscText(zadanie.trudnosc)}"
            context = {
                'meta': meta,
                'zadanie':zadanie,
                "action":"/losujzadanie"
            }
            return render(request, 'wygenerowanezadanie.html', context)
        else:
            messages.error(request, 'Błąd w formularzu!')
            return HttpResponseRedirect("/losujzadanie")
    else:
        return render(request, 'losujzadanie.html', context)
    
def load_tematy(request):
    dzial = request.GET.get('dzial')
    tematy = dzialTematy(dzial)
    form = BaseForm(initial={"dzial": dzial})
    form.fields['tematy'].choices = tematy
    return render(request, 'tematy_options.html', {'form':form})
    


def testparametry(request):
    form = TestForm()
    context = {'form':form, "action":"/losujzadanie"}
    if (request.method == 'POST'):
        form = TestForm(request.POST)
        form.is_valid()
        if (True):
            dzial = form.cleaned_data['dzial']
            tematylista = request.POST.getlist('tematy')
            trudnosci = form.cleaned_data['trudnosc']
            liczbazad = form.cleaned_data['liczbazad']
            if(len(tematylista)==0 or len(trudnosci)==0):
                messages.error(request, 'Wprowadź parametry!')
                return HttpResponseRedirect("/testparametry")
            trudn = []
            for x in trudnosci:
                trudn.append(int(x))
            try:
                zadaniaDoTestu = generujTest(dzial, tematylista, trudn, liczbazad)
            except ValueError:
                messages.error(request, 'Nieprawidłowe tematy!')
                return HttpResponseRedirect("/testparametry")
            meta = f"Dział: {dzialText(dzial)}<br>{tematyText(tematylista)}"
            context = {
                'typ': f"Test - {dzialText(dzial)}",
                'meta': meta,
                'zadania':zadaniaDoTestu,
                "action": "/losujzadanie"
            }
            return render(request, 'wygenerowanyarkusz.html', context)
        else:
            messages.error(request, 'Błąd w formularzu!')
            return HttpResponseRedirect("/testparametry")
    else:
        return render(request, 'testparametry.html', context)
    return render(request, 'testparametry.html', context)

def load_tematy_test(request):
    dzial = request.GET.get('dzial')
    tematy = dzialTematy(dzial)
    form = TestForm(initial={"dzial": dzial})
    form.fields['tematy'].choices = tematy
    return render(request, 'tematy_options_test.html', {'form':form})

def wyborarkusza(request):
    return render(request, 'wyborarkusza.html')

def formula2023(request):
    context = {
        'typ': "Arkusz - Formuła 2023",
        'meta': "Arkusz maturalny w formule 2023",
        'zadania': generuj2023()
    }
    return render(request, 'wygenerowanyarkusz.html', context)

def formula2015(request):
    context = {
        'typ': "Arkusz - Formuła 2015",
        'meta': "Arkusz maturalny w formule 2015",
        'zadania': generuj2015()
    }
    return render(request, 'wygenerowanyarkusz.html', context)

def malamatura(request):
    zadania = generujMalaMatura()
    context = {
        'typ': "Arkusz - Mała Matura",
        'meta': "Arkusz - mała matura",
        'zadania': zadania
    }
    return render(request, 'wygenerowanyarkusz.html', context)
    
    def get(self, request, *args, **kwargs):
        data = {
            "TytulPdf": "Arkusz 2023",
            "Tresc": zadania
        }
        pdf = render_to_pdf('pdf.html', data)
        if pdf:
            response = HttpResponse(pdf, content_type="application/pdf")
            filename = data["TytulPdf"]
            content = "inline, filename = %s" %data['Tresc']
            #response['Content-Disposition']=content
            return response
        return HttpResponse("Wystąpił błąd.")

def baza(request):
    form = BaseForm()
    context = {"form":form, "action":"/baza"}
    if (request.method == 'POST'):
        form = BaseForm(request.POST)
        form.is_valid()
        if (True):
            dzial = form.cleaned_data['dzial']
            tematylista = request.POST.getlist('tematy')
            trudnosci = form.cleaned_data['trudnosc']
            if(len(tematylista)==0 or len(trudnosci)==0):
                messages.error(request, 'Wprowadź parametry!')
                return HttpResponseRedirect("/baza")
            trudn = []
            for x in trudnosci:
                trudn.append(int(x))
            try:
                zadania = przegladajBaze(dzial, tematylista, trudn)
            except ValueError:
                messages.error(request, 'Nieprawidłowe tematy!')
                return HttpResponseRedirect("/baza")
            listatrudnosci = []
            for zadanie in zadania:
                listatrudnosci.append(trudnoscText(zadanie.trudnosc))
            context = {
                'listatrudnosci': listatrudnosci,
                'dzial': dzialText(dzial),
                'zadania': zadania, 
                "action":"/baza"
            }
            return render(request, 'bazazad.html', context)
        else:
            messages.error(request, 'Błąd w formularzu!')
            return HttpResponseRedirect("/baza")
    else:
        return render(request, 'losujzadanie.html', context)
    return render(request , 'bazazad.html')

def kontakt(request):
    if(request.method == "GET"):
        form = ContactForm()
        context = {'form': form, 'thanks': False}
    if(request.method == "POST"):
        form = ContactForm(request.POST)
        if(form.is_valid):
            imie = request.POST.get('subject')
            wiadomosc = request.POST.get('message')
            email = request.POST.get('email')
            subject = "Kontakt - strona internetowa"
            from_email = "kontakt@matura365.pl"
            message = "Nadawca: " + imie + " , adres e=mail:"+ email + "\n Treść: \n" + wiadomosc
            recipient_list = ["matura365@gmail.com"]
            send_mail(subject, message, from_email, recipient_list)
            context = {
            'form': form,
            'thanks': True,
            }
        return render(request, 'contact.html', context)
        
    return render(request, 'contact.html', context)

def instrukcje(request):
    return render(request, 'instrukcje.html')


