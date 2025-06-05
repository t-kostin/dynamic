from constance.signals import config_updated
from django.utils.timezone import activate
from django.dispatch import receiver

@receiver(config_updated)
def update_timezone(sender, key, old_value, new_value, **kwargs):
    # print(f'{new_value = }')
    if key == 'TIME_ZONE':
        activate(new_value)
