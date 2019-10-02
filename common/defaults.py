from mezzanine.conf import register_setting

#contact infos
register_setting(
    name="CONTACT_EMAIL_FROM",
    description="Email de contact",
    editable=True,
    default="contact@nomdelacompagnie.com",
    label="Email de contact - General"
)

register_setting(
    name="CONTACT_EMAIL_TO",
    description="",
    editable=False,
    default="Site Web de Nom de la compagnie"
)

#social medias urls
register_setting(
    name="SITE_SOCIAL_MEDIA_FACEBOOK",
    description="Lien Page Facebook",
    editable=True,
    default="",
    label="Lien Page Facebook"
)
register_setting(
    name="SITE_SOCIAL_MEDIA_TWITTER",
    description="Lien Fil Twitter",
    editable=True,
    default="",
    label="Lien Fil Twitter"
)
register_setting(
    name="SITE_SOCIAL_MEDIA_INSTAGRAM",
    description="Lien Compte Instagram",
    editable=True,
    default="",
    label="Lien Compte Instagram"
)

#register settings to be accessible from settings variable
register_setting(
name="TEMPLATE_ACCESSIBLE_SETTINGS",
default=("CONTACT_EMAIL_FROM", ),
append=True,
editable=True,
)

register_setting(
name="TEMPLATE_ACCESSIBLE_SETTINGS",
default=("CONTACT_EMAIL_TO", ),
append=True,
editable=True,
)

register_setting(
name="TEMPLATE_ACCESSIBLE_SETTINGS",
default=("SITE_SOCIAL_MEDIA_FACEBOOK", ),
append=True,
editable=True,
)

register_setting(
name="TEMPLATE_ACCESSIBLE_SETTINGS",
default=("SITE_SOCIAL_MEDIA_TWITTER", ),
append=True,
editable=True,
)

register_setting(
name="TEMPLATE_ACCESSIBLE_SETTINGS",
default=("SITE_SOCIAL_MEDIA_INSTAGRAM", ),
append=True,
editable=True,
)