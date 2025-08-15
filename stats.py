
def get_num_words(file):
    with open(file) as f:
        file_contents = f.read()
        file_list = file_contents.split()
        return len(file_list)
    
def get_num_char(file):
    with open(file) as f:
        file_contents = f.read()
        file_l = file_contents.lower()
        num_char = {}
        for l in file_l:
            if l in num_char:
                num_char[l] += 1
            else:
                num_char[l] = 1
        return num_char   

def sort_count(items):
    return items["count"]

def get_list_dict(file):
    dict_char = get_num_char(file)
    list = []
    for l in dict_char:
        extra_dict = {"char" : l, "count" : dict_char[l]}
        list.append(extra_dict)
    list.sort(reverse=True,key=sort_count)
    return list
    
