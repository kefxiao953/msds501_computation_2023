from q1_2_4 import *

def return_movie_by_id(movie_list, title_id, title_id_val):
    """
    Return a movie (dict) where its title_id's value is title_id
    """
    for movie in movie_list:
        if movie[title_id] == title_id_val:
            return movie
def return_information(movie_list, title_id, title_id_val, information):
    """
    For the given movie_list returned from create_movie_list(),
    return the movie which title_id is same as title_id argument.
    """
    return return_movie_by_id(movie_list, title_id, title_id_val)[information]


def return_information_value(movie_list_information, key, value):
    """
    For information, an array which is the value of "information"
    created by create_movie_list(),
    return a movie dictionary where its key and value matches
    with key/vaue arguments.
    """
    for movie_info in movie_list_information:
        if movie_info[key] == value:
            return movie_info
        
def test_create_movie_list_1():
    """
    First test case for create_movie_list()
    """
    input_file = './imdb_titles_small.tsv'
    delimiter = '\t'
    keys = ['title', 'region', 'language', 'types']
    null_value = '\\N'
    title_id = 'title_id'
    information = 'information'

    movie_list = create_movie_list(input_file, delimiter, keys,
                                   null_value, title_id, information)
    assert len(movie_list) == 99\
        and len(return_information(movie_list, title_id,
                                   'tt0000012', information)) == 28\
        and return_information_value(return_information(movie_list,
                                                        title_id,
                                                        'tt0000012',
                                                        information),
                                     'region', 'ES') ==\
        {'title': 'La llegada de un tren a la estación de La Ciotat',
         'region': 'ES', 'types': 'imdbDisplay'}


def test_create_movie_list_2():
    """
    Second test case for create_movie_list()
    """
    input_file = './imdb_titles_medium.tsv'
    delimiter = '\t'
    keys = ['title', 'region', 'language', 'types']
    null_value = '\\N'
    title_id = 'title_id'
    information = 'information'

    movie_list = create_movie_list(input_file, delimiter, keys, null_value,
                                   title_id, information)
    assert len(movie_list) == 3363\
           and len(return_information(movie_list, title_id,
                                      'tt0002825', information)) == 2\
           and return_information_value(return_information(movie_list,
                                                           title_id,
                                                           'tt0002825',
                                                           information),
                                        'types',
                                        'imdbDisplay') ==\
           {'title': 'An Elephant on His Hands',
            'region': 'US', 'types': 'imdbDisplay'}
    

def test_sort_information():
    """
    Test case for sort_information()
    """
    input_file = './imdb_titles_small.tsv'
    delimiter = '\t'
    keys = ['title', 'region', 'language', 'types']
    null_value = '\\N'
    title_id = 'title_id'
    information = 'information'

    movie_list = create_movie_list(input_file, delimiter, keys,
                                   null_value, title_id, information)
    filtered_list = list()
    filtered_list.append(return_movie_by_id(movie_list, title_id, 'tt0000001'))
    filtered_list.append(return_movie_by_id(movie_list, title_id, 'tt0000002'))

    assert sort_information(movie_list=filtered_list,
                            key='region')[0][information] ==\
           [{'title': 'Carmencita', 'types': 'original'},
            {'title': 'Carmencita', 'region': 'DE'},
            {'title': 'Καρμενσίτα', 'region': 'GR', 'types': 'imdbDisplay'},
            {'title': 'Carmencita - spanyol tánc', 'region': 'HU',
             'types': 'imdbDisplay'},
            {'title': 'カルメンチータ', 'region': 'JP', 'language': 'ja',
             'types': 'imdbDisplay'},
            {'title': 'Карменсита', 'region': 'RU', 'types': 'imdbDisplay'},
            {'title': 'Карменсіта', 'region': 'UA', 'types': 'imdbDisplay'},
            {'title': 'Carmencita', 'region': 'US', 'types': 'imdbDisplay'}]\
           and sort_information(movie_list=filtered_list,
                                number=2,
                                key='region')[1][information] ==\
           [{'title': 'Le clown et ses chiens', 'types': 'original'},
            {'region': 'DE', 'title': 'Der Clown und seine Hunde'},
            {'region': 'FR', 'title': 'Le clown et ses chiens',
             'types': 'imdbDisplay'},
            {'region': 'HU', 'title': 'A bohóc és kutyái',
             'types': 'imdbDisplay'},
            {'language': 'ja', 'region': 'JP', 'title': '道化師と犬',
             'types': 'imdbDisplay'},
            {'region': 'RO', 'title': 'Clovnul si cainii sai',
             'types': 'imdbDisplay'},
            {'region': 'RU', 'title': 'Клоун и его собаки',
             'types': 'imdbDisplay'},
            {'region': 'US', 'title': 'The Clown and His Dogs'}]
