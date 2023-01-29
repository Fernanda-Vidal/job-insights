from src.pre_built.sorting import sort_by

mock_jobs_list = [
    {"max_salary": 100, "min_salary": 10, "date_posted": "2022-10-10"},
    {"max_salary": 1980, "min_salary": 1250, "date_posted": "2021-11-25"},
    {"max_salary": 2560, "min_salary": 1590, "date_posted": "2023-01-13"},
]


def test_sort_by_criteria():
    sort_by(jobs=mock_jobs_list, criteria="max_salary")
    assert mock_jobs_list == [
        {"max_salary": 2560, "min_salary": 1590, "date_posted": "2023-01-13"},
        {"max_salary": 1980, "min_salary": 1250, "date_posted": "2021-11-25"},
        {"max_salary": 100, "min_salary": 10, "date_posted": "2022-10-10"}
    ]

    sort_by(jobs=mock_jobs_list, criteria="min_salary")
    assert mock_jobs_list == [
        {"max_salary": 100, "min_salary": 10, "date_posted": "2022-10-10"},
        {"max_salary": 1980, "min_salary": 1250, "date_posted": "2021-11-25"},
        {"max_salary": 2560, "min_salary": 1590, "date_posted": "2023-01-13"}
    ]

    sort_by(jobs=mock_jobs_list, criteria="date_posted")
    assert mock_jobs_list == [
        {"max_salary": 2560, "min_salary": 1590, "date_posted": "2023-01-13"},
        {"max_salary": 100, "min_salary": 10, "date_posted": "2022-10-10"},
        {"max_salary": 1980, "min_salary": 1250, "date_posted": "2021-11-25"}
    ]
    