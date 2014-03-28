# from __future__ import unicode_literals

# from django.utils.encoding import force_text
# from django.utils.functional import wraps
# from django.utils import six


# def parse_tags(tagstring):
#     """
#     Parses tag input, with multiple word input being activated and
#     delineated by commas.

#     Modified by mario <mariusz.karwala@tivix.com>
#     """
#     if not tagstring:
#         return []

#     tagstring = force_text(tagstring)

#     words = list(set(split_strip(tagstring, ',')))
#     words.sort()
#     return words


# def split_strip(string, delimiter=','):
#     if not string:
#         return []

#     words = [w.strip() for w in string.split(delimiter)]
#     return [w for w in words if w]


# def edit_string_for_tags(tags):
#     """
#     Renders tag input, with multiple word input being activated and
#     delineated by commas.

#     Modified by mario <mariusz.karwala@tivix.com>
#     """
#     names = []
#     for tag in tags:
#         name = tag.name
#         names.append(name)
#     return ', '.join(sorted(names))


# def require_instance_manager(func):
#     @wraps(func)
#     def inner(self, *args, **kwargs):
#         if self.instance is None:
#             raise TypeError("Can't call %s with a non-instance manager" % func.__name__)
#         return func(self, *args, **kwargs)
#     return inner
