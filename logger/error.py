class Deprecated(Exception):
    """
    Raised when a deprecated attribute is accessed.

    Attributes:
        old_attr (str): The name of the deprecated attribute.
        new_attr (str | None): The name of the new attribute to use instead, if available.
        deprecated_version (str): The version since which the attribute has been deprecated.
        has_new (bool): Whether a new attribute is available to replace the deprecated one.

    Args:
        old_attr (str): The name of the deprecated attribute.
        deprecated_version (str): The version since which the attribute has been deprecated.
        new_attr (str | None, optional): The name of the new attribute to use instead, if available. Defaults to None.
        has_new (bool, optional): Whether a new attribute is available to replace the deprecated one. Defaults to True.

    Raises:
        Exception: When a deprecated attribute is accessed.

    Example:
        >>> raise Deprecated("old_method", "1.2.3", "new_method")
        Traceback (most recent call last):
        ...
        Deprecated: old_method has deprecated since version 1.2.3, use new_method instead.

        >>> raise Deprecated("old_method", "1.2.3")
        Traceback (most recent call last):
        ...
        Deprecated: old_method has deprecated since version 1.2.3.
    """
    def __init__(self, old_attr: str, deprecated_version, new_attr: str | None = None, has_new: bool = True):
        self._old_attr = old_attr
        self._new_attr = new_attr
        self._deprecated_version = deprecated_version
        self._has_new = has_new
        if self._has_new:
            self._message = f"{old_attr} has deprecated since version {str(deprecated_version)}."
            super().__init__(self._message)
        
        else:    
            self._message = f"{old_attr} has deprecated since version {str(deprecated_version)}, use {new_attr} instead."
            super().__init__(self._message)
            
    @property
    def old_attr(self):
        return self._old_attr
    
    @property
    def new_attr(self):
        return self._new_attr
    
    @property
    def deprecated_version(self):
        return self._deprecated_version
    
    @property
    def has_new(self):
        return self._has_new
    
class WillBeAddInNewerVersion(Exception):
    """
    This exception is used to notify the user that the requested feature or functionality is not implemented in the current version of the software, but it is planned to be added in a future release.

Attributes:
    message (str): A message describing the feature or functionality that will be added in a newer version.

Args:
    message (str): A message describing the feature or functionality that will be added in a newer version.

Raises:
    WillBeAddedInNewerVersion: When a feature or functionality is not available in the current version but will be added in a newer version.

Example:
    `raise WillBeAddedInNewerVersion("The advanced analytics feature will be added in version 2.0.")`
    """
    def __init__(self, attr: str, planned_version):
        self._attr = attr
        self._planned_version = planned_version
        
        self._message = f"{attr} has not been added to module, but will add in version {planned_version}"
        
        super().__init__(self._message)
        
    @property
    def attr(self):
        return self._attr
    
    @property
    def planned_version(self):
        return self._planned_version
    