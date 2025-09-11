from datetime import datetime
from tracker import storage


def calculate_hours(entries):
    report = {}
    for project, start, end in entries:
        start_dt = datetime.fromisoformat(start)
        end_dt = datetime.fromisoformat(end) if end else datetime.now()
        duration = (end_dt - start_dt).total_seconds() / 3600
        report[project] = report.get(project, 0) + duration
    return report


def start_project(project: str):
    storage.add_start(project)


def stop_project(project: str):
    storage.stop(project)


def generate_report():
    entries = storage.fetch_entries()
    return calculate_hours(entries)
