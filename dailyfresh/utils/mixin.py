from django.contrib.auth.decorators import login_required

# 验证用户是否登入
class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls,**initkwargs):
        # 调用父类的as_view
        view = super(LoginRequiredMixin,cls).as_view(**initkwargs)
        return login_required(view)

