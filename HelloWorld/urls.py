from django.conf.urls import url

from . import view, testdb, search, search2

from django.contrib import admin

urlpatterns = [
	url(r'^hello$', view.hello),
	url(r'^save', testdb.save),
	url(r'^update', testdb.update),
	url(r'^delete', testdb.delete),
	url(r'^look', testdb.look),
	url(r'^search_form', search.search_form),
	url(r'^search$', search.search),
	url(r'^search-post$', search2.search_post),
	url(r'^admin/', admin.site.urls),
]
