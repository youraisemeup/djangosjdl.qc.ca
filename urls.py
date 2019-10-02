from __future__ import unicode_literals

from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from sjdl.common import views
from django.views.generic import RedirectView, TemplateView
from mezzanine.core.views import direct_to_template


admin.autodiscover()

# Add the urlpatterns for any custom Django applications here.
# You can also change the ``home`` view to add your own functionality
# to the project's homepage.

urlpatterns = i18n_patterns("",
    # Change the admin prefix here to use an alternate URL for the
    # admin interface, which would be marginally more secure.

)

urlpatterns += patterns('sjdl.usefullinks.views',
    url(r'agrotourisme/(?P<category>producteurs)/$', 'Agrotourisme',name='organismes'),
    url(r'agrotourisme/(?P<category>producteurs)/(?P<slug>.*)/$', 'fiche',name='organismes'),
    url(r'(?P<category>organismes-sportifs-et-de-plein-air)/', 'OrganismesSportifs', name='organismes'),
    url(r'(?P<category>organismes)/', 'Organismes', name='organismes'),
)

urlpatterns += patterns('',

    # We don't want to presume how your homepage works, so here are a
    # few patterns you can use to set it up.

    # HOMEPAGE AS STATIC TEMPLATE
    # ---------------------------
    # This pattern simply loads the default.html template. It isn't
    # commented out like the others, so it's the default. You only need
    # one homepage pattern, so if you use a different one, comment this
    # one out.

    # url("^$", direct_to_template, {"template": "homepage.html"}, name="home"),
    url(r'^robots\.txt$', direct_to_template, {'template': 'robots.txt', 'mimetype': 'text/plain'}),

    url(r'^$', 'sjdl.common.views.home', name="home"),
    url(r"^plan-du-site", 'sjdl.common.views.sitemap', name="sitemap"),
    # url(r"^elections", 'sjdl.common.views.pg_elections', name="elections"),

    url(r'formulaire-de-commande/$', 'sjdl.common.views.coffretform', name='coffret'),
    url(r'formulaire-de-commande/imprimer/$', 'sjdl.common.views.coffretformprint', name='coffret'),

    url(r'^nouvelles/', include('sjdl.news.urls', namespace='news')),
    url(r'^chantiers-en-cours/', include('sjdl.infotravaux.urls', namespace='infotravaux')),
    url(r'^evenements/', include('sjdl.events.urls', namespace='events')),
    url(r'emplois/', include('sjdl.careers.urls', namespace='careers')),

    url(r'vie-democratique/conseil-municipal/seance.*/(?P<year>\d{4})/$', 'sjdl.documentation.views.seancesConseilMunicipal', name="documentation"),
    url(r'vie-democratique/conseil-municipal/seance.*/$', 'sjdl.documentation.views.seancesConseilMunicipal', name="documentation"),
    # l(r'vie-democratique/conseil-municipal/seance.*/$', RedirectView.as_view(url=r'/2015/$')),
    url(r'vie-democratique/conseil-municipal/$', 'sjdl.documentation.views.conseilMunicipal',name='documentation'),

    url(r'^services-en-ligne/reglements-municipaux','sjdl.documentation.views.reglementsMunicipaux',name='regmunicipaux'),

    url(r'traitement-des-eaux-usees.*/seance.*/(?P<year>\d{4})/$', 'sjdl.documentation.views.archivesPV_RT', name="documentation"),
    url(r'assainissement-des-eaux-usees.*/seance.*/(?P<year>\d{4})/$', 'sjdl.documentation.views.archivesPV_RA', name="documentation"),
    url(r'traitement-des-eaux-usees.*/$', 'sjdl.documentation.views.ProcesVerbauxRegieTraitementSeances',name='documentation'),
    url(r'assainissement-des-eaux-usees.*/$', 'sjdl.documentation.views.ProcesVerbauxRegieAssainissementSeances',name='documentation'),
    url(r'avis-publics/$', 'sjdl.documentation.views.avispublics',name="documentation"),
    url(r'avis-publics/(?P<year>\d{4})/$', 'sjdl.documentation.views.avispublics',name="documentation"),

    url(r'^publications/$', 'sjdl.documentation.views.publications', name='documentation'),
    url(r'^publications/(?P<year>\d{4})/$', 'sjdl.documentation.views.publications', name='documentation'),

    url(r'^faq/','sjdl.faq.views.listing',name='faq'),

    url(r'^elections/$', TemplateView.as_view(template_name='elections/elections.html'), name="elections"),
    url(r'^elections-candidature/$', TemplateView.as_view(template_name='elections/elections-candidature.html'), name="elections"),
    url(r'^elections-candidatures/$', TemplateView.as_view(template_name='elections/elections-candidatures.html'), name="elections"),
    url(r'^elections-informations/$', TemplateView.as_view(template_name='elections/elections-informations.html'), name="elections"),
    url(r'^elections-resultats/$', TemplateView.as_view(template_name='elections/elections-resultats.html'), name="elections"),
    url(r'^infolettre/',include('sjdl.cyberimpact.urls',namespace='cyberimpact')),

    url(r'recherche-bac/$','sjdl.searchbac.views.search',name='searchbac'),

    url('^', include("sjdl.animaux.urls", namespace="animaux")),

    # manual redirects for empty pages. beurk.
    (r'^decouvrir-saint-joseph-du-lac/$',
     RedirectView.as_view(url='/decouvrir-saint-joseph-du-lac/presentation-generale/histoire-et-origine/')),
    (r'^decouvrir-saint-joseph-du-lac/presentation-generale/$',
     RedirectView.as_view(url='/decouvrir-saint-joseph-du-lac/presentation-generale/histoire-et-origine/')),

    (r'^services-municipaux/$', RedirectView.as_view(url='/services-municipaux/direction-generale/')),
    (r'^services-municipaux/finances/$', RedirectView.as_view(url='/services-municipaux/finances/mission/')),
    (r'^services-en-ligne/$', RedirectView.as_view(url='/services-en-ligne/emplois/')),
    (r'^loisirs-et-culture/$', RedirectView.as_view(url='/loisirs-et-culture/mission-du-service-des-loisirs/')),
    (r'^agrotourisme/$', RedirectView.as_view(url='/agrotourisme/saint-joseph-du-lac-le-pays-de-la-pomme/')),

    url("^cyber/recherche_bacs_list/$",'sjdl.searchbac.admin_views.recherche_bacs_list'),
    ("^cyber/", include(admin.site.urls)),


    # HOMEPAGE AS AN EDITABLE PAGE IN THE PAGE TREE
    # ---------------------------------------------
    # This pattern gives us a normal ``Page`` object, so that your
    # homepage can be managed via the page tree in the admin. If you
    # use this pattern, you'll need to create a page in the page tree,
    # and specify its URL (in the Meta Data section) as "/", which
    # is the value used below in the ``{"slug": "/"}`` part.
    # Also note that the normal rule of adding a custom
    # template per page with the template name using the page's slug
    # doesn't apply here, since we can't have a template called
    # "/.html" - so for this case, the template "pages/default.html"
    # should be used if you want to customize the homepage's template.

    # url("^$", "mezzanine.pages.views.page", {"slug": "/"}, name="home"),

    # HOMEPAGE FOR A BLOG-ONLY SITE
    # -----------------------------
    # This pattern points the homepage to the blog post listing page,
    # and is useful for sites that are primarily blogs. If you use this
    # pattern, you'll also need to set BLOG_SLUG = "" in your
    # ``settings.py`` module, and delete the blog page object from the
    # page tree in the admin if it was installed.

    # url("^$", "mezzanine.blog.views.blog_post_list", name="home"),

    # MEZZANINE'S URLS
    # ----------------
    # ADD YOUR OWN URLPATTERNS *ABOVE* THE LINE BELOW.
    # ``mezzanine.urls`` INCLUDES A *CATCH ALL* PATTERN
    # FOR PAGES, SO URLPATTERNS ADDED BELOW ``mezzanine.urls``
    # WILL NEVER BE MATCHED!

    # If you'd like more granular control over the patterns in
    # ``mezzanine.urls``, go right ahead and take the parts you want
    # from it, and use them directly below instead of using
    # ``mezzanine.urls``.
    ("^", include("mezzanine.urls")),

    # MOUNTING MEZZANINE UNDER A PREFIX
    # ---------------------------------
    # You can also mount all of Mezzanine's urlpatterns under a
    # URL prefix if desired. When doing this, you need to define the
    # ``SITE_PREFIX`` setting, which will contain the prefix. Eg:
    # SITE_PREFIX = "my/site/prefix"
    # For convenience, and to avoid repeating the prefix, use the
    # commented out pattern below (commenting out the one above of course)
    # which will make use of the ``SITE_PREFIX`` setting. Make sure to
    # add the import ``from django.conf import settings`` to the top
    # of this file as well.
    # Note that for any of the various homepage patterns above, you'll
    # need to use the ``SITE_PREFIX`` setting as well.

    # ("^%s/" % settings.SITE_PREFIX, include("mezzanine.urls"))

)


# Adds ``STATIC_URL`` to the context of error pages, so that error
# pages can use JS, CSS and images.
handler404 = "mezzanine.core.views.page_not_found"
handler500 = "mezzanine.core.views.server_error"
