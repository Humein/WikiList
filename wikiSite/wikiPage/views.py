from django.shortcuts import render
import logging
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from .models import WiKi
from django.db.models import Q

logger = logging.getLogger(__name__)


def index(request):
    latest_wiki_list = WiKi.objects.order_by('-pub_date')[:100]
    template = loader.get_template('wikiPage/index.html')
    context = {
        'latest_wiki_list': latest_wiki_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, title_url):
    # return HttpResponse("%s." % question_text)
    return redirect("%s" % title_url)  # url重定向


def search(request):
    q = request.GET.get('q')
    error_msg = ''
    if not q:
        error_msg = "请输入关键词"
        return render(request, 'wikiPage/results.html', {'error_msg': error_msg})

    wiki_list = WiKi.objects.filter(Q(title_text__icontains=q) | Q(author_text__icontains=q))
    print("======== %s" % wiki_list.count())
    return render(request, 'wikiPage/results.html', {'error_msg': error_msg,
                                                  'wiki_list': wiki_list})
