def create_movie_list(input_file, delimiter, keys, null_value, title_id, information):
    x = 5
    results = list()
    memo = set()
    with open(input_file, 'r', encoding=None) as f:
        
        header_name=f.readline()
        movies = f.readlines()
        lines=list()

    for line in movies:
        lines.append(line.strip('\n').split(delimiter))

    lines=sorted(lines, key = lambda x: x[0])
    
    for parts in lines:
        info_dict = dict()
        if parts[0] not in memo:
            memo.add(parts[0])
            if x != 5:
                results.append(d_line)
            x = 3
            d_line = dict()
            d_line[title_id] = parts[0]
            d_line[information] = []
            for i in range(len(keys)):
                j = i + 2
                if parts[j] != null_value:
                    info_dict[keys[i]] = parts[j]
            if parts[1] == '1':
                d_line['original_title'] = parts[2]
            d_line[information].append(info_dict)
        else:
            for i in range(len(keys)):
                j = i + 2
                if parts[j] != null_value:
                    info_dict[keys[i]] = parts[j]
            d_line[information].append(info_dict)
            if parts[1] == '1':
                d_line['original_title'] = parts[2]
    if x != 5:
        results.append(d_line)
    return results


def return_title_id_original_title_dict(movie_list, title_id):
    original_title_dict= dict()
    num=len(movie_list)
    key_to_check='original_title'
    
    for i in range(num):
        if key_to_check in movie_list[i]:
            id=movie_list[i][title_id]
            original_title_dict[id]= movie_list[i][key_to_check]
    return original_title_dict

def return_information_element_set(**kwargs):
    movies_list = kwargs['movie_list']
    key = kwargs['key']
    info='information'
    num=len(movies_list)
    unique_set=set()
    for i in range(num):
        # if field information is in the dictionary entry
        if info in movies_list[i]:
            for info_dict in movies_list[i][info]:
                # check if the key is in the info dictionary of the current movie dictionary 
                if key in info_dict:
                    unique_set.add(info_dict[key])
    return unique_set


def sort_information(**kwargs):
   
    output=list()
    info = 'information'
    movie_list = kwargs['movie_list']
    num = len(movie_list)
    key = kwargs['key']
    id= list(movie_list[0].keys())[0]
    
    #for each movie sort by the key field 
    for i in range(num):

        info_dict=dict()
        info_dict['title_id']=movie_list[i][id]

        key_items = [item for item in movie_list[i][info] if key in item.keys()]

#Dictionaries not with key p
        non_key_items = [item for item in movie_list[i][info] if key not in item.keys()]

#Sort the p-key dictionaries
        #info_dict[info]=list()
        sorted_key_items= sorted(key_items, key=lambda i: i.get(key))
        info_dict[info]=non_key_items+sorted_key_items   

#Attach non p-key dictionay items at end
        
        output.append(info_dict)


    return output
