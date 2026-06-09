import enum
import re
import subprocess
import sys


# Credits: https://stackoverflow.com/a/1630350
def lookahead(iterable):
    """Pass through all values from the given iterable, augmented by the
    information if there are more values to come after the current one
    (True), or if it is the last value (False).
    """
    # Get an iterator and pull the first value.
    it = iter(iterable)
    last = next(it)
    # Run the iterator to exhaustion (starting from the second value).
    for val in it:
        # Report the *previous* value (more to come).
        yield last, True
        last = val
    # Report the last value.
    yield last, False


def contains(a, pos, b):
    ai = pos
    bi = 0
    if len(b) > len(a) - pos:
        return False
    while bi < len(b):
        if a[ai] != b[bi]:
            return False
        ai += 1
        bi += 1
    return True


def split_safe(s: str, delim: str) -> [str]:
    tokens = []
    i = 0
    last = 0
    inside = 0
    while i < len(s):
        c = s[i]
        if i == len(s) - 1:
            tokens.append(s[last : i + 1])
        if c in ('<', '[', '{', '('):
            inside += 1
            i += 1
            continue
        if c in ('>', ']', '}', ')'):
            inside -= 1
            i += 1
            continue
        if inside > 0:
            i += 1
            continue
        if contains(s, i, delim):
            tokens.append(s[last:i])
            i += 2
            last = i
        i += 1
    return tokens


_ANONYMOUS_SYNTHETIC_TOKEN_RE = re.compile(r'^@\d+$')
# Matches Doxygen synthetic anonymous compound names, for example:
# `bsp_display_cfg_t::@020116075137215116233064045310076123006060214171`
_ANONYMOUS_SYNTHETIC_NAME_RE = re.compile(r'(?<![\w/])(?:[A-Za-z_](?:\\.|\w)*::)*@\d+\b')


def is_anonymous_synthetic_name(name: str) -> bool:
    if not name:
        return False
    return bool(_ANONYMOUS_SYNTHETIC_TOKEN_RE.match(name.rsplit('::', maxsplit=1)[-1]))


def anonymous_compound_label(kind: str) -> str:
    if kind == 'union':
        return 'anonymous union'
    if kind == 'struct':
        return 'anonymous struct'
    return 'anonymous type'


def sanitize_anonymous_compound_type(type_name: str) -> str:
    if not type_name:
        return type_name

    sanitized = _ANONYMOUS_SYNTHETIC_NAME_RE.sub('anonymous', type_name)
    sanitized = re.sub(r'\bunion\s+anonymous\s+union\b', 'anonymous union', sanitized)
    sanitized = re.sub(r'\bstruct\s+anonymous\s+struct\b', 'anonymous struct', sanitized)
    sanitized = re.sub(r'\bunion\s+anonymous\b', 'anonymous union', sanitized)
    sanitized = re.sub(r'\bstruct\s+anonymous\b', 'anonymous struct', sanitized)
    return sanitized


def get_git_revision_hash() -> str:
    try:
        return subprocess.check_output(['git', 'rev-parse', 'HEAD']).decode('ascii').strip()
    except subprocess.CalledProcessError:
        return ''


class ColoredPrinter(enum.Enum):
    grey: str = '\x1b[37;20m'
    yellow: str = '\x1b[33;20m'
    red: str = '\x1b[31;20m'

    reset: str = '\x1b[0m'


def _color_fmt(msg: str, color: ColoredPrinter) -> str:
    if sys.platform == 'win32':  # does not support it
        return msg

    return color.value + msg + ColoredPrinter.reset.value


def info(msg: str) -> None:
    print(_color_fmt(msg, ColoredPrinter.grey))


def warning(msg: str) -> None:
    print(_color_fmt(msg, ColoredPrinter.yellow))


def error(msg: str) -> None:
    print(_color_fmt(msg, ColoredPrinter.red))
