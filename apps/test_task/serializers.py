# IDE: PyCharm
# Project: maklai-internship
# Path: apps/test_task
# File: serializers.py
# Contact: Semyon Mamonov <semyon.mamonov@gmail.com>
# Created by ox23 at 2023-04-30 (y-m-d) 9:05 PM

from typing import Union

from rest_framework import serializers
from rest_framework.settings import api_settings
from rest_framework.exceptions import ValidationError
from rest_framework.fields import empty

from .utils.tree import NLTKTreeParaphrase


class Paraphrase:
    def __init__(self, tree: str):
        self.tree = tree


class ParaphraseSerializer(serializers.BaseSerializer):

    syntax_tree_url_kwargs = 'tree'
    syntax_tree_path = 'NP.NP'

    def __init__(self, instance=None, data=empty, **kwargs):
        self.paraphraser: NLTKTreeParaphrase = None
        super().__init__(instance, data, **kwargs)

    def _validate_stree(self, stree) -> Union[NLTKTreeParaphrase, ValidationError]:
        if not stree:
            raise ValidationError({
                self.syntax_tree_url_kwargs: ['Parameter `%s` is empty:' % self.syntax_tree_url_kwargs],
            })

        try:
            pphraser = NLTKTreeParaphrase(stree, self.syntax_tree_path)
        except Exception as exc:
            raise ValidationError({
                api_settings.NON_FIELD_ERRORS_KEY:
                    ['`%s` is probably malformed (error: %s)' % (self.syntax_tree_url_kwargs, exc.args[0])]
            })
        return pphraser

    def to_representation(self, instance: str):
        return {
            self.syntax_tree_url_kwargs: ' '.join(instance.split())
        }

    def to_internal_value(self, data):
        self.paraphraser = self._validate_stree(data.get(self.syntax_tree_url_kwargs))
        data[self.syntax_tree_url_kwargs] = self.paraphraser

        return data
