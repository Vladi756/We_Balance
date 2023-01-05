from rest_framework import serializers
from .models import Preferences, WorkDone, Flagged

class WorkDoneSerializer(serializers.ModelSerializer):

	class Meta:
		model = WorkDone
		fields = ('id','user', 'date','emails','calls', 'hours', 'meetings', 'breaks')

class PreferencesSerializer(serializers.ModelSerializer):

	class Meta:
		model = Preferences
		fields = ('id','user','emails','calls', 'hours', 'meetings', 'breaks')

class FlaggedSerializer(serializers.ModelSerializer):

	class Meta:
		model = Flagged
		fields = ('id','user','date_flagged','flag', 'preference', 'work_done', 'action_taken')
