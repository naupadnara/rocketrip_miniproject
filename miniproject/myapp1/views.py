from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext

from myapp1.models import Activity
from myapp1.forms import ActivityForm

def activities(request):
    latest_activity_list = Activity.objects.all().order_by('ActivityDate')
    
    return render_to_response('myapp1/myactivity.html',
    {'latest_activity_list': latest_activity_list,})

def activity_add(request):
    # sticks in a POST or renders empty form
    form = ActivityForm(request.POST or None)
    if form.is_valid():
        Activity  = form.save()
        #This is where you might chooose to do stuff.
        #cmodel.name = 'test1'
        
        Activity.save()
        return redirect(activities)

    return render_to_response('myapp1/activity_add.html',
                              {'activity_form': form},
                              context_instance=RequestContext(request))
                              
#def contact_edit(request, contact_id):
#    contact = get_object_or_404(Contact, pk=contact_id)
#    form = ContactForm(request.POST or None, instance=contact)
#    if form.is_valid():
#        contact = form.save()
#        #this is where you might choose to do stuff.
#        #contact.name = 'test'
#        contact.save()
#        return redirect(contacts)

#    return render_to_response('phonebook/contact_edit.html',
#                              {'activity_form': form,
#                               'activity_id': activity_id},
#                              context_instance=RequestContext(request))
                              
#def contact_delete(request, contact_id):
#    c = Contact.objects.get(pk=contact_id).delete()

#    return redirect(contacts)
