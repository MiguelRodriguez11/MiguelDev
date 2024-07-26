import pytest
from linkBio.model.language import LanguageModel

def test_get_languages():
    languages = LanguageModel.get_languages()
    assert languages != None

def test_get_languages_elemnts():
    languages = LanguageModel.get_languages()
    assert len(languages) > 0

def test_get_languages_lenght():
    languages = LanguageModel.get_languages()
    for languages in languages:
        assert len(languages)>0