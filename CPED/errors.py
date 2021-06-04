class CharError(Exception): pass
class ListLenError(Exception): pass
class UnUsedCharsConfiguration(Exception): pass
class ConfigurationUnCompleted(Exception): pass
class ConfigurationUnChecked(Exception): pass
class StrListSizeError(Exception): pass

Error = [
    "A char may be missing or added on a list that need the same amount of values as another list.",
    "A list has not the same length as his linked list/word.",
    "A configured used char list has been configure but it isn't used in global configuration.",
    "Configured is not completed, be sure that you configure correctly you configure as in your Configure() function.",
    "Configuration has not been checked !",
    "Maximum list size for type: str <= 26 !",
    "Type isn't taking in charge for the moment.",
    "Type: Str has only attributes: 'lower' and 'upper'."
]