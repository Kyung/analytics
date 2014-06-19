# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        pass

    def backwards(self, orm):
        pass

    models = {
        u'Analytics.authgroup': {
            'Meta': {'object_name': 'AuthGroup', 'db_table': "u'auth_group'", 'managed': 'False'},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'})
        },
        u'Analytics.authgrouppermissions': {
            'Meta': {'object_name': 'AuthGroupPermissions', 'db_table': "u'auth_group_permissions'", 'managed': 'False'},
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Analytics.AuthGroup']"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'permission': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Analytics.AuthPermission']"})
        },
        u'Analytics.authpermission': {
            'Meta': {'object_name': 'AuthPermission', 'db_table': "u'auth_permission'", 'managed': 'False'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Analytics.DjangoContentType']"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'Analytics.authuser': {
            'Meta': {'object_name': 'AuthUser', 'db_table': "u'auth_user'", 'managed': 'False'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'Analytics.authusergroups': {
            'Meta': {'object_name': 'AuthUserGroups', 'db_table': "u'auth_user_groups'", 'managed': 'False'},
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Analytics.AuthGroup']"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Analytics.AuthUser']"})
        },
        u'Analytics.authuseruserpermissions': {
            'Meta': {'object_name': 'AuthUserUserPermissions', 'db_table': "u'auth_user_user_permissions'", 'managed': 'False'},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'permission': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Analytics.AuthPermission']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Analytics.AuthUser']"})
        },
        u'Analytics.djangoadminlog': {
            'Meta': {'object_name': 'DjangoAdminLog', 'db_table': "u'django_admin_log'", 'managed': 'False'},
            'action_flag': ('django.db.models.fields.SmallIntegerField', [], {}),
            'action_time': ('django.db.models.fields.DateTimeField', [], {}),
            'change_message': ('django.db.models.fields.TextField', [], {}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Analytics.DjangoContentType']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'object_repr': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Analytics.AuthUser']"})
        },
        u'Analytics.djangocontenttype': {
            'Meta': {'object_name': 'DjangoContentType', 'db_table': "u'django_content_type'", 'managed': 'False'},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'Analytics.djangosession': {
            'Meta': {'object_name': 'DjangoSession', 'db_table': "u'django_session'", 'managed': 'False'},
            'expire_date': ('django.db.models.fields.DateTimeField', [], {}),
            'session_data': ('django.db.models.fields.TextField', [], {}),
            'session_key': ('django.db.models.fields.CharField', [], {'max_length': '40', 'primary_key': 'True'})
        },
        u'Analytics.djangosite': {
            'Meta': {'object_name': 'DjangoSite', 'db_table': "u'django_site'", 'managed': 'False'},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'Analytics.memberhandleractivity': {
            'Meta': {'object_name': 'MemberhandlerActivity', 'db_table': "u'memberhandler_activity'", 'managed': 'False'},
            'category': ('django.db.models.fields.IntegerField', [], {}),
            'deletedindicator': ('django.db.models.fields.BooleanField', [], {'db_column': "u'deletedIndicator'"}),
            'genericindicator': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'db_column': "u'genericIndicator'", 'blank': 'True'}),
            'icon_uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'info': ('django.db.models.fields.CharField', [], {'max_length': '2048'}),
            'norepeatindicator': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'db_column': "u'noRepeatIndicator'", 'blank': 'True'}),
            'seq': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'servertimestamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'serverTimestamp'", 'blank': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'type': ('django.db.models.fields.IntegerField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'weeklyindicator': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'db_column': "u'weeklyIndicator'", 'blank': 'True'})
        },
        u'Analytics.memberhandleractivitycard': {
            'Meta': {'object_name': 'MemberhandlerActivitycard', 'db_table': "u'memberhandler_activitycard'", 'managed': 'False'},
            'activity': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Analytics.MemberhandlerActivity']", 'null': 'True', 'blank': 'True'}),
            'card': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Analytics.MemberhandlerCard']", 'null': 'True', 'blank': 'True'}),
            'deletedindicator': ('django.db.models.fields.BooleanField', [], {'db_column': "u'deletedIndicator'"}),
            'sequence': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'servertimestamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'serverTimestamp'", 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        u'Analytics.memberhandlerbadge': {
            'Meta': {'object_name': 'MemberhandlerBadge', 'db_table': "u'memberhandler_badge'", 'managed': 'False'},
            'card': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Analytics.MemberhandlerCard']", 'null': 'True', 'blank': 'True'}),
            'deletedindicator': ('django.db.models.fields.BooleanField', [], {'db_column': "u'deletedIndicator'"}),
            'image_uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'info': ('django.db.models.fields.CharField', [], {'max_length': '2048', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'servertimestamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'serverTimestamp'", 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        u'Analytics.memberhandlerbigbluetest': {
            'Meta': {'object_name': 'MemberhandlerBigbluetest', 'db_table': "u'memberhandler_bigbluetest'", 'managed': 'False'},
            'bgafter': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'bgbefore': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'challengeweekactivity': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Analytics.MemberhandlerChallengeweekactivity']", 'null': 'True', 'db_column': "u'challengeWeekActivity_id'", 'blank': 'True'}),
            'completiondate': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'completionDate'", 'blank': 'True'}),
            'deletedindicator': ('django.db.models.fields.BooleanField', [], {'db_column': "u'deletedIndicator'"}),
            'diabetes': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'exercise': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'hypo': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'insulin': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'intensity': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'meal': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'servertimestamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'serverTimestamp'", 'blank': 'True'}),
            'teammember': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Analytics.MemberhandlerTeammember']", 'null': 'True', 'db_column': "u'teamMember_id'", 'blank': 'True'}),
            'time': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'units': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        u'Analytics.memberhandlercard': {
            'Meta': {'object_name': 'MemberhandlerCard', 'db_table': "u'memberhandler_card'", 'managed': 'False'},
            'category': ('django.db.models.fields.IntegerField', [], {}),
            'deletedindicator': ('django.db.models.fields.BooleanField', [], {'db_column': "u'deletedIndicator'"}),
            'detail': ('django.db.models.fields.CharField', [], {'max_length': '10485760'}),
            'image_uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'ratingcount': ('django.db.models.fields.IntegerField', [], {'db_column': "u'ratingCount'"}),
            'ratingsum': ('django.db.models.fields.IntegerField', [], {'db_column': "u'ratingSum'"}),
            'servertimestamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'serverTimestamp'", 'blank': 'True'}),
            'summary': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'url_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        u'Analytics.memberhandlercardkeyword': {
            'Meta': {'object_name': 'MemberhandlerCardkeyword', 'db_table': "u'memberhandler_cardkeyword'", 'managed': 'False'},
            'card': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Analytics.MemberhandlerCard']", 'null': 'True', 'blank': 'True'}),
            'deletedindicator': ('django.db.models.fields.BooleanField', [], {'db_column': "u'deletedIndicator'"}),
            'keyword': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'servertimestamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'serverTimestamp'", 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        u'Analytics.memberhandlercardrating': {
            'Meta': {'object_name': 'MemberhandlerCardrating', 'db_table': "u'memberhandler_cardrating'", 'managed': 'False'},
            'card': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Analytics.MemberhandlerCard']", 'null': 'True', 'blank': 'True'}),
            'deletedindicator': ('django.db.models.fields.BooleanField', [], {'db_column': "u'deletedIndicator'"}),
            'member': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Analytics.MemberhandlerMember']", 'null': 'True', 'blank': 'True'}),
            'rating': ('django.db.models.fields.IntegerField', [], {}),
            'servertimestamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'serverTimestamp'", 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        u'Analytics.memberhandlerchallenge': {
            'Meta': {'object_name': 'MemberhandlerChallenge', 'db_table': "u'memberhandler_challenge'", 'managed': 'False'},
            'badge': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Analytics.MemberhandlerBadge']", 'null': 'True', 'blank': 'True'}),
            'deletedindicator': ('django.db.models.fields.BooleanField', [], {'db_column': "u'deletedIndicator'"}),
            'image_uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'info': ('django.db.models.fields.CharField', [], {'max_length': '2048', 'blank': 'True'}),
            'options': ('django.db.models.fields.IntegerField', [], {}),
            'reward': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'servertimestamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'serverTimestamp'", 'blank': 'True'}),
            'sku': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'sponsor': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'weeks': ('django.db.models.fields.IntegerField', [], {})
        },
        u'Analytics.memberhandlerchallengeweek': {
            'Meta': {'object_name': 'MemberhandlerChallengeweek', 'db_table': "u'memberhandler_challengeweek'", 'managed': 'False'},
            'challenge': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Analytics.MemberhandlerChallenge']", 'null': 'True', 'blank': 'True'}),
            'deletedindicator': ('django.db.models.fields.BooleanField', [], {'db_column': "u'deletedIndicator'"}),
            'sequence': ('django.db.models.fields.IntegerField', [], {}),
            'servertimestamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'serverTimestamp'", 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        u'Analytics.memberhandlerchallengeweekactivity': {
            'Meta': {'object_name': 'MemberhandlerChallengeweekactivity', 'db_table': "u'memberhandler_challengeweekactivity'", 'managed': 'False'},
            'activity': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Analytics.MemberhandlerActivity']", 'null': 'True', 'blank': 'True'}),
            'challenge_uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'challengeweekoccurrence': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Analytics.MemberhandlerChallengeweekoccurrence']", 'null': 'True', 'db_column': "u'challengeWeekOccurrence_id'", 'blank': 'True'}),
            'deletedindicator': ('django.db.models.fields.BooleanField', [], {'db_column': "u'deletedIndicator'"}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sequence': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'servertimestamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'serverTimestamp'", 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'units': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        u'Analytics.memberhandlerchallengeweekoccurrence': {
            'Meta': {'object_name': 'MemberhandlerChallengeweekoccurrence', 'db_table': "u'memberhandler_challengeweekoccurrence'", 'managed': 'False'},
            'challenge_uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'challengeweeksequence': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Analytics.MemberhandlerChallengeweeksequence']", 'null': 'True', 'db_column': "u'challengeWeekSequence_id'", 'blank': 'True'}),
            'deletedindicator': ('django.db.models.fields.BooleanField', [], {'db_column': "u'deletedIndicator'"}),
            'scheduledday': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'scheduledDay'", 'blank': 'True'}),
            'sequence': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'servertimestamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'serverTimestamp'", 'blank': 'True'}),
            'spacing': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        u'Analytics.memberhandlerchallengeweeksequence': {
            'Meta': {'object_name': 'MemberhandlerChallengeweeksequence', 'db_table': "u'memberhandler_challengeweeksequence'", 'managed': 'False'},
            'challenge_uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'challengeweek': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Analytics.MemberhandlerChallengeweek']", 'null': 'True', 'db_column': "u'challengeWeek_id'", 'blank': 'True'}),
            'combinationheading': ('django.db.models.fields.CharField', [], {'max_length': '128', 'db_column': "u'combinationHeading'", 'blank': 'True'}),
            'combinationtype': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'combinationType'", 'blank': 'True'}),
            'deletedindicator': ('django.db.models.fields.BooleanField', [], {'db_column': "u'deletedIndicator'"}),
            'info': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True'}),
            'servertimestamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'serverTimestamp'", 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        u'Analytics.memberhandlercomment': {
            'Meta': {'object_name': 'MemberhandlerComment', 'db_table': "u'memberhandler_comment'", 'managed': 'False'},
            'deletedindicator': ('django.db.models.fields.BooleanField', [], {'db_column': "u'deletedIndicator'"}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Analytics.MemberhandlerPost']", 'null': 'True', 'blank': 'True'}),
            'servertimestamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'serverTimestamp'", 'blank': 'True'}),
            'team_uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'teammember': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Analytics.MemberhandlerTeammember']", 'null': 'True', 'db_column': "u'teamMember_id'", 'blank': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '2048'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        u'Analytics.memberhandlerdatabaseversion': {
            'Meta': {'object_name': 'MemberhandlerDatabaseversion', 'db_table': "u'memberhandler_databaseversion'", 'managed': 'False'},
            'region': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'servertimestamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'serverTimestamp'", 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '36'})
        },
        u'Analytics.memberhandlerimage': {
            'Meta': {'object_name': 'MemberhandlerImage', 'db_table': "u'memberhandler_image'", 'managed': 'False'},
            'data': ('django.db.models.fields.TextField', [], {}),
            'deletedindicator': ('django.db.models.fields.BooleanField', [], {'db_column': "u'deletedIndicator'"}),
            'imagetype': ('django.db.models.fields.IntegerField', [], {'db_column': "u'imageType'"}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Analytics.MemberhandlerLocation']", 'null': 'True', 'blank': 'True'}),
            'servertimestamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'serverTimestamp'", 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        u'Analytics.memberhandlerlike': {
            'Meta': {'object_name': 'MemberhandlerLike', 'db_table': "u'memberhandler_like'", 'managed': 'False'},
            'comment': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Analytics.MemberhandlerComment']", 'null': 'True', 'blank': 'True'}),
            'deletedindicator': ('django.db.models.fields.BooleanField', [], {'db_column': "u'deletedIndicator'"}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Analytics.MemberhandlerPost']", 'null': 'True', 'blank': 'True'}),
            'servertimestamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'serverTimestamp'", 'blank': 'True'}),
            'team_uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'teammember': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Analytics.MemberhandlerTeammember']", 'null': 'True', 'db_column': "u'teamMember_id'", 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        u'Analytics.memberhandlerlocation': {
            'Meta': {'object_name': 'MemberhandlerLocation', 'db_table': "u'memberhandler_location'", 'managed': 'False'},
            'deletedindicator': ('django.db.models.fields.BooleanField', [], {'db_column': "u'deletedIndicator'"}),
            'latitude': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'longitude': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'servertimestamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'serverTimestamp'", 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        u'Analytics.memberhandlermember': {
            'Meta': {'object_name': 'MemberhandlerMember', 'db_table': "u'memberhandler_member'", 'managed': 'False'},
            'cardviews': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'cardViews'", 'blank': 'True'}),
            'deletedindicator': ('django.db.models.fields.BooleanField', [], {'db_column': "u'deletedIndicator'"}),
            'deviceid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'db_column': "u'deviceId'", 'blank': 'True'}),
            'devicesecret': ('django.db.models.fields.CharField', [], {'max_length': '128', 'db_column': "u'deviceSecret'", 'blank': 'True'}),
            'devicetoken': ('django.db.models.fields.CharField', [], {'max_length': '128', 'db_column': "u'deviceToken'", 'blank': 'True'}),
            'emailaddress': ('django.db.models.fields.CharField', [], {'max_length': '256', 'db_column': "u'emailAddress'", 'blank': 'True'}),
            'emailverified': ('django.db.models.fields.BooleanField', [], {'db_column': "u'emailVerified'"}),
            'group': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'idnum': ('django.db.models.fields.IntegerField', [], {}),
            'image_uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'longtermgoal': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'db_column': "u'longTermGoal'", 'blank': 'True'}),
            'membertype': ('django.db.models.fields.IntegerField', [], {'db_column': "u'memberType'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'pushfrequency': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'pushFrequency'", 'blank': 'True'}),
            'pushtoken': ('django.db.models.fields.CharField', [], {'max_length': '128', 'db_column': "u'pushToken'", 'blank': 'True'}),
            'servertimestamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'serverTimestamp'", 'blank': 'True'}),
            'story': ('django.db.models.fields.CharField', [], {'max_length': '2048', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        u'Analytics.memberhandlermemberbadge': {
            'Meta': {'object_name': 'MemberhandlerMemberbadge', 'db_table': "u'memberhandler_memberbadge'", 'managed': 'False'},
            'badge': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'badge'", 'null': 'True', 'to': u"orm['Analytics.MemberhandlerBadge']"}),
            'deletedindicator': ('django.db.models.fields.BooleanField', [], {'db_column': "u'deletedIndicator'"}),
            'earneddate': ('django.db.models.fields.DateTimeField', [], {'db_column': "u'earnedDate'"}),
            'member': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'member'", 'null': 'True', 'to': u"orm['Analytics.MemberhandlerMember']"}),
            'servertimestamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'serverTimestamp'", 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        u'Analytics.memberhandlermemberchallengeweekactivity': {
            'Meta': {'object_name': 'MemberhandlerMemberchallengeweekactivity', 'db_table': "u'memberhandler_memberchallengeweekactivity'", 'managed': 'False'},
            'challengeweekactivity': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Analytics.MemberhandlerChallengeweekactivity']", 'null': 'True', 'db_column': "u'challengeWeekActivity_id'", 'blank': 'True'}),
            'completed': ('django.db.models.fields.IntegerField', [], {}),
            'completedday': ('django.db.models.fields.IntegerField', [], {'db_column': "u'completedDay'"}),
            'deletedindicator': ('django.db.models.fields.BooleanField', [], {'db_column': "u'deletedIndicator'"}),
            'servertimestamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'serverTimestamp'", 'blank': 'True'}),
            'specificactivity': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Analytics.MemberhandlerActivity']", 'null': 'True', 'db_column': "u'specificActivity_id'", 'blank': 'True'}),
            'team_uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'teammember': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Analytics.MemberhandlerTeammember']", 'null': 'True', 'db_column': "u'teamMember_id'", 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        u'Analytics.memberhandlermemberchallengeweekoccurrence': {
            'Meta': {'object_name': 'MemberhandlerMemberchallengeweekoccurrence', 'db_table': "u'memberhandler_memberchallengeweekoccurrence'", 'managed': 'False'},
            'challengeweekoccurrence': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Analytics.MemberhandlerChallengeweekoccurrence']", 'null': 'True', 'db_column': "u'challengeWeekOccurrence_id'", 'blank': 'True'}),
            'deletedindicator': ('django.db.models.fields.BooleanField', [], {'db_column': "u'deletedIndicator'"}),
            'scheduledday': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'scheduledDay'", 'blank': 'True'}),
            'servertimestamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'serverTimestamp'", 'blank': 'True'}),
            'team_uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'teammember': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Analytics.MemberhandlerTeammember']", 'null': 'True', 'db_column': "u'teamMember_id'", 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        u'Analytics.memberhandlermemberspecificactivity': {
            'Meta': {'object_name': 'MemberhandlerMemberspecificactivity', 'db_table': "u'memberhandler_memberspecificactivity'", 'managed': 'False'},
            'challengeweek': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Analytics.MemberhandlerChallengeweek']", 'null': 'True', 'db_column': "u'challengeWeek_id'", 'blank': 'True'}),
            'deletedindicator': ('django.db.models.fields.BooleanField', [], {'db_column': "u'deletedIndicator'"}),
            'genericactivity': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'memberhandlermemberspecificactivity_genericactivity'", 'null': 'True', 'db_column': "u'genericActivity_id'", 'to': u"orm['Analytics.MemberhandlerActivity']"}),
            'selecteddate': ('django.db.models.fields.DateTimeField', [], {'db_column': "u'selectedDate'"}),
            'selectedday': ('django.db.models.fields.IntegerField', [], {'db_column': "u'selectedDay'"}),
            'servertimestamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'serverTimestamp'", 'blank': 'True'}),
            'specificactivity': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'memberhandlermemberspecificactivity_specificactivity'", 'null': 'True', 'db_column': "u'specificActivity_id'", 'to': u"orm['Analytics.MemberhandlerActivity']"}),
            'team_uuid': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'teammember': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Analytics.MemberhandlerTeammember']", 'null': 'True', 'db_column': "u'teamMember_id'", 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        u'Analytics.memberhandlerp2pconversation': {
            'Meta': {'object_name': 'MemberhandlerP2Pconversation', 'db_table': "u'memberhandler_p2pconversation'", 'managed': 'False'},
            'deletedindicator': ('django.db.models.fields.BooleanField', [], {'db_column': "u'deletedIndicator'"}),
            'lastupdatetimestamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'lastUpdateTimestamp'", 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'owner'", 'null': 'True', 'to': u"orm['Analytics.MemberhandlerMember']"}),
            'servertimestamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'serverTimestamp'", 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'unreadmessages': ('django.db.models.fields.BooleanField', [], {'db_column': "u'unreadMessages'"}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'withmember': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'withmember'", 'null': 'True', 'db_column': "u'withMember_id'", 'to': u"orm['Analytics.MemberhandlerMember']"})
        },
        u'Analytics.memberhandlerp2pmessage': {
            'Meta': {'object_name': 'MemberhandlerP2Pmessage', 'db_table': "u'memberhandler_p2pmessage'", 'managed': 'False'},
            'deletedindicator': ('django.db.models.fields.BooleanField', [], {'db_column': "u'deletedIndicator'"}),
            'receivedtimestamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'receivedTimestamp'", 'blank': 'True'}),
            'recipient': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'recipient'", 'null': 'True', 'to': u"orm['Analytics.MemberhandlerMember']"}),
            'sender': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'sender'", 'null': 'True', 'to': u"orm['Analytics.MemberhandlerMember']"}),
            'servertimestamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'serverTimestamp'", 'blank': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '2048'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        u'Analytics.memberhandlerpost': {
            'Meta': {'object_name': 'MemberhandlerPost', 'db_table': "u'memberhandler_post'", 'managed': 'False'},
            'createtimestamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'createTimestamp'", 'blank': 'True'}),
            'deletedindicator': ('django.db.models.fields.BooleanField', [], {'db_column': "u'deletedIndicator'"}),
            'image_uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'imageheight': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'imageHeight'", 'blank': 'True'}),
            'imagewidth': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'imageWidth'", 'blank': 'True'}),
            'insetimage_uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'db_column': "u'insetImage_uuid'", 'blank': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Analytics.MemberhandlerLocation']", 'null': 'True', 'blank': 'True'}),
            'servertimestamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'serverTimestamp'", 'blank': 'True'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Analytics.MemberhandlerTeam']", 'null': 'True', 'blank': 'True'}),
            'teammember': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Analytics.MemberhandlerTeammember']", 'null': 'True', 'db_column': "u'teamMember_id'", 'blank': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True'}),
            'thumbnail_uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        u'Analytics.memberhandlerpostcard': {
            'Meta': {'object_name': 'MemberhandlerPostcard', 'db_table': "u'memberhandler_postcard'", 'managed': 'False'},
            'card': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Analytics.MemberhandlerCard']", 'null': 'True', 'blank': 'True'}),
            'deletedindicator': ('django.db.models.fields.BooleanField', [], {'db_column': "u'deletedIndicator'"}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Analytics.MemberhandlerPost']", 'null': 'True', 'blank': 'True'}),
            'servertimestamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'serverTimestamp'", 'blank': 'True'}),
            'team_uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        u'Analytics.memberhandlerserverinteractions': {
            'Meta': {'object_name': 'MemberhandlerServerinteractions', 'db_table': "u'memberhandler_serverinteractions'", 'managed': 'False'},
            'bytecount': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'byteCount'", 'blank': 'True'}),
            'delta': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'servertimestamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'serverTimestamp'", 'blank': 'True'}),
            'transactiontype': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'transactionType'", 'blank': 'True'}),
            'user': ('django.db.models.fields.IntegerField', [], {})
        },
        u'Analytics.memberhandlerspecificactivity': {
            'Meta': {'object_name': 'MemberhandlerSpecificactivity', 'db_table': "u'memberhandler_specificactivity'", 'managed': 'False'},
            'deletedindicator': ('django.db.models.fields.BooleanField', [], {'db_column': "u'deletedIndicator'"}),
            'genericactivity': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'genericactivity'", 'null': 'True', 'db_column': "u'genericActivity_id'", 'to': u"orm['Analytics.MemberhandlerActivity']"}),
            'seq': ('django.db.models.fields.IntegerField', [], {}),
            'servertimestamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'serverTimestamp'", 'blank': 'True'}),
            'specificactivity': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'specificactivity'", 'null': 'True', 'db_column': "u'specificActivity_id'", 'to': u"orm['Analytics.MemberhandlerActivity']"}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        u'Analytics.memberhandlerteam': {
            'Meta': {'object_name': 'MemberhandlerTeam', 'db_table': "u'memberhandler_team'", 'managed': 'False'},
            'activitylevel': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'activityLevel'", 'blank': 'True'}),
            'closedate': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'closeDate'", 'blank': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'createdate': ('django.db.models.fields.DateTimeField', [], {'db_column': "u'createDate'"}),
            'deletedindicator': ('django.db.models.fields.BooleanField', [], {'db_column': "u'deletedIndicator'"}),
            'image_uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'info': ('django.db.models.fields.CharField', [], {'max_length': '2048'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'publicemail': ('django.db.models.fields.CharField', [], {'max_length': '256', 'db_column': "u'publicEmail'", 'blank': 'True'}),
            'servertimestamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'serverTimestamp'", 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'timezone': ('django.db.models.fields.IntegerField', [], {}),
            'timezonename': ('django.db.models.fields.CharField', [], {'max_length': '256', 'db_column': "u'timeZoneName'", 'blank': 'True'}),
            'type': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'visibility': ('django.db.models.fields.IntegerField', [], {})
        },
        u'Analytics.memberhandlerteambadge': {
            'Meta': {'object_name': 'MemberhandlerTeambadge', 'db_table': "u'memberhandler_teambadge'", 'managed': 'False'},
            'badge': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Analytics.MemberhandlerBadge']", 'null': 'True', 'blank': 'True'}),
            'deletedindicator': ('django.db.models.fields.BooleanField', [], {'db_column': "u'deletedIndicator'"}),
            'earneddate': ('django.db.models.fields.DateTimeField', [], {'db_column': "u'earnedDate'"}),
            'servertimestamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'serverTimestamp'", 'blank': 'True'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Analytics.MemberhandlerTeam']", 'null': 'True', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        u'Analytics.memberhandlerteamchallenge': {
            'Meta': {'object_name': 'MemberhandlerTeamchallenge', 'db_table': "u'memberhandler_teamchallenge'", 'managed': 'False'},
            'challenge': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Analytics.MemberhandlerChallenge']", 'null': 'True', 'blank': 'True'}),
            'deletedindicator': ('django.db.models.fields.BooleanField', [], {'db_column': "u'deletedIndicator'"}),
            'enddate': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'endDate'", 'blank': 'True'}),
            'servertimestamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'serverTimestamp'", 'blank': 'True'}),
            'startdate': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'startDate'", 'blank': 'True'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Analytics.MemberhandlerTeam']", 'null': 'True', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        u'Analytics.memberhandlerteamkeyword': {
            'Meta': {'object_name': 'MemberhandlerTeamkeyword', 'db_table': "u'memberhandler_teamkeyword'", 'managed': 'False'},
            'deletedindicator': ('django.db.models.fields.BooleanField', [], {'db_column': "u'deletedIndicator'"}),
            'keyword': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'servertimestamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'serverTimestamp'", 'blank': 'True'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Analytics.MemberhandlerTeam']", 'null': 'True', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        u'Analytics.memberhandlerteammember': {
            'Meta': {'object_name': 'MemberhandlerTeammember', 'db_table': "u'memberhandler_teammember'", 'managed': 'False'},
            'adminindicator': ('django.db.models.fields.BooleanField', [], {'db_column': "u'adminIndicator'"}),
            'deletedindicator': ('django.db.models.fields.BooleanField', [], {'db_column': "u'deletedIndicator'"}),
            'image_uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'joindate': ('django.db.models.fields.DateTimeField', [], {'db_column': "u'joinDate'"}),
            'leavedate': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'leaveDate'", 'blank': 'True'}),
            'member_uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'membertype': ('django.db.models.fields.IntegerField', [], {'db_column': "u'memberType'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'servertimestamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'serverTimestamp'", 'blank': 'True'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Analytics.MemberhandlerTeam']", 'null': 'True', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        u'Analytics.memberhandlerteammemberrecognizedactivity': {
            'Meta': {'object_name': 'MemberhandlerTeammemberrecognizedactivity', 'db_table': "u'memberhandler_teammemberrecognizedactivity'", 'managed': 'False'},
            'activity': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Analytics.MemberhandlerActivity']", 'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'deletedindicator': ('django.db.models.fields.BooleanField', [], {'db_column': "u'deletedIndicator'"}),
            'duration': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'memberchallengeweekactivity': ('django.db.models.fields.CharField', [], {'max_length': '36', 'db_column': "u'memberChallengeWeekActivity'", 'blank': 'True'}),
            'servertimestamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'serverTimestamp'", 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'teammember': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Analytics.MemberhandlerTeammember']", 'null': 'True', 'db_column': "u'teamMember_id'", 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        u'Analytics.memberhandlerteampost': {
            'Meta': {'object_name': 'MemberhandlerTeampost', 'db_table': "u'memberhandler_teampost'", 'managed': 'False'},
            'deletedindicator': ('django.db.models.fields.BooleanField', [], {'db_column': "u'deletedIndicator'"}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Analytics.MemberhandlerPost']", 'null': 'True', 'blank': 'True'}),
            'servertimestamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'serverTimestamp'", 'blank': 'True'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Analytics.MemberhandlerTeam']", 'null': 'True', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        u'Analytics.memberhandlertip': {
            'Meta': {'object_name': 'MemberhandlerTip', 'db_table': "u'memberhandler_tip'", 'managed': 'False'},
            'challenge': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Analytics.MemberhandlerChallenge']", 'null': 'True', 'blank': 'True'}),
            'day': ('django.db.models.fields.IntegerField', [], {}),
            'image_uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'imageheight': ('django.db.models.fields.FloatField', [], {'db_column': "u'imageHeight'"}),
            'imagewidth': ('django.db.models.fields.FloatField', [], {'db_column': "u'imageWidth'"}),
            'insetimage_uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'db_column': "u'insetImage_uuid'", 'blank': 'True'}),
            'servertimestamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'serverTimestamp'", 'blank': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '2048'}),
            'thumbnail_uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        u'Analytics.mydjangochoice': {
            'Meta': {'object_name': 'MydjangoChoice', 'db_table': "u'mydjango_choice'", 'managed': 'False'},
            'choice': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'poll': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Analytics.MydjangoPoll']"}),
            'votes': ('django.db.models.fields.IntegerField', [], {})
        },
        u'Analytics.mydjangopoll': {
            'Meta': {'object_name': 'MydjangoPoll', 'db_table': "u'mydjango_poll'", 'managed': 'False'},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'Analytics.registrationregistrationprofile': {
            'Meta': {'object_name': 'RegistrationRegistrationprofile', 'db_table': "u'registration_registrationprofile'", 'managed': 'False'},
            'activation_key': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Analytics.AuthUser']", 'unique': 'True'})
        },
        u'Analytics.southmigrationhistory': {
            'Meta': {'object_name': 'SouthMigrationhistory', 'db_table': "u'south_migrationhistory'", 'managed': 'False'},
            'app_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'applied': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'migration': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['Analytics']