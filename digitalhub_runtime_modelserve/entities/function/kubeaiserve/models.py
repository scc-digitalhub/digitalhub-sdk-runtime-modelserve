from __future__ import annotations

from typing import Optional

from pydantic import BaseModel


class KubeaiAdapter(BaseModel):
    url: Optional[str] = None
    name: Optional[str] = None
