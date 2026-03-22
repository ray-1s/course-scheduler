# test_schedule.py
from app import SchedulingInput, _solve_schedule

# Your hardcoded input as a Python dictionary
test_input = {
    "sections": [
        {
            "id": "sec1",
            "course_id": "C101",
            "section_code": "A",
            "instructor_id": "inst1",
            "expected_enrollment": 30,
            "allowed_meeting_patterns": ["mp1"],
            "room_requirements": []
        }
    ],
    "instructors": [
        {
            "id": "inst1",
            "rank_type": "Adjunct",
            "preferences": {"max_teaching_days": 3, "preferred_days": ["Mon"], "preferred_patterns": ["mp1"]}
        }
    ],
    "rooms": [
        {"id": "room1", "building": "B1", "capacity": 50, "features": []}
    ],
    "timeslots": [
        {"id": "ts1", "day": "Mon"}
    ],
    "meeting_patterns": [
        {"id": "mp1", "compatible_timeslot_sets": [["ts1"]]}
    ],
    "crosslist_groups": [],
    "no_overlap_groups": [],
    "blocked_times": [],
    "locked_assignments": [],
    "soft_locks": []
}

scheduling_input = SchedulingInput(test_input)
result = _solve_schedule(scheduling_input)
print(result)