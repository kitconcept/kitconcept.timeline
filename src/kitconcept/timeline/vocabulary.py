# -*- coding: utf-8 -*-
from datetime import date
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


def YearVocabulary(context):
    """Vocabulary factory for year options."""

    current_year = date.today().year
    return SimpleVocabulary([
        SimpleTerm(value=year)
        for year in range(
            current_year + 1,
            current_year - 30,
            -1
        )
    ])
