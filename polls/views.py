# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from polls.models import Poll, Choice
from django.template import Context, loader, RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import Http404

def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
#    t = loader.get_template('polls/index.html')
#    c = Context({
#'latest_poll_list': latest_poll_list,
#   })
#   return HttpResponse(t.render(c))
    return render_to_response('polls/index.html', {'latest_poll_list':latest_poll_list})

#def detail(request, poll_id):
    #p = get_object_or_404(Poll, pk=poll_id)
    #return render_to_response('polls/detail.html', {'poll': p}, context_instance=RequestContext(request))

#def results(request, poll_id):
    #p = get_object_or_404(Poll, pk=poll_id)
    #return render_to_response('polls/results.html', {'poll': p})

from tropo import Tropo
from django.views.decorators.csrf import csrf_exempt
import logging
logger = logging.getLogger(__name__)

@csrf_exempt
def tropo(request):
    t = Tropo()
    json = {'hi':'i dunnooooo'}
    print request
    print '======='
    if request.method == 'POST':
	print request.POST['msg']
	print request.POST['user']
	print "POST"
	print request.POST
	for key in request.POST:
	    print '-----'
	    print key
	    print len(key)
	    print request.POST[key]
	    print '------'
	for item in request.POST.items():
	    print item
	json = t.say('Thanks for your message: '+str(request.POST['msg']))
        json = t.RenderJson(json)
    return HttpResponse(json)

def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
	selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
	return render_to_response('polls/detail.html', {

	}, context_instance=RequestContext(request))
    else:
	selected_choice.votes += 1
	selected_choice.save()
	# Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('poll_results', args=(p.id,)))	
