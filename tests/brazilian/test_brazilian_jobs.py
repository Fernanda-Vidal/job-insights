from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():

    list_dict = read_brazilian_file("tests/mocks/brazilians_jobs.csv")
    for dict in list_dict:
        assert "title" and "salary" and "type" in dict
