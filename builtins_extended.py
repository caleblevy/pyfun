"""Extra, simple, "builtin-like" functions."""


def subclasstree(cls):
    """Return dictionary whose first key is the class and whose
    value is a dict mapping each of its subclasses to their
    subclass trees recursively.
    """
    classtree = {cls: {}}
    for subclass in type.__subclasses__(cls):  # long version allows type
        classtree[cls].update(subclasstree(subclass))
    return classtree


def subclasses(cls):
    """List all subclasses of cls recursively."""
    p = {cls}
    subclasses = set()
    while p:
        subclasses.update(p)
        q = set()
        for base in p:
            for subclass in type.__subclasses__(base):
                if subclass not in subclasses:
                    q.add(subclass)
        p = q
    return subclasses


class PopattrDefault(object):
    """Hacking trick for altering help text docs."""

    def __repr__(self):
        """Moves cursor back to beginning of "default=" and overwrites
        such that it reads "popattr(...)".
        """
        default_text = ("popattr__object, "
                        "popattr__name, "
                        "popattr__default="
                        )
        return '\b'*len(default_text) + "..."


def _make_popattr():
    """Makes popattr with an unreachable default argument."""
    _default_object = PopattrDefault()

    # use stupid long names to prevent keyword args because whatevs.
    def popattr(popattr__object,
                popattr__name,
                popattr__default=_default_object):
        """popattr(object, name[, default]) -> value

        Remove a named attribute from object and return the corresponding
        value. When the attribute does not exist, default is returned if
        given, otherwise an exception is raised.
        """
        # Case for NOT raising errors
        if popattr__default is not _default_object:
            # must return identical to getattr, since there is hasattr
            # weirdness
            attr = getattr(popattr__object, popattr__name, _default_object)
            if attr is not _default_object:  # safe in this case
                delattr(popattr__object, popattr__name)
                return attr  # make sure not to return _default_obj
            else:
                return popattr__default
        else:
            attr = getattr(popattr__object, popattr__name)
            delattr(popattr__object, popattr__name)
            return attr

    return popattr


popattr = _make_popattr()
del _make_popattr, PopattrDefault
