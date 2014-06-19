# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals
from django.db import models

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=80)
    class Meta:
        managed = False
        db_table = 'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')
    class Meta:
        managed = False
        db_table = 'auth_group_permissions'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'auth_permission'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    password = models.CharField(max_length=128)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    is_superuser = models.BooleanField()
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'auth_user'

class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)
    class Meta:
        managed = False
        db_table = 'auth_user_groups'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'

class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)
    action_time = models.DateTimeField()
    user = models.ForeignKey(AuthUser)
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    class Meta:
        managed = False
        db_table = 'django_admin_log'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'django_content_type'

class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'django_session'

class DjangoSite(models.Model):
    id = models.IntegerField(primary_key=True)
    domain = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'django_site'

class MemberhandlerActivity(models.Model):
    title = models.CharField(max_length=256)
    type = models.IntegerField()
    category = models.IntegerField()
    info = models.CharField(max_length=2048)
    tag = models.CharField(max_length=128, blank=True)
    seq = models.IntegerField(blank=True, null=True)
    icon_uuid = models.CharField(max_length=36, blank=True)
    uuid = models.CharField(primary_key=True, max_length=36)
    servertimestamp = models.DateTimeField(db_column='serverTimestamp', blank=True, null=True) # Field name made lowercase.
    timestamp = models.DateTimeField()
    deletedindicator = models.BooleanField(db_column='deletedIndicator') # Field name made lowercase.
    genericindicator = models.NullBooleanField(db_column='genericIndicator') # Field name made lowercase.
    weeklyindicator = models.NullBooleanField(db_column='weeklyIndicator') # Field name made lowercase.
    norepeatindicator = models.NullBooleanField(db_column='noRepeatIndicator') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'memberhandler_activity'

class MemberhandlerActivitycard(models.Model):
    activity = models.ForeignKey(MemberhandlerActivity, blank=True, null=True)
    card = models.ForeignKey('MemberhandlerCard', blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    uuid = models.CharField(primary_key=True, max_length=36)
    servertimestamp = models.DateTimeField(db_column='serverTimestamp', blank=True, null=True) # Field name made lowercase.
    timestamp = models.DateTimeField()
    deletedindicator = models.BooleanField(db_column='deletedIndicator') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'memberhandler_activitycard'

class MemberhandlerBadge(models.Model):
    name = models.CharField(max_length=256)
    info = models.CharField(max_length=2048, blank=True)
    uuid = models.CharField(primary_key=True, max_length=36)
    timestamp = models.DateTimeField()
    servertimestamp = models.DateTimeField(db_column='serverTimestamp', blank=True, null=True) # Field name made lowercase.
    deletedindicator = models.BooleanField(db_column='deletedIndicator') # Field name made lowercase.
    image_uuid = models.CharField(max_length=36, blank=True)
    card = models.ForeignKey('MemberhandlerCard', blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'memberhandler_badge'

class MemberhandlerBigbluetest(models.Model):
    diabetes = models.CharField(max_length=128, blank=True)
    exercise = models.CharField(max_length=128, blank=True)
    intensity = models.CharField(max_length=128, blank=True)
    time = models.CharField(max_length=128, blank=True)
    meal = models.CharField(max_length=128, blank=True)
    bgbefore = models.FloatField(blank=True, null=True)
    bgafter = models.FloatField(blank=True, null=True)
    units = models.CharField(max_length=128, blank=True)
    insulin = models.CharField(max_length=128, blank=True)
    hypo = models.CharField(max_length=128, blank=True)
    completiondate = models.DateTimeField(db_column='completionDate', blank=True, null=True) # Field name made lowercase.
    uuid = models.CharField(primary_key=True, max_length=36)
    servertimestamp = models.DateTimeField(db_column='serverTimestamp', blank=True, null=True) # Field name made lowercase.
    timestamp = models.DateTimeField()
    deletedindicator = models.BooleanField(db_column='deletedIndicator') # Field name made lowercase.
    challengeweekactivity = models.ForeignKey('MemberhandlerChallengeweekactivity', db_column='challengeWeekActivity_id', blank=True, null=True) # Field name made lowercase.
    teammember = models.ForeignKey('MemberhandlerTeammember', db_column='teamMember_id', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'memberhandler_bigbluetest'

class MemberhandlerCard(models.Model):
    title = models.CharField(max_length=256)
    summary = models.CharField(max_length=1024)
    detail = models.CharField(max_length=10485760)
    category = models.IntegerField()
    url_id = models.IntegerField(blank=True, null=True)
    image_uuid = models.CharField(max_length=36, blank=True)
    uuid = models.CharField(primary_key=True, max_length=36)
    servertimestamp = models.DateTimeField(db_column='serverTimestamp', blank=True, null=True) # Field name made lowercase.
    timestamp = models.DateTimeField()
    deletedindicator = models.BooleanField(db_column='deletedIndicator') # Field name made lowercase.
    ratingsum = models.IntegerField(db_column='ratingSum') # Field name made lowercase.
    ratingcount = models.IntegerField(db_column='ratingCount') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'memberhandler_card'

class MemberhandlerCardkeyword(models.Model):
    keyword = models.CharField(max_length=128)
    card = models.ForeignKey(MemberhandlerCard, blank=True, null=True)
    uuid = models.CharField(primary_key=True, max_length=36)
    servertimestamp = models.DateTimeField(db_column='serverTimestamp', blank=True, null=True) # Field name made lowercase.
    timestamp = models.DateTimeField()
    deletedindicator = models.BooleanField(db_column='deletedIndicator') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'memberhandler_cardkeyword'

class MemberhandlerCardrating(models.Model):
    rating = models.IntegerField()
    card = models.ForeignKey(MemberhandlerCard, blank=True, null=True)
    member = models.ForeignKey('MemberhandlerMember', blank=True, null=True)
    uuid = models.CharField(primary_key=True, max_length=36)
    servertimestamp = models.DateTimeField(db_column='serverTimestamp', blank=True, null=True) # Field name made lowercase.
    timestamp = models.DateTimeField()
    deletedindicator = models.BooleanField(db_column='deletedIndicator') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'memberhandler_cardrating'

class MemberhandlerChallenge(models.Model):
    title = models.CharField(max_length=256)
    info = models.CharField(max_length=2048, blank=True)
    sponsor = models.CharField(max_length=256, blank=True)
    reward = models.CharField(max_length=256, blank=True)
    weeks = models.IntegerField()
    tag = models.CharField(max_length=128, blank=True)
    options = models.IntegerField()
    badge = models.ForeignKey(MemberhandlerBadge, blank=True, null=True)
    image_uuid = models.CharField(max_length=36, blank=True)
    uuid = models.CharField(primary_key=True, max_length=36)
    servertimestamp = models.DateTimeField(db_column='serverTimestamp', blank=True, null=True) # Field name made lowercase.
    timestamp = models.DateTimeField()
    deletedindicator = models.BooleanField(db_column='deletedIndicator') # Field name made lowercase.
    sku = models.CharField(max_length=36, blank=True)
    class Meta:
        managed = False
        db_table = 'memberhandler_challenge'

class MemberhandlerChallengeweek(models.Model):
    title = models.CharField(max_length=128, blank=True)
    sequence = models.IntegerField()
    challenge = models.ForeignKey(MemberhandlerChallenge, blank=True, null=True)
    uuid = models.CharField(primary_key=True, max_length=36)
    servertimestamp = models.DateTimeField(db_column='serverTimestamp', blank=True, null=True) # Field name made lowercase.
    timestamp = models.DateTimeField()
    deletedindicator = models.BooleanField(db_column='deletedIndicator') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'memberhandler_challengeweek'

class MemberhandlerChallengeweekactivity(models.Model):
    quantity = models.IntegerField(blank=True, null=True)
    units = models.IntegerField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    challengeweekoccurrence = models.ForeignKey('MemberhandlerChallengeweekoccurrence', db_column='challengeWeekOccurrence_id', blank=True, null=True) # Field name made lowercase.
    activity = models.ForeignKey(MemberhandlerActivity, blank=True, null=True)
    uuid = models.CharField(primary_key=True, max_length=36)
    servertimestamp = models.DateTimeField(db_column='serverTimestamp', blank=True, null=True) # Field name made lowercase.
    timestamp = models.DateTimeField()
    deletedindicator = models.BooleanField(db_column='deletedIndicator') # Field name made lowercase.
    challenge_uuid = models.CharField(max_length=36, blank=True)
    class Meta:
        managed = False
        db_table = 'memberhandler_challengeweekactivity'

class MemberhandlerChallengeweekoccurrence(models.Model):
    scheduledday = models.IntegerField(db_column='scheduledDay', blank=True, null=True) # Field name made lowercase.
    sequence = models.IntegerField(blank=True, null=True)
    spacing = models.IntegerField(blank=True, null=True)
    challengeweeksequence = models.ForeignKey('MemberhandlerChallengeweeksequence', db_column='challengeWeekSequence_id', blank=True, null=True) # Field name made lowercase.
    uuid = models.CharField(primary_key=True, max_length=36)
    servertimestamp = models.DateTimeField(db_column='serverTimestamp', blank=True, null=True) # Field name made lowercase.
    timestamp = models.DateTimeField()
    deletedindicator = models.BooleanField(db_column='deletedIndicator') # Field name made lowercase.
    challenge_uuid = models.CharField(max_length=36, blank=True)
    class Meta:
        managed = False
        db_table = 'memberhandler_challengeweekoccurrence'

class MemberhandlerChallengeweeksequence(models.Model):
    info = models.CharField(max_length=1024, blank=True)
    combinationtype = models.IntegerField(db_column='combinationType', blank=True, null=True) # Field name made lowercase.
    combinationheading = models.CharField(db_column='combinationHeading', max_length=128, blank=True) # Field name made lowercase.
    challengeweek = models.ForeignKey(MemberhandlerChallengeweek, db_column='challengeWeek_id', blank=True, null=True) # Field name made lowercase.
    uuid = models.CharField(primary_key=True, max_length=36)
    servertimestamp = models.DateTimeField(db_column='serverTimestamp', blank=True, null=True) # Field name made lowercase.
    timestamp = models.DateTimeField()
    deletedindicator = models.BooleanField(db_column='deletedIndicator') # Field name made lowercase.
    challenge_uuid = models.CharField(max_length=36, blank=True)
    class Meta:
        managed = False
        db_table = 'memberhandler_challengeweeksequence'

class MemberhandlerComment(models.Model):
    text = models.CharField(max_length=2048)
    uuid = models.CharField(primary_key=True, max_length=36)
    timestamp = models.DateTimeField()
    servertimestamp = models.DateTimeField(db_column='serverTimestamp', blank=True, null=True) # Field name made lowercase.
    deletedindicator = models.BooleanField(db_column='deletedIndicator') # Field name made lowercase.
    teammember = models.ForeignKey('MemberhandlerTeammember', db_column='teamMember_id', blank=True, null=True) # Field name made lowercase.
    post = models.ForeignKey('MemberhandlerPost', blank=True, null=True)
    team_uuid = models.CharField(max_length=36, blank=True)
    class Meta:
        managed = False
        db_table = 'memberhandler_comment'

class MemberhandlerDatabaseversion(models.Model):
    version = models.CharField(max_length=36)
    region = models.CharField(max_length=36)
    uuid = models.CharField(primary_key=True, max_length=36)
    timestamp = models.DateTimeField()
    servertimestamp = models.DateTimeField(db_column='serverTimestamp', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'memberhandler_databaseversion'

class MemberhandlerImage(models.Model):
    data = models.TextField()
    imagetype = models.IntegerField(db_column='imageType') # Field name made lowercase.
    uuid = models.CharField(primary_key=True, max_length=36)
    servertimestamp = models.DateTimeField(db_column='serverTimestamp', blank=True, null=True) # Field name made lowercase.
    timestamp = models.DateTimeField()
    deletedindicator = models.BooleanField(db_column='deletedIndicator') # Field name made lowercase.
    location = models.ForeignKey('MemberhandlerLocation', blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'memberhandler_image'

class MemberhandlerLike(models.Model):
    deletedindicator = models.BooleanField(db_column='deletedIndicator') # Field name made lowercase.
    uuid = models.CharField(primary_key=True, max_length=36)
    timestamp = models.DateTimeField()
    servertimestamp = models.DateTimeField(db_column='serverTimestamp', blank=True, null=True) # Field name made lowercase.
    post = models.ForeignKey('MemberhandlerPost', blank=True, null=True)
    teammember = models.ForeignKey('MemberhandlerTeammember', db_column='teamMember_id', blank=True, null=True) # Field name made lowercase.
    team_uuid = models.CharField(max_length=36, blank=True)
    comment = models.ForeignKey(MemberhandlerComment, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'memberhandler_like'

class MemberhandlerLocation(models.Model):
    latitude = models.CharField(max_length=256)
    longitude = models.CharField(max_length=256)
    uuid = models.CharField(primary_key=True, max_length=36)
    servertimestamp = models.DateTimeField(db_column='serverTimestamp', blank=True, null=True) # Field name made lowercase.
    timestamp = models.DateTimeField()
    deletedindicator = models.BooleanField(db_column='deletedIndicator') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'memberhandler_location'

class MemberhandlerMember(models.Model):
    emailaddress = models.CharField(db_column='emailAddress', max_length=256, blank=True) # Field name made lowercase.
    emailverified = models.BooleanField(db_column='emailVerified') # Field name made lowercase.
    group = models.CharField(max_length=256, blank=True)
    idnum = models.IntegerField()
    image_uuid = models.CharField(max_length=36, blank=True)
    location = models.CharField(max_length=256, blank=True)
    longtermgoal = models.CharField(db_column='longTermGoal', max_length=1024, blank=True) # Field name made lowercase.
    story = models.CharField(max_length=2048, blank=True)
    name = models.CharField(max_length=256)
    membertype = models.IntegerField(db_column='memberType') # Field name made lowercase.
    servertimestamp = models.DateTimeField(db_column='serverTimestamp', blank=True, null=True) # Field name made lowercase.
    timestamp = models.DateTimeField()
    uuid = models.CharField(primary_key=True, max_length=36)
    deletedindicator = models.BooleanField(db_column='deletedIndicator') # Field name made lowercase.
    pushtoken = models.CharField(db_column='pushToken', max_length=128, blank=True) # Field name made lowercase.
    pushfrequency = models.IntegerField(db_column='pushFrequency', blank=True, null=True) # Field name made lowercase.
    cardviews = models.IntegerField(db_column='cardViews', blank=True, null=True) # Field name made lowercase.
    deviceid = models.CharField(db_column='deviceId', max_length=36, blank=True) # Field name made lowercase.
    devicetoken = models.CharField(db_column='deviceToken', max_length=128, blank=True) # Field name made lowercase.
    devicesecret = models.CharField(db_column='deviceSecret', max_length=128, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'memberhandler_member'

class MemberhandlerMemberbadge(models.Model):
    earneddate = models.DateTimeField(db_column='earnedDate') # Field name made lowercase.
    uuid = models.CharField(primary_key=True, max_length=36)
    timestamp = models.DateTimeField()
    servertimestamp = models.DateTimeField(db_column='serverTimestamp', blank=True, null=True) # Field name made lowercase.
    deletedindicator = models.BooleanField(db_column='deletedIndicator') # Field name made lowercase.
    member = models.ForeignKey(MemberhandlerMember, related_name='member', blank=True, null=True)
    badge = models.ForeignKey(MemberhandlerBadge, related_name='badge', blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'memberhandler_memberbadge'

class MemberhandlerMemberchallengeweekactivity(models.Model):
    completed = models.IntegerField()
    completedday = models.IntegerField(db_column='completedDay') # Field name made lowercase.
    challengeweekactivity = models.ForeignKey(MemberhandlerChallengeweekactivity, db_column='challengeWeekActivity_id', blank=True, null=True) # Field name made lowercase.
    teammember = models.ForeignKey('MemberhandlerTeammember', db_column='teamMember_id', blank=True, null=True) # Field name made lowercase.
    team_uuid = models.CharField(max_length=36, blank=True)
    uuid = models.CharField(primary_key=True, max_length=36)
    servertimestamp = models.DateTimeField(db_column='serverTimestamp', blank=True, null=True) # Field name made lowercase.
    timestamp = models.DateTimeField()
    deletedindicator = models.BooleanField(db_column='deletedIndicator') # Field name made lowercase.
    specificactivity = models.ForeignKey(MemberhandlerActivity, db_column='specificActivity_id', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'memberhandler_memberchallengeweekactivity'

class MemberhandlerMemberchallengeweekoccurrence(models.Model):
    scheduledday = models.IntegerField(db_column='scheduledDay', blank=True, null=True) # Field name made lowercase.
    challengeweekoccurrence = models.ForeignKey(MemberhandlerChallengeweekoccurrence, db_column='challengeWeekOccurrence_id', blank=True, null=True) # Field name made lowercase.
    teammember = models.ForeignKey('MemberhandlerTeammember', db_column='teamMember_id', blank=True, null=True) # Field name made lowercase.
    team_uuid = models.CharField(max_length=36, blank=True)
    uuid = models.CharField(primary_key=True, max_length=36)
    servertimestamp = models.DateTimeField(db_column='serverTimestamp', blank=True, null=True) # Field name made lowercase.
    timestamp = models.DateTimeField()
    deletedindicator = models.BooleanField(db_column='deletedIndicator') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'memberhandler_memberchallengeweekoccurrence'

class MemberhandlerMemberspecificactivity(models.Model):
    selecteddate = models.DateTimeField(db_column='selectedDate') # Field name made lowercase.
    selectedday = models.IntegerField(db_column='selectedDay') # Field name made lowercase.
    team_uuid = models.CharField(max_length=36)
    uuid = models.CharField(primary_key=True, max_length=36)
    servertimestamp = models.DateTimeField(db_column='serverTimestamp', blank=True, null=True) # Field name made lowercase.
    timestamp = models.DateTimeField()
    deletedindicator = models.BooleanField(db_column='deletedIndicator') # Field name made lowercase.
    teammember = models.ForeignKey('MemberhandlerTeammember', db_column='teamMember_id', blank=True, null=True) # Field name made lowercase.
    challengeweek = models.ForeignKey(MemberhandlerChallengeweek, db_column='challengeWeek_id', blank=True, null=True) # Field name made lowercase.
    genericactivity = models.ForeignKey(MemberhandlerActivity, related_name='memberhandlermemberspecificactivity_genericactivity', db_column='genericActivity_id', blank=True, null=True) # Field name made lowercase.
    specificactivity = models.ForeignKey(MemberhandlerActivity, related_name='memberhandlermemberspecificactivity_specificactivity', db_column='specificActivity_id', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'memberhandler_memberspecificactivity'

class MemberhandlerP2Pconversation(models.Model):
    unreadmessages = models.BooleanField(db_column='unreadMessages') # Field name made lowercase.
    lastupdatetimestamp = models.DateTimeField(db_column='lastUpdateTimestamp', blank=True, null=True) # Field name made lowercase.
    uuid = models.CharField(primary_key=True, max_length=36)
    servertimestamp = models.DateTimeField(db_column='serverTimestamp', blank=True, null=True) # Field name made lowercase.
    timestamp = models.DateTimeField()
    deletedindicator = models.BooleanField(db_column='deletedIndicator') # Field name made lowercase.
    owner = models.ForeignKey(MemberhandlerMember, related_name='owner', blank=True, null=True)
    withmember = models.ForeignKey(MemberhandlerMember, related_name='withmember', db_column='withMember_id', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'memberhandler_p2pconversation'

class MemberhandlerP2Pmessage(models.Model):
    text = models.CharField(max_length=2048)
    uuid = models.CharField(primary_key=True, max_length=36)
    receivedtimestamp = models.DateTimeField(db_column='receivedTimestamp', blank=True, null=True) # Field name made lowercase.
    servertimestamp = models.DateTimeField(db_column='serverTimestamp', blank=True, null=True) # Field name made lowercase.
    timestamp = models.DateTimeField()
    deletedindicator = models.BooleanField(db_column='deletedIndicator') # Field name made lowercase.
    sender = models.ForeignKey(MemberhandlerMember, related_name='sender', blank=True, null=True)
    recipient = models.ForeignKey(MemberhandlerMember, related_name='recipient', blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'memberhandler_p2pmessage'

class MemberhandlerPost(models.Model):
    deletedindicator = models.BooleanField(db_column='deletedIndicator') # Field name made lowercase.
    text = models.CharField(max_length=1024, blank=True)
    servertimestamp = models.DateTimeField(db_column='serverTimestamp', blank=True, null=True) # Field name made lowercase.
    timestamp = models.DateTimeField()
    createtimestamp = models.DateTimeField(db_column='createTimestamp', blank=True, null=True) # Field name made lowercase.
    uuid = models.CharField(primary_key=True, max_length=36)
    teammember = models.ForeignKey('MemberhandlerTeammember', db_column='teamMember_id', blank=True, null=True) # Field name made lowercase.
    team = models.ForeignKey('MemberhandlerTeam', blank=True, null=True)
    image_uuid = models.CharField(max_length=36, blank=True)
    thumbnail_uuid = models.CharField(max_length=36, blank=True)
    location = models.ForeignKey(MemberhandlerLocation, blank=True, null=True)
    insetimage_uuid = models.CharField(db_column='insetImage_uuid', max_length=36, blank=True) # Field name made lowercase.
    imagewidth = models.FloatField(db_column='imageWidth', blank=True, null=True) # Field name made lowercase.
    imageheight = models.FloatField(db_column='imageHeight', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'memberhandler_post'

class MemberhandlerPostcard(models.Model):
    card = models.ForeignKey(MemberhandlerCard, blank=True, null=True)
    post = models.ForeignKey(MemberhandlerPost, blank=True, null=True)
    team_uuid = models.CharField(max_length=36, blank=True)
    uuid = models.CharField(primary_key=True, max_length=36)
    servertimestamp = models.DateTimeField(db_column='serverTimestamp', blank=True, null=True) # Field name made lowercase.
    timestamp = models.DateTimeField()
    deletedindicator = models.BooleanField(db_column='deletedIndicator') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'memberhandler_postcard'

class MemberhandlerServerinteractions(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.IntegerField()
    transactiontype = models.IntegerField(db_column='transactionType', blank=True, null=True) # Field name made lowercase.
    bytecount = models.IntegerField(db_column='byteCount', blank=True, null=True) # Field name made lowercase.
    delta = models.FloatField(blank=True, null=True)
    servertimestamp = models.DateTimeField(db_column='serverTimestamp', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'memberhandler_serverinteractions'

class MemberhandlerSpecificactivity(models.Model):
    seq = models.IntegerField()
    uuid = models.CharField(primary_key=True, max_length=36)
    servertimestamp = models.DateTimeField(db_column='serverTimestamp', blank=True, null=True) # Field name made lowercase.
    timestamp = models.DateTimeField()
    deletedindicator = models.BooleanField(db_column='deletedIndicator') # Field name made lowercase.
    genericactivity = models.ForeignKey(MemberhandlerActivity, related_name='genericactivity', db_column='genericActivity_id', blank=True, null=True) # Field name made lowercase.
    specificactivity = models.ForeignKey(MemberhandlerActivity, related_name='specificactivity', db_column='specificActivity_id', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'memberhandler_specificactivity'

class MemberhandlerTeam(models.Model):
    name = models.CharField(max_length=256)
    info = models.CharField(max_length=2048)
    image_uuid = models.CharField(max_length=36, blank=True)
    visibility = models.IntegerField()
    activitylevel = models.IntegerField(db_column='activityLevel', blank=True, null=True) # Field name made lowercase.
    createdate = models.DateTimeField(db_column='createDate') # Field name made lowercase.
    closedate = models.DateTimeField(db_column='closeDate', blank=True, null=True) # Field name made lowercase.
    timezone = models.IntegerField()
    timezonename = models.CharField(db_column='timeZoneName', max_length=256, blank=True) # Field name made lowercase.
    uuid = models.CharField(primary_key=True, max_length=36)
    servertimestamp = models.DateTimeField(db_column='serverTimestamp', blank=True, null=True) # Field name made lowercase.
    timestamp = models.DateTimeField()
    deletedindicator = models.BooleanField(db_column='deletedIndicator') # Field name made lowercase.
    code = models.CharField(max_length=36, blank=True)
    publicemail = models.CharField(db_column='publicEmail', max_length=256, blank=True) # Field name made lowercase.
    type = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'memberhandler_team'

class MemberhandlerTeambadge(models.Model):
    earneddate = models.DateTimeField(db_column='earnedDate') # Field name made lowercase.
    uuid = models.CharField(primary_key=True, max_length=36)
    servertimestamp = models.DateTimeField(db_column='serverTimestamp', blank=True, null=True) # Field name made lowercase.
    timestamp = models.DateTimeField()
    deletedindicator = models.BooleanField(db_column='deletedIndicator') # Field name made lowercase.
    team = models.ForeignKey(MemberhandlerTeam, blank=True, null=True)
    badge = models.ForeignKey(MemberhandlerBadge, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'memberhandler_teambadge'

class MemberhandlerTeamchallenge(models.Model):
    startdate = models.DateTimeField(db_column='startDate', blank=True, null=True) # Field name made lowercase.
    enddate = models.DateTimeField(db_column='endDate', blank=True, null=True) # Field name made lowercase.
    uuid = models.CharField(primary_key=True, max_length=36)
    timestamp = models.DateTimeField()
    servertimestamp = models.DateTimeField(db_column='serverTimestamp', blank=True, null=True) # Field name made lowercase.
    deletedindicator = models.BooleanField(db_column='deletedIndicator') # Field name made lowercase.
    challenge = models.ForeignKey(MemberhandlerChallenge, blank=True, null=True)
    team = models.ForeignKey(MemberhandlerTeam, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'memberhandler_teamchallenge'

class MemberhandlerTeamkeyword(models.Model):
    keyword = models.CharField(max_length=128)
    uuid = models.CharField(primary_key=True, max_length=36)
    servertimestamp = models.DateTimeField(db_column='serverTimestamp', blank=True, null=True) # Field name made lowercase.
    timestamp = models.DateTimeField()
    deletedindicator = models.BooleanField(db_column='deletedIndicator') # Field name made lowercase.
    team = models.ForeignKey(MemberhandlerTeam, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'memberhandler_teamkeyword'

class MemberhandlerTeammember(models.Model):
    name = models.CharField(max_length=256)
    membertype = models.IntegerField(db_column='memberType') # Field name made lowercase.
    joindate = models.DateTimeField(db_column='joinDate') # Field name made lowercase.
    leavedate = models.DateTimeField(db_column='leaveDate', blank=True, null=True) # Field name made lowercase.
    adminindicator = models.BooleanField(db_column='adminIndicator') # Field name made lowercase.
    uuid = models.CharField(primary_key=True, max_length=36)
    servertimestamp = models.DateTimeField(db_column='serverTimestamp', blank=True, null=True) # Field name made lowercase.
    timestamp = models.DateTimeField()
    deletedindicator = models.BooleanField(db_column='deletedIndicator') # Field name made lowercase.
    team = models.ForeignKey(MemberhandlerTeam, blank=True, null=True)
    image_uuid = models.CharField(max_length=36, blank=True)
    member_uuid = models.CharField(max_length=36, blank=True)
    class Meta:
        managed = False
        db_table = 'memberhandler_teammember'

class MemberhandlerTeammemberrecognizedactivity(models.Model):
    uuid = models.CharField(primary_key=True, max_length=36)
    teammember = models.ForeignKey(MemberhandlerTeammember, db_column='teamMember_id', blank=True, null=True) # Field name made lowercase.
    activity = models.ForeignKey(MemberhandlerActivity, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    memberchallengeweekactivity = models.CharField(db_column='memberChallengeWeekActivity', max_length=36, blank=True) # Field name made lowercase.
    servertimestamp = models.DateTimeField(db_column='serverTimestamp', blank=True, null=True) # Field name made lowercase.
    timestamp = models.DateTimeField()
    deletedindicator = models.BooleanField(db_column='deletedIndicator') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'memberhandler_teammemberrecognizedactivity'

class MemberhandlerTeampost(models.Model):
    uuid = models.CharField(primary_key=True, max_length=36)
    servertimestamp = models.DateTimeField(db_column='serverTimestamp', blank=True, null=True) # Field name made lowercase.
    timestamp = models.DateTimeField()
    deletedindicator = models.BooleanField(db_column='deletedIndicator') # Field name made lowercase.
    team = models.ForeignKey(MemberhandlerTeam, blank=True, null=True)
    post = models.ForeignKey(MemberhandlerPost, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'memberhandler_teampost'

class MemberhandlerTip(models.Model):
    text = models.CharField(max_length=2048)
    image_uuid = models.CharField(max_length=36, blank=True)
    thumbnail_uuid = models.CharField(max_length=36, blank=True)
    insetimage_uuid = models.CharField(db_column='insetImage_uuid', max_length=36, blank=True) # Field name made lowercase.
    challenge = models.ForeignKey(MemberhandlerChallenge, blank=True, null=True)
    day = models.IntegerField()
    uuid = models.CharField(primary_key=True, max_length=36)
    servertimestamp = models.DateTimeField(db_column='serverTimestamp', blank=True, null=True) # Field name made lowercase.
    imagewidth = models.FloatField(db_column='imageWidth') # Field name made lowercase.
    imageheight = models.FloatField(db_column='imageHeight') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'memberhandler_tip'

class MydjangoChoice(models.Model):
    id = models.IntegerField(primary_key=True)
    poll = models.ForeignKey('MydjangoPoll')
    choice = models.CharField(max_length=200)
    votes = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'mydjango_choice'

class MydjangoPoll(models.Model):
    id = models.IntegerField(primary_key=True)
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'mydjango_poll'

class RegistrationRegistrationprofile(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser, unique=True)
    activation_key = models.CharField(max_length=40)
    class Meta:
        managed = False
        db_table = 'registration_registrationprofile'

class SouthMigrationhistory(models.Model):
    id = models.IntegerField(primary_key=True)
    app_name = models.CharField(max_length=255)
    migration = models.CharField(max_length=255)
    applied = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'south_migrationhistory'

