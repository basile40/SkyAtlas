from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True)
class SevereAlert:
    id: str
    headline: str
    severity: str
    event: str
    effective: datetime
    expires: datetime
    area_description: str