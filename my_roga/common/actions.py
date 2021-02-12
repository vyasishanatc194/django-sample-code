from django.utils import timezone

class Actions(object):

    def __init__(self, model):
        self.model = model

    def create(self, **kwargs):
        obj = self.model.objects.create(**kwargs)
        return obj
    
    def update(self, id, **kwargs):
        if not id:
            return False
        obj = self.model.objects.filter(id=int(id)).update(**kwargs)
        update_obj = self.model.objects.filter(id=int(id)).first()
        if update_obj:
            update_obj.updated_at = timezone.now()
            update_obj.save()
            return update_obj
        return obj
    
    def delete(self, id):
        if not id:
            return False
        obj = self.model.objects.filter(id=int(id)).first()
        if obj:
            obj.delete()
            return True
        return False

    def soft_delete(self, id, reason=''):
        if not id:
            return False
        obj = self.model.objects.filter(id=int(id)).first()
        if obj:
            obj.active = False
            obj.is_deleted = True
            obj.deleted_at = timezone.now()
            obj.delete_reason = reason
            obj.save()
            return True
        return False
    
    def revive(self, id):
        obj = self.model.objects.filter(id=int(id)).first()
        if obj:
            obj.active = True
            obj.is_deleted = False
            obj.deleted_at = None
            obj.delete_reason = ''
            obj.save()
            return True
        return False
