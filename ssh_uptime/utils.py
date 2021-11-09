from datetime import datetime, timezone, timedelta


def get_time() -> str:
    return datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(timezone(timedelta(hours=8))).isoformat()
