#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mezzanine.conf import register_setting

register_setting(
    name="CONTACT_CAREERS_EMAIL_FROM",
    description="Email de contact pour postuler a un emploi",
    editable=True,
    default="rh@nomdelacompagnie.com",
    label="Email de contact - Postuler a un emploi"
)

register_setting(
name="TEMPLATE_ACCESSIBLE_SETTINGS",
description="Sequence of setting names available within templates.",
default=("CONTACT_CAREERS_EMAIL_FROM", ),
append=True,
editable=True,
)