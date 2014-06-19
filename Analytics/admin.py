from django.contrib import admin

from Analytics.models import AuthGroup, AuthGroupPermissions, MemberhandlerActivity, DjangoSite
from Analytics.models import MemberhandlerChallengeweekoccurrence, MemberhandlerActivity, MemberhandlerActivitycard, MemberhandlerBadge, MemberhandlerMember, MemberhandlerPost
from Analytics.models import MemberhandlerTeam, MemberhandlerTeammember, MemberhandlerTeamkeyword, MemberhandlerTeampost, MemberhandlerTeammemberrecognizedactivity
from Analytics.models import MemberhandlerChallengeweek, MemberhandlerChallengeweekactivity

# Register your models here.

admin.site.register(AuthGroup)
admin.site.register(AuthGroupPermissions)
admin.site.register(MemberhandlerActivity)
admin.site.register(DjangoSite)

admin.site.register(MemberhandlerMember)

admin.site.register(MemberhandlerTeam)
admin.site.register(MemberhandlerTeammember)
admin.site.register(MemberhandlerTeamkeyword)
admin.site.register(MemberhandlerTeampost)
admin.site.register(MemberhandlerTeammemberrecognizedactivity)

admin.site.register(MemberhandlerChallengeweek)
admin.site.register(MemberhandlerChallengeweekactivity)

admin.site.register(MemberhandlerPost)