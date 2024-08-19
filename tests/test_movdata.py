from movdata.ml import save_movies
from movdata.mov_detail import load_movie_list, make_movie_info_data

# 연도별 영화 저장
# def test_save_movies():
#     for i in range(2015, 2022):
#         r = save_movies(year=i, sleep_time=0.1)
#         assert r

# 연도별 저장된 영화들의 상세 정보 저장
def test_load_movies():
    assert make_movie_info_data(2015)