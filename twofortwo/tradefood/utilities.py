from django.utils.timezone import now, timedelta

def is_alive(obj):
  time_now = now()
  return obj.date_posted + timedelta(obj.duration) > time_now