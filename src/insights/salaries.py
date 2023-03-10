from typing import Union, List, Dict
from src.insights import jobs


def get_max_salary(path: str) -> int:
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    # raise NotImplementedError
    jobs_salary = jobs.read(path)
    max_salary_job = []

    for item in jobs_salary:
        if item["max_salary"].isnumeric():
            max_salary_job.append(int(item["max_salary"]))

    return max(max_salary_job)


def get_min_salary(path: str) -> int:
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    # raise NotImplementedError
    jobs_salary = jobs.read(path)
    min_salary_job = []

    for item in jobs_salary:
        if item["min_salary"].isnumeric():
            min_salary_job.append(int(item["min_salary"]))

    return min(min_salary_job)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    # raise NotImplementedError

    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError('min_salary or max_salary does not exists')

    try:
        request_salary = int(salary)
        max_salary = int(job["max_salary"])
        min_salary = int(job["min_salary"])

    # Consulta em: http://turing.com.br/pydoc/2.7/tutorial/errors.html
    except (ValueError, TypeError, NameError):
        raise ValueError('some fields are not valid integers')

    else:
        if max_salary < min_salary:

            raise ValueError('max_salary is smaller than min_salary')
        return max_salary >= request_salary >= min_salary

    finally:
        print("Try checking if request salary match with the range")


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    # raise NotImplementedError

    filtered_salaries = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary) is True:
                filtered_salaries.append(job)

        except ValueError:
            ValueError

    return filtered_salaries
