"""Class of utils.
"""
import json
import urlparse

from django.core.serializers.json import DjangoJSONEncoder
from django.utils.html import escape

from tastypie.serializers import Serializer


class PrettyJSONSerializer(Serializer):
    """Class to return a JSON indented as standard.

    Attributes:
        content_types (TYPE): Accepted content types.
        formats (list): Accepted formats.
        json_indent (int): Number of spaces to idents.
    """
    json_indent = 2
    formats = ['json', 'jsonp', 'xml', 'yaml', 'html', 'plist', 'urlencode']
    content_types = {
        'json': 'application/json',
        'jsonp': 'text/javascript',
        'xml': 'application/xml',
        'yaml': 'text/yaml',
        'html': 'text/html',
        'plist': 'application/x-plist',
        'urlencode': 'application/x-www-form-urlencoded',
    }

    def to_json(self, data, options=None):
        """Class to serialize a json object.

        Args:
            data (TYPE): Data to serialize.
            options (None, optional): Serialize options.

        Returns:
            TYPE: json.
        """
        options = options or {}
        data = self.to_simple(data, options)
        return json.dumps(data, cls=DjangoJSONEncoder,
                          sort_keys=True, ensure_ascii=False,
                          indent=self.json_indent)

    def from_urlencode(self, data, options=None):
        """Handles basic formencoded url posts

        Args:
            data (TYPE): Url data to encode.
            options (None, optional): Encode options.
        """
        qs = dict((k, v if len(v) > 1 else v[0])
                  for k, v in urlparse.parse_qs(data).iteritems())

        return qs

    def to_urlencode(self, content):
        """Handles basic formencoded url posts

        Args:
            content (TYPE): Data to encode.

        Returns:
            TYPE: Encoded data.
        """
        pass


def sanitize(text):
    """Replace single quotes.

    Args:
        text (TYPE): Text to replace.

    Returns:
        TYPE: Replaced text.
    """
    # We put the single quotes back, due to their frequent usage in exception
    # messages.
    return escape(text).replace('&#39;', "'").replace('&quot;', '"')


def expand_line(line, filler, padding_width, count=None):
    if count is None:
        count = line.count(filler)
    if count <= 0:
        return line
    else:
        next_filler = line.index(filler)
        if next_filler < 0:
            return line
        elif next_filler == (len(line) - 1):
            return line[:-1]
        else:
            padding = ' ' * (padding_width / count)
            return line[:next_filler] + padding + expand_line(
                line[next_filler + 1:],
                filler,
                padding_width - len(padding),
                count - 1)
