from django.db import models

class Deployment(models.Model):
    '''Deployment information
    '''

    name = models.CharField(max_length=128, blank=False)

    location = models.CharField(max_length=50, blank=True)

    sensor_node_count = models.PositiveIntegerField(default=0)

    gateway_count = models.PositiveIntegerField(default=0)

    master_key_group = models.ForeignKey('Key', blank=False, null=False,
                                related_name='deployment_mkg')

    master_key_authentication = models.ForeignKey('Key', blank=False, null=False,
                                related_name='deployment_mka')

    master_key_encryption = models.ForeignKey('Key', blank=False, null=False,
                                related_name='deployment_mke')

    def __unicode__(self):
        return ', '.join([unicode(self.id), self.name])


class Node(models.Model):
    ''' node information
    '''
    SENSOR_NODE, GATEWAY_NODE, SNIFFER_NODE = range(3)
    NODES_CHOICES = (
            (SENSOR_NODE, 'Sensor'),
            (GATEWAY_NODE, 'Gateway'),
            (SNIFFER_NODE, 'Sniffer')
        )

    node_type = models.PositiveSmallIntegerField(
            default=SENSOR_NODE,
            choices=NODES_CHOICES
            )

    group_key = models.ForeignKey('Key', blank=False, null=False,
                                related_name='node_gk')

    authentication_key = models.ForeignKey('Key', blank=False, null=False,
                                related_name='node_ak')

    encryption_key = models.ForeignKey('Key', blank=False, null=False,
                                related_name='node_ek')

    ota_key = models.ForeignKey('Key', blank=False, null=False,
                                related_name='node_ok')

    registration_status = models.BooleanField(default=False)

    deployment = models.ForeignKey('Deployment', blank = False, null=False,
                                related_name='node')

    def __unicode__(self):
        return ', '.join([unicode(self.id), self.node_type, self.deployment.name])


class Key(models.Model):
    '''Keys information
    '''
    MASTER_KEY, AUTHENTICATION_KEY, ENCRYPTION_KEY, GROUP_KEY, OTA_KEY = range(5)
    KEY_CHOICES = (
            (MASTER_KEY, "Master Key"),
            (AUTHENTICATION_KEY, "Authentication Key"),
            (ENCRYPTION_KEY, "Encryption Key"),
            (GROUP_KEY, "Group Key"),
            (OTA_KEY, "OTA Key")
        )

    key_type = models.PositiveSmallIntegerField(
            default=MASTER_KEY,
            choices=KEY_CHOICES
        )
    key_value = models.CharField(max_length=32)

    def __unicode__(self):
        return ', '.join([unicode(self.id), self.key_type])


class AppConfig(models.Model):
    '''AppConfig information
    '''

    deployment = models.ForeignKey('Deployment', blank=False, null=False,
                        related_name='app_config')

    def __unicode__(self):
        return ', '.join([unicode(self.id)])


class SensorMap(models.Model):
    ''' Sensor mapping information
    '''

    modality_bit = models.PositiveSmallIntegerField()

    app_config = models.ForeignKey('AppConfig', blank=False, null=False,
                        related_name='sensor_map')

    sensor = models.ForeignKey('Sensor', blank=False, null=False,
                        related_name='sensor_map')

    def __unicode__(self):
        return ', '.join([unicode(self.id), self.modality_bit])


class Sensor(models.Model):
    ''' Sensor information
    '''

    modality = models.CharField(max_length=50)

    data_length = models.PositiveIntegerField()

    def __unicode__(self):
        return ', '.join([unicode(self.id), self.modality])
