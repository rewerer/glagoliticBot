class GlagoliticTransliter:
    """
    Транслитератор кирилицы в глаголицу.
    """

    english_to_gothic_table = {
        "\u0061": "\U00010330",
        "\u0062": "\U00010331",
        #"\u0063": "\u10330",  #c
        "\u0064": "\U00010333",
        "\u0065": "\U00010334",  #e
        "\u0066": "\U00010346",
        "\u0067": "\U00010332",
        "\u0068": "\U00010337",  #h
        "\u0069": "\U00010339",
        "\u006A": "\U0001033E",
        "\u006B": "\U0001033A",  #k
        "\u006C": "\U0001033B",
        "\u006D": "\U0001033C",
        "\u006E": "\U0001033D",  #n
        "\u006F": "\U00010349",
        "\u0070": "\U00010340",
        "\u0071": "\U00010335",  #q
        "\u0072": "\U00010342",
        "\u0073": "\U00010343",   #s
        "\u0074": "\U00010344",
        "\u0075": "\U0001033F",  #u
        #"\u0076": "\u10330",   #v
        "\u0077": "\U00010345",  #w
        "\u0078": "\U00010347",  #x
        "\u0079": "\U00010345",  #y
        "\u007A": "\U00010336",  #z
        "\u00FE": "\U00010338",
        # "\u0074\u0068": "",
    }

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

    @classmethod
    def english_to_gothic(cls, text: str) -> str:
        translited_text = ""
        length = len(text)
        skipped_step = -1
        for i in range(0, length):
            if i == skipped_step:
                continue
            letter = text[i]
            if letter == 't' or letter == 'T':
                if i < (length - 1):
                    if text[i + 1].lower() == 'h':
                        translited_text = translited_text + "\U00010338"
                        skipped_step = i + 1
                else:
                    translited_text = translited_text + cls.english_to_gothic_table['t']
            elif letter == 'h' or letter == 'H':
                if i < (length - 1):
                    if text[i + 1].lower() == 'w':
                        translited_text = translited_text + "\U00010348"
                        skipped_step = i + 1
                else:
                    translited_text = translited_text + cls.english_to_gothic_table['h']
            elif letter in cls.english_to_gothic_table:
                translited_text = translited_text + cls.english_to_gothic_table[letter]
            elif letter.lower() in cls.english_to_gothic_table:
                translited_text = (
                        translited_text + cls.english_to_gothic_table[letter.lower()].upper()
                )
            else:
                translited_text = translited_text + letter
        return translited_text

__all__ = ["GlagoliticTransliter"]