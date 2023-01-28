from typing import List, Dict
from src.insights import jobs


def get_unique_industries(path: str) -> List[str]:
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    # raise NotImplementedError

    industries_read = jobs.read(path)
    industries = []
    for item in industries_read:
        if item["industry"] not in industries:
            if item["industry"] == "":
                pass
            else:
                industries.append(item["industry"])
        else:
            pass

    return industries


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    # raise NotImplementedError
    filtered_job_industry = []

    for job in jobs:
        if job["industry"] == industry:
            filtered_job_industry.append(job)

    return filtered_job_industry
