from django.urls import path
from . feeds import LatestPostedFeed
from . import views

app_name = 'blog'

urlpatterns = [
	# post views
	path('', views.post_list, name="post_list"),
	path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
	#path('', views.PostListView.as_view(), name='post_list'),
	path('<int:year>/<int:month>/<int:day>/<slug:post>/',
		  views.post_detail,
		  name='post_detail'),
	path('<int:post_id>/', views.post_share, name="post_share"),
	# Feed URL
	path('feed/', LatestPostedFeed(), name="post_feed"),
	# Search URL
	path('search/', views.post_search, name='post_search'),

]