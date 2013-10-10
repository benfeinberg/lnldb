# Create your views here.

from django.views.generic.detail import DetailView

from meetings.models import MeetingAnnounce

class MeetingAnnounceView(DetailView):

    model = MeetingAnnounce
    slug_field = "uuid"
    template_name = "emails/email_notice.html"

    #def get_context_data(self, **kwargs):
        #context = super(ArticleDetailView, self).get_context_data(**kwargs)
        #context['now'] = timezone.now()
        #return context