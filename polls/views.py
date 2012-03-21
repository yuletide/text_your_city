# Create your views here.
import logging, json

from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from django.template import Context, loader, RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from polls.models import Poll, Choice
from tropo import Tropo

logger = logging.getLogger(__name__)

def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    return render_to_response('polls/index.html', {'latest_poll_list':latest_poll_list})

    #    t = loader.get_template('polls/index.html')
    #    c = Context({
    #'latest_poll_list': latest_poll_list,
    #   })
    #   return HttpResponse(t.render(c))

    #def detail(request, poll_id):
        #p = get_object_or_404(Poll, pk=poll_id)
        #return render_to_response('polls/detail.html', {'poll': p}, context_instance=RequestContext(request))

    #def results(request, poll_id):
        #p = get_object_or_404(Poll, pk=poll_id)
        #return render_to_response('polls/results.html', {'poll': p})

@csrf_exempt
def tropo(request):
    t = Tropo()
    post = json.loads(request.raw_post_data)
    """i.e. 
    {u'session': {u'accountId': u'116309',
      u'callId': u'84f41109d43f2fd15acd7b14b2d41aff',
      u'from': {u'channel': u'TEXT',
       u'id': u'16178754091',
       u'name': None,
       u'network': u'SMS'},
      u'headers': {u'CSeq': u'1 INVITE',
       u'Call-ID': u'jtx7xm',
       u'Contact': u'<sip:10.6.93.101:5066;transport=udp>',
       u'Content-Length': u'124',
       u'Content-Type': u'application/sdp',
       u'From': u'<sip:43E9CB5D-990F-40F1-B651FEB065A75608@10.6.61.201;channel=private;user=16178754091;msg=Haaa;network=SMS;step=1>;tag=mmmvpu',
       u'Max-Forwards': u'70',
       u'To': u'<sip:9996208444@10.6.69.204:5061;to=12677024939>',
       u'Via': u'SIP/2.0/UDP 10.6.93.101:5066;branch=z9hG4bKytsld7'},
      u'id': u'1cbd4a93b582ac4ea339a311b30fd9b5',
      u'initialText': u'Haaa',
      u'timestamp': u'2012-03-20T23:46:12.447Z',
      u'to': {u'channel': u'TEXT',
       u'id': u'12677024939',
       u'name': None,
       u'network': u'SMS'},
      u'userType': u'HUMAN'}}
    """
    json = {'hi':'i dunnooooo'}
    print request
    print '======='
    if request.method == 'POST':
	print request.POST['msg']
	print request.POST['user']
	print "POST"
	print request.POST
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
