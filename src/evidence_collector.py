"""
TAIF Evidence Collector
Sprint 2.4 Stable Version
"""

from dataclasses import dataclass, asdict
from typing import List
import feedparser


@dataclass
class Evidence:
    evidence_id: str
    stock_id: str
    company: str
    published_time: str
    title: str
    source: str
    url: str
    content: str
    evidence_type: str


class EvidenceCollector:

    def __init__(self):
        print("EvidenceCollector initialized.")

    def _build_rss_url(self, keyword: str):

        return f"https://news.google.com/rss/search?q={keyword}"

    def collect(
        self,
        stock_id: str,
        company_name: str = "",
        limit: int = 10,
    ):

        keyword = company_name if company_name else stock_id

        rss_url = self._build_rss_url(keyword)

        feed = feedparser.parse(rss_url)

        evidence_list = []

        for i, entry in enumerate(feed.entries[:limit]):

            evidence = Evidence(

                evidence_id=f"{stock_id}_{i+1:04d}",

                stock_id=stock_id,

                company=company_name,

                published_time=entry.get("published", ""),

                title=entry.get("title", ""),

                source=feed.feed.get("title", "Google News"),

                url=entry.get("link", ""),

                content=entry.get("summary", ""),

                evidence_type="news",

            )

            evidence_list.append(asdict(evidence))

        return evidence_list