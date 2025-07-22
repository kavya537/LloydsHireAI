from typing import TypedDict, List

class CandidateInfo(TypedDict):
    name: str
    email: str
    skills: List[str]
    experience: int
    match_percentage: float

class JobDescriptionInfo(TypedDict):
    title: str
    description: str
    requirements: List[str]