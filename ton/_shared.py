import collections

from ton import tags

ParseResult = collections.namedtuple(
    'ParseResult',
    [
        'success',
        'value',
        'remaining',
    ],
)

_FAILED_PARSE_RESULT = ParseResult(success = False, value = None, remaining = None)
