from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from micro_blog.views import contact, subscribe
import microsite_front
from pages.views import site_page, set_country
from microsite_front.xml import rss, blog_rss, sitemap, facebook_rss
from microsite_front.views import index, tools, url_checker_tool, s3_objects_set_metadata, html_sitemap, books, oss
from search.views import autocomplete
from django.views.static import serve
from .country_urls import country_patterns
from django.utils.translation import ugettext_lazy as _
from solid_i18n.urls import solid_i18n_patterns

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'_static/(?P<path>.*)$', serve, {'document_root': settings.BASE_DIR + '/books/templates/html/_static/'}),
    url(r'_sources/(?P<path>.*)$', serve, {'document_root': settings.BASE_DIR + '/books/templates/html/_sources/'}),
    url(_(r'^$'), index),
    url(r'^books/(?P<path>.*)$', books),
    url(r'^tools/$', tools, name='tools'),
    url(r'^tools/url-checker/$', url_checker_tool, name='url_checker_tool'),
    url(r'^tools/set-meta-data-for-S3-objects/$', s3_objects_set_metadata, name='s3_objects_set_metadata'),
    url(r'^contact-india/$', contact, name="contact_india"),
    url(r'^contact-usa/$', contact, name="contact_usa"),
    url(r'^subscribe/$', subscribe),
    url(r'^open-source-softwares/$', oss),
    url(r'^set_country/$', set_country, name="set_country"),

    # url(r'^forum/', include('django_simple_forum.urls', namespace="django_simple_forum")),

    url(r'^portal/', include('micro_admin.urls', namespace='micro_admin')),
    url(_(r'^blog/'), include('micro_blog.urls', namespace='micro_blog')),
    url(r'^portal/content/', include('pages.urls', namespace='pages')),
    url(r'^sitemap/$', html_sitemap),
    url(r'^facebook.rss$', facebook_rss),
    url(r'^rss.xml$', rss),
    url(r'^blog.rss$', blog_rss),
    url(r'^sitemap.xml$', sitemap),
    url(r'^search/autocomplete/$', autocomplete),
    url(r'^(?P<slug>[-\w]+)/$', site_page),

]

urlpatterns += country_patterns(
    # url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^(?P<slug>[-\w]+)/$', site_page),
)


handler404 = microsite_front.views.handler404
handler500 = microsite_front.views.handler500

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]

if settings.DEBUG is False:   # if DEBUG is True it will be served automatically
    urlpatterns += [
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    ]

if settings.DEBUG:
    from django.views.static import serve
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
