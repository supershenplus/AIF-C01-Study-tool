"""Question bank for the AWS AI Practitioner (AIF-C01) Study Tool.

100 questions across 5 domains, weighted by exam percentage.
"""

from .models import DomainInfo, Question
from .questions_d1d2 import D1_QUESTIONS, D2_QUESTIONS
from .questions_d3d4d5 import D3_QUESTIONS, D4_QUESTIONS, D5_QUESTIONS


DOMAINS = [
    DomainInfo(
        number=1,
        name="Fundamentals of AI and ML",
        weight=20,
        subdomains=[
            "1.1 Basic AI concepts and terminologies",
            "1.2 Practical use cases for AI",
            "1.3 ML development lifecycle",
            "1.4 AWS AI/ML services",
        ],
    ),
    DomainInfo(
        number=2,
        name="Fundamentals of Generative AI",
        weight=24,
        subdomains=[
            "2.1 Foundation models and architectures",
            "2.2 Prompt engineering",
            "2.3 Fine-tuning and customization",
            "2.4 AWS generative AI services",
        ],
    ),
    DomainInfo(
        number=3,
        name="Applications of Foundation Models",
        weight=28,
        subdomains=[
            "3.1 Text generation applications",
            "3.2 RAG and knowledge bases",
            "3.3 AI agents and reasoning",
            "3.4 Multimodal and image applications",
        ],
    ),
    DomainInfo(
        number=4,
        name="Guidelines for Responsible AI",
        weight=14,
        subdomains=[
            "4.1 Fairness and bias",
            "4.2 Explainability and transparency",
            "4.3 AI governance",
        ],
    ),
    DomainInfo(
        number=5,
        name="Security, Compliance, and Governance",
        weight=14,
        subdomains=[
            "5.1 Security for AI",
            "5.2 Compliance",
            "5.3 Monitoring and governance",
        ],
    ),
]

_ALL_RAW = D1_QUESTIONS + D2_QUESTIONS + D3_QUESTIONS + D4_QUESTIONS + D5_QUESTIONS


def get_all_questions() -> list[Question]:
    """Return all questions as Question objects."""
    return [Question.from_dict(q) for q in _ALL_RAW]


def get_questions_by_domain(domain: int) -> list[Question]:
    """Return questions for a specific domain."""
    return [Question.from_dict(q) for q in _ALL_RAW if q["domain"] == domain]
