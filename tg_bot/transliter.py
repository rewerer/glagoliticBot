class GlagoliticTransliter:
    """
    Транслитератор кирилицы в глаголицу.
    """

    cyrillic_to_glagolitic_table = {
        "\u0430": "\u2c30",
        "\u0431": "\u2c31",
        "\u0432": "\u2c32",
        "\u0433": "\u2c33",
        "\u0434": "\u2c34",
        "\u0435": "\u2c35",
        "\u0451": "\u2c56",
        "\u0436": "\u2c36",
        "\u0437": "\u2c38",
        "\u0438": "\u2c3a",
        "\u0439": "\u2C3A",
        "\u043a": "\u2c3d",
        "\u043b": "\u2c3e",
        "\u043c": "\u2c3f",
        "\u043d": "\u2c40",
        "\u043e": "\u2c41",
        "\u043f": "\u2c42",
        "\u0440": "\u2c43",
        "\u0441": "\u2c44",
        "\u0442": "\u2c45",
        "\u0443": "\u2c46",
        "\u0444": "\u2c47",
        "\u0445": "\u2c48",
        "\u0446": "\u2c4c",
        "\u0447": "\u2c4d",
        "\u0448": "\u2c4e",
        "\u0449": "\u2c4b",
        "\u044a": "\u2c4f",
        "\u044b": "\u2C4F\u2C39",
        "\u044c": "\u2c50",
        "\u044d": "\uef61",
        "\u044e": "\u2c53",
        "\u044f": "\u2c5d",
    }
#\u2C1F\u2C09
    glagolitic_to_cyrillic_table = {
        "\u2c30": "\u0430",
        "\u2c31": "\u0431",
        "\u2c32": "\u0432",
        "\u2c33": "\u0433",
        "\u2c34": "\u0434",
        "\u2c35": "\u0435",
        "\u2c56": "\u0451",
        "\u2c36": "\u0436",
        "\u2c38": "\u0437",
        "\u2c3a": "\u0438",
        "\uef63": "\u0439",
        "\u2c3d": "\u043a",
        "\u2c3e": "\u043b",
        "\u2c3f": "\u043c",
        "\u2c40": "\u043d",
        "\u2c41": "\u043e",
        "\u2c42": "\u043f",
        "\u2c43": "\u0440",
        "\u2c44": "\u0441",
        "\u2c45": "\u0442",
        "\u2c46": "\u0443",
        "\u2c47": "\u0444",
        "\u2c48": "\u0445",
        "\u2c4c": "\u0446",
        "\u2c4d": "\u0447",
        "\u2c4e": "\u0448",
        "\u2c4b": "\u0449",
        "\u2c4f": "\u044a",
        "\uef5f": "\u044b",
        "\u2c50": "\u044c",
        "\uef61": "\u044d",
        "\u2c53": "\u044e",
        "\u2c5d": "\u044f",
    }

    @classmethod
    def cyrillic_to_glagolitic(cls, text: str) -> str:
        translited_text = ""
        for letter in text:
            if letter in cls.cyrillic_to_glagolitic_table:
                translited_text = translited_text + cls.cyrillic_to_glagolitic_table[letter]
            elif letter.lower() in cls.cyrillic_to_glagolitic_table:
                translited_text = (
                        translited_text + cls.cyrillic_to_glagolitic_table[letter.lower()].upper()
                )
            else:
                translited_text = translited_text + letter
        return translited_text

    @classmethod
    def glagolitic_to_cyrillic(cls, text: str) -> str:
        translited_text = ""
        for letter in text:
            if letter in cls.glagolitic_to_cyrillic_table:
                translited_text = translited_text + cls.glagolitic_to_cyrillic_table[letter]
            elif letter.lower() in cls.glagolitic_to_cyrillic_table:
                translited_text = (
                        translited_text + cls.glagolitic_to_cyrillic_table[letter.lower()].upper()
                )
            else:
                translited_text = translited_text + letter
        return translited_text

__all__ = ["GlagoliticTransliter"]