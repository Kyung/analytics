from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.shortcuts import render
from django.shortcuts import get_object_or_404

from Analytics.models import MemberhandlerPost, MemberhandlerChallenge, MemberhandlerChallengeweekactivity

# handling gdata
import gdata
import datetime
#import gdata.gauth
from gdata.analytics import client

import urllib

# Create your views here.

def member_post(request):

    post_list = MemberhandlerPost.objects.all()
    context = {'post_list': post_list}

    return render(request, 'member_post.html', context)

def challenge_list(request):

    challenge_list = MemberhandlerChallenge.objects.all()
    context = {'challenge_list': challenge_list}

    return render(request, 'challenge_list.html', context)

def challenge_detail(request):

    if len(request.POST['uuid']) == 0:
        return HttpResponse('No uuid')
    else:
        challenge_id = request.POST['uuid']

    challenge_activity = MemberhandlerChallengeweekactivity.objects.filter(challenge_uuid=challenge_id)

    context = {'challenge_activity': challenge_activity,
               'challenge_id': challenge_id}

    return render(request, 'challenge_detail.html', context)

def ganalytics(request):

    # https://developers.google.com/analytics/devguides/reporting/core/dimsmets
    result = get_ga_data(datetime.date(2014, 04, 01),
                         datetime.date(2014, 04, 20),
                         'ga:timeOnScreen', # metrics
                         'ga:screenName') # dimensions

    # metrics list
    #

    # dimension lists
    # 'ga:latitude'
    # 'ga:longitude'
    # 'ga:appVersion'
    # 'ga:screenName'

    context = {'result': result}

    return render(request, 'g_analytics.html', context)


PROJECT_NAME = 'hOurworld'
PROFILE_ID = 'ga:83495002' # fittle ID
CLIENT_ID = '486370921525-musm3tcf9oi7a8g4dik61tvcif24p997.apps.googleusercontent.com'
CLIENT_SECRET = 'CC8JbPVtZCeuy_-JOeqJOAeG'
REDIRECT_URLS = 'urn:ietf:wg:oauth:2.0:oob'
SCOPE = 'https://www.google.com/analytics/feeds/'  # Default scope for analytics

def get_token(self):
    try:

        token = gdata.gauth.OAuth2Token(client_id=CLIENT_ID,
                                        client_secret=CLIENT_SECRET,
                                        scope=SCOPE,
                                        user_agent=PROJECT_NAME)

        self.redirect(token.generate_authorize_url(redirect_uri=REDIRECT_URLS))

        return token.get_access_token()
    except:
        pass

def get_ga_client(sdate, edate, metrics, dimensions):
    my_client = gdata.analytics.client.AnalyticsClient(source=PROJECT_NAME)
    my_client.client_login('fittle.org@gmail.com',
                           'wellness2013',
                           source=PROJECT_NAME,
                           service='analytics',)

    #token = get_token()

    #my_client = gdata.analytics.client.AnalyticsClient()
    #token.authorize(my_client)

    #account_query = gdata.analytics.client.AccountFeedQuery()
    query = gdata.analytics.client.DataFeedQuery({'ids': PROFILE_ID,
                                                           'start-date': sdate,
                                                           'end-date': edate,
                                                           'metrics': metrics,
                                                           'dimensions': dimensions})

    feed = my_client.GetDataFeed(query)
    return feed

def get_ga_data(sdate, edate, metrics, dimensions):
    result = []
    feed = get_ga_client(sdate, edate, metrics, dimensions)

    for value in feed.entry:
        for dimension, metric in zip(value.dimension, value.metric):
            result.append((dimension.value, metric.value))

    return result
