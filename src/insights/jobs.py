from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """
    # raise NotImplementedError

    with open(path) as file:
        jobs_reader = csv.DictReader(file, delimiter=",", quotechar='"')
        jobs = list(jobs_reader)
    return jobs


def get_unique_job_types(path: str) -> List[str]:
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    # raise NotImplementedError
    jobs_types = read(path)
    jobs = []
    for type in jobs_types:
        if type["job_type"] not in jobs:
            jobs.append(type["job_type"])
        else:
            pass

    return jobs


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    # raise NotImplementedError
    filtered_jobs = []

    for job in jobs:
        if job["job_type"] == job_type:
            filtered_jobs.append(job)

    return filtered_jobs
