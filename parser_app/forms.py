from django import forms
from . import models, parser


class ParserForm(forms.Form):
    MEDIA_CHOISES = (("BOOKS", "BOOKS"),)
    media_type = forms.ChoiceField(choices=MEDIA_CHOISES)

    class Meta:
        fields = [
            "media_type",
        ]

    def parser_data(self):
        if self.data["media_type"] == "BOOKS":
            book_parser = parser.parser()
            for i in book_parser:
                models.BookParser.objects.create(**i)
