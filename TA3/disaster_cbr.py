import json
from pathlib import Path

CASE_FILE = Path("cases.json")

# Case representation: previous disaster cases
cases = [
    {
        "id": "C001",
        "problem": {
            "type": "flood",
            "severity": 4,
            "population": 12000,
            "rainfall": 260,
            "road": "limited"
        },
        "solution": {
            "site": "North High School",
            "teams": 4,
            "trucks": 2,
            "action": "Evacuate low-lying households first"
        }
    },
    {
        "id": "C002",
        "problem": {
            "type": "flood",
            "severity": 5,
            "population": 25000,
            "rainfall": 420,
            "road": "blocked"
        },
        "solution": {
            "site": "East Sports Complex",
            "teams": 8,
            "trucks": 4,
            "action": "Evacuate all zones immediately"
        }
    },
    {
        "id": "C003",
        "problem": {
            "type": "earthquake",
            "severity": 4,
            "population": 18000,
            "rainfall": 40,
            "road": "limited"
        },
        "solution": {
            "site": "Central University Gym",
            "teams": 7,
            "trucks": 3,
            "action": "Search damaged buildings and assist injured residents"
        }
    }
]

# New disaster problem
new_case = {
    "type": "flood",
    "severity": 5,
    "population": 22000,
    "rainfall": 390,
    "road": "blocked"
}


# Similarity assessment
def similarity(query, case):
    score = 0

    if query["type"] == case["type"]:
        score += 0.30

    score += max(
        0,
        1 - abs(query["severity"] - case["severity"]) / 4
    ) * 0.20

    score += max(
        0,
        1 - abs(query["population"] - case["population"]) / 30000
    ) * 0.20

    score += max(
        0,
        1 - abs(query["rainfall"] - case["rainfall"]) / 500
    ) * 0.20

    if query["road"] == case["road"]:
        score += 0.10

    return score


# Display the new problem
print("NEW DISASTER PROBLEM")
print("--------------------")
print("Disaster type:", new_case["type"])
print("Severity:", new_case["severity"])
print("Affected population:", new_case["population"])
print("Rainfall:", new_case["rainfall"], "mm")
print("Road access:", new_case["road"])

# Retrieve the most similar case
ranked_cases = sorted(
    cases,
    key=lambda case: similarity(new_case, case["problem"]),
    reverse=True
)

retrieved_case = ranked_cases[0]
score = similarity(new_case, retrieved_case["problem"])

# Adapt the retrieved solution
adapted_solution = retrieved_case["solution"].copy()

if new_case["population"] > 20000:
    adapted_solution["teams"] += 2
    adapted_solution["trucks"] += 1

if new_case["severity"] >= 5:
    adapted_solution["action"] = (
        "Begin full emergency evacuation immediately"
    )

if new_case["road"] == "blocked":
    adapted_solution["action"] += (
        " using boats, helicopters, or alternate routes"
    )

# Display the CBR result
print("\nCASE-BASED REASONING RESULT")
print("---------------------------")
print("Retrieved case:", retrieved_case["id"])
print("Similarity score:", round(score, 3))

print("\nADAPTED SOLUTION")
print("----------------")
print("Evacuation site:", adapted_solution["site"])
print("Rescue teams:", adapted_solution["teams"])
print("Water trucks:", adapted_solution["trucks"])
print("Recommended action:", adapted_solution["action"])

# Retain the new case
new_case_record = {
    "id": "C004",
    "problem": new_case,
    "solution": adapted_solution,
    "outcome": "Residents were evacuated safely."
}

cases.append(new_case_record)

with CASE_FILE.open("w", encoding="utf-8") as file:
    json.dump(cases, file, indent=4)

# Display learning result
print("\nLEARNING AND RETENTION")
print("----------------------")
print("New case retained successfully.")

print("\nUPDATED CASE BASE")
print("-----------------")
for case in cases:
    print(case["id"], "-", case["problem"]["type"])

print("Total cases in case base:", len(cases))