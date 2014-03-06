from django.contrib import admin
from .models import (
		Deployment,
		Node,
		Key,
		AppConfig,
		SensorMap,
		Sensor
		)
admin.site.register(Deployment)
admin.site.register(Node)
admin.site.register(Key)
admin.site.register(AppConfig)
admin.site.register(SensorMap)
admin.site.register(Sensor)