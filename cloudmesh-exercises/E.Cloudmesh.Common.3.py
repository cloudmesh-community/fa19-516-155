# fa19-516-155 E.Cloudmesh.Common.3
"""
Usage: E.Cloudmesh.Common.3.py [-h]

Function to convert input dictionary to a flat dictionary using cloudmesh utility FlatDict

Arguments:
  ipDict    input dict to convert to a flat dictionary.

Options:
-h --help
"""
from cloudmesh.common.FlatDict import FlatDict
from cloudmesh.common.util import banner

if __name__=="__main__":
    d = {
        "glossary": {
            "title": "example glossary",
            "GlossDiv": {
                "title": "S",
                "GlossList": {
                    "GlossEntry": {
                        "ID": "SGML",
                        "SortAs": "SGML",
                        "GlossTerm": "Standard Generalized Markup Language",
                        "Acronym": "SGML",
                        "Abbrev": "ISO 8879:1986",
                        "GlossDef": {
                            "para": "A meta-markup language, used to create markup languages such as DocBook.",
                            "GlossSeeAlso": ["GML", "XML"]
                        },
                        "GlossSee": "markup"
                    }
                }
            }
        }
    }
    banner("Converting input dictionary to a Flat Dictionary and printing keys: ")
    d1 = FlatDict(d)

    for i in d1.keys():
        print(i, " : ", d1[i])