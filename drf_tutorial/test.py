# -*- coding: utf-8 -*-
import os
import django

#  you have to set the correct path to you settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_tutorial.settings")
django.setup()


from apps.snippets.models import Snippet
from apps.snippets.serializers import SnippetSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


def run():
    snippet = Snippet(code='foo = "bar"\n')
    # print the methods and attributes of the snippet instance avoid every item with __
    print('Methods in Model instance: ',[item for item in dir(snippet) if not item.startswith('_')])

    serializer = SnippetSerializer(snippet)
    print('Methods in Serializer instance: ',[item for item in dir(serializer) if not item.startswith('_')])

    


if __name__ == '__main__':
    run()