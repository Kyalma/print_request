from django.contrib.auth.models import User, Group
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver


@receiver(post_save, sender=User, weak=False)
def set_default_user_group(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='requester')
        instance.groups.add(group)
        print(f"default group added: {group}")
