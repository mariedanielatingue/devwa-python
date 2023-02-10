
import re


DATA_TEXT = "salut ma fille# comment vas tu? # demain j'acheterai une belle voiture pour toi!#"

def replace_hashtag_by_link(value):
    return re.sub("#[\w]+", lambda x: "<a href=''>{}</a>".format(x.group()), value)

print(replace_hashtag_by_link(DATA_TEXT))