from django.conf.urls import include, url
from django.core import urlresolvers
from django.utils.translation import ugettext_lazy as _

from wagtail.wagtailadmin import hooks
from wagtail.wagtailadmin.menu import MenuItem

from wagtail.wagtailsnippets import urls
from wagtail.wagtailsnippets.permissions import user_can_edit_snippets


def register_admin_urls():
    return [
        url(r'^snippets/', include(urls)),
    ]
hooks.register('register_admin_urls', register_admin_urls)


def construct_main_menu(request, menu_items):
    if user_can_edit_snippets(request.user):
        menu_items.append(
            MenuItem(_('Snippets'), urlresolvers.reverse('wagtailsnippets_index'), classnames='icon icon-snippet', order=500)
        )
hooks.register('construct_main_menu', construct_main_menu)
