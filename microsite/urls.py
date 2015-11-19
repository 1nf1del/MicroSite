from django.conf.urls import patterns, include, url
from django.conf import settings


urlpatterns = patterns(
    '',

    url(r'^$', 'microsite_front.views.index'),
    url(r'^tools/$', 'microsite_front.views.tools', name='tools'),
    url(r'^tools/url-checker/$', 'microsite_front.views.url_checker_tool',
                                                name='url_checker_tool'),
    url(r'^tools/set-meta-data-for-S3-objects/$', 'microsite_front.views.s3_objects_set_metadata',
                                                name='s3_objects_set_metadata'),
    url(r'^report/$', 'micro_blog.views.report'),
    url(r'^contact/$', 'micro_blog.views.contact'),
    url(r'^careers/$', 'microsite_front.views.career_page'),
    url(r'^portal/', include('micro_admin.urls', namespace='micro_admin')),
    url(r'^blog/', include('micro_blog.urls', namespace='micro_blog')),
    url(r'^portal/content/', include('pages.urls', namespace='pages')),
    url(r'^portal/employee/', include('employee.urls', namespace='employee')),
    url(r'^books/', include('books.urls', namespace='books')),
    url(r'^sitemap/$', 'microsite_front.views.html_sitemap'),
    url(r'^(?P<slug>[-\w]+)/$', 'pages.views.site_page'),
    url(r'^rss.xml$', 'microsite_front.xml.rss'),
    url(r'^blog.rss$', 'microsite_front.xml.blog_rss'),
    url(r'^sitemap.xml$', 'microsite_front.xml.sitemap'),
    url(r'^search/autocomplete/$', 'search.views.autocomplete'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^404$', 'micro_blog.views.handler404'),
        url(r'^500$', 'micro_blog.views.handler500'),
    )
