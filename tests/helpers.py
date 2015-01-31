from django.test import override_settings


def setup_template_loader(templates):
    return override_settings(TEMPLATES={
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'OPTIONS': {
            'loaders': [('django.template.loaders.locmem.Loader', templates)],
        },
    })
