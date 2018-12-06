from django.urls import path
from .views import ChoiceList
#from .views import QuestionViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
urlpatterns = [
path("polls/<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
#path("polls/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="create_vote"),
]
#

#router.register('', QuestionViewSet, base_name='questions')
urlpatterns = router.urls
