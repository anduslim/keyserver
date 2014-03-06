# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Deployment'
        db.create_table('actors_deployment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('sensor_node_count', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('gateway_count', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('master_key_group', self.gf('django.db.models.fields.related.ForeignKey')(related_name='deployment_mkg', to=orm['actors.Key'])),
            ('master_key_authentication', self.gf('django.db.models.fields.related.ForeignKey')(related_name='deployment_mka', to=orm['actors.Key'])),
            ('master_key_encryption', self.gf('django.db.models.fields.related.ForeignKey')(related_name='deployment_mke', to=orm['actors.Key'])),
        ))
        db.send_create_signal('actors', ['Deployment'])

        # Adding model 'Node'
        db.create_table('actors_node', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('node_type', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('group_key', self.gf('django.db.models.fields.related.ForeignKey')(related_name='node_gk', to=orm['actors.Key'])),
            ('authentication_key', self.gf('django.db.models.fields.related.ForeignKey')(related_name='node_ak', to=orm['actors.Key'])),
            ('encryption_key', self.gf('django.db.models.fields.related.ForeignKey')(related_name='node_ek', to=orm['actors.Key'])),
            ('ota_key', self.gf('django.db.models.fields.related.ForeignKey')(related_name='node_ok', to=orm['actors.Key'])),
            ('registration_status', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('deployment', self.gf('django.db.models.fields.related.ForeignKey')(related_name='node', to=orm['actors.Deployment'])),
        ))
        db.send_create_signal('actors', ['Node'])

        # Adding model 'Key'
        db.create_table('actors_key', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('key_type', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('key_value', self.gf('django.db.models.fields.CharField')(max_length=32)),
        ))
        db.send_create_signal('actors', ['Key'])

        # Adding model 'AppConfig'
        db.create_table('actors_appconfig', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('deployment', self.gf('django.db.models.fields.related.ForeignKey')(related_name='app_config', to=orm['actors.Deployment'])),
        ))
        db.send_create_signal('actors', ['AppConfig'])

        # Adding model 'SensorMap'
        db.create_table('actors_sensormap', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('modality_bit', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('app_config', self.gf('django.db.models.fields.related.ForeignKey')(related_name='sensor_map', to=orm['actors.AppConfig'])),
            ('sensor', self.gf('django.db.models.fields.related.ForeignKey')(related_name='sensor_map', to=orm['actors.Sensor'])),
        ))
        db.send_create_signal('actors', ['SensorMap'])

        # Adding model 'Sensor'
        db.create_table('actors_sensor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('modality', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('data_length', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal('actors', ['Sensor'])


    def backwards(self, orm):
        # Deleting model 'Deployment'
        db.delete_table('actors_deployment')

        # Deleting model 'Node'
        db.delete_table('actors_node')

        # Deleting model 'Key'
        db.delete_table('actors_key')

        # Deleting model 'AppConfig'
        db.delete_table('actors_appconfig')

        # Deleting model 'SensorMap'
        db.delete_table('actors_sensormap')

        # Deleting model 'Sensor'
        db.delete_table('actors_sensor')


    models = {
        'actors.appconfig': {
            'Meta': {'object_name': 'AppConfig'},
            'deployment': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'app_config'", 'to': "orm['actors.Deployment']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'actors.deployment': {
            'Meta': {'object_name': 'Deployment'},
            'gateway_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'master_key_authentication': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'deployment_mka'", 'to': "orm['actors.Key']"}),
            'master_key_encryption': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'deployment_mke'", 'to': "orm['actors.Key']"}),
            'master_key_group': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'deployment_mkg'", 'to': "orm['actors.Key']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'sensor_node_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        'actors.key': {
            'Meta': {'object_name': 'Key'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key_type': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'key_value': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        'actors.node': {
            'Meta': {'object_name': 'Node'},
            'authentication_key': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'node_ak'", 'to': "orm['actors.Key']"}),
            'deployment': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'node'", 'to': "orm['actors.Deployment']"}),
            'encryption_key': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'node_ek'", 'to': "orm['actors.Key']"}),
            'group_key': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'node_gk'", 'to': "orm['actors.Key']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'node_type': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'ota_key': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'node_ok'", 'to': "orm['actors.Key']"}),
            'registration_status': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'actors.sensor': {
            'Meta': {'object_name': 'Sensor'},
            'data_length': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modality': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'actors.sensormap': {
            'Meta': {'object_name': 'SensorMap'},
            'app_config': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sensor_map'", 'to': "orm['actors.AppConfig']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modality_bit': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'sensor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sensor_map'", 'to': "orm['actors.Sensor']"})
        }
    }

    complete_apps = ['actors']