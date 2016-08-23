from __future__ import absolute_import, unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

DEFAULTS = {
    'SUCCESS_MSG': _('Thank you, the form has been submitted.'),
    'ERROR_MSG': _('There was an error processing the form'),
}


def get_formblocks_setting(name):
    return getattr(settings, 'WAGTAIL_FORMBLOCKS_'.format(name), DEFAULTS[name])
