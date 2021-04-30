from django.db.models.signals import pre_save, post_save,m2m_changed
from django.dispatch import receiver
from addEmp.models import Developer

# projectRating=0
# blogRating=0
# qaRating=0
@receiver(m2m_changed, sender=Developer.project.through)
def pre_save_developer(sender, instance, **kwargs):
    # print(".......................................",instance)
    projectRating=0
    for project in instance.project.all():
        projectRating +=project.rating
    instance.temp1=projectRating
    # print(instance.temp1)

@receiver(m2m_changed, sender=Developer.blog.through)
def pre_save_developer(sender, instance, **kwargs):
    print("signal")
    blogRating=0
    for blog in instance.blog.all():
        blogRating += blog.rating
    instance.temp2=blogRating
@receiver(m2m_changed, sender=Developer.blog.through)
def pre_save_developer(sender, instance, **kwargs):
    print("signal")
    qaRating=0
    for q in instance.q_a.all():
        qaRating += q.rating
    instance.temp3=qaRating

@receiver(pre_save,sender=Developer)
def pre_save_developer(sender, instance, **kwargs):
    score = 0
    pr=instance.temp1
    # score=instance.temp1+instance.temp2+instance.temp2
    instance.score = pr
    print(instance.score)
    # score = projectRating+blogRating+qaRating

# @receiver(m2m_changed, sender=Developer)
# def pre_save_developer(sender, instance, **kwargs):
#     score = 0
#     print("signal")
#     for project in instance.project.all():
#         projectRating =project.rating
#     for blog in instance.blog.all():
#         blogRating = blog.rating
#     for q in instance.q_a.all():
#         qaRating = q.rating

#     score = projectRating+blogRating+qaRating
#     instance.score = score