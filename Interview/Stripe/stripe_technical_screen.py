import re
def func(client_string:str, server_string:list):
    if len(client_string) == 0:
        return None
    client_list = client_string.split(', ')
    for entry in client_list:
        if len(entry) == 2:
            return [((re.search(entry, string)).string) for string in server_string if re.search(entry, string)]
        return [lang for lang in client_list if lang in server_string ]




assert func("en-US, fr-FR, ge-GR", ["en-US", "fr-FR"]) == ["en-US","fr-FR"]
assert func("", ["en-US", "fr-FR"]) == None
assert func("en-US, fr-FR, ge-GR", ["tn-TN"]) == []
assert func("en, tn-TN", ["en-EN", "fr-FR"]) == ["en-EN"]
