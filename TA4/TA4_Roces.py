"""TA4: Knowledge Representation, Rule-Based Reasoning, and Case-Based Reasoning.

Use case: diagnosing a laptop that is not charging. The example facts and cases
are illustrative; update the student details and scenario as appropriate.
"""
from copy import deepcopy

# Knowledge representation: facts are grouped into three meaningful categories.
knowledge_base = {
    "power": {"outlet_working": True, "adapter_light_on": False},
    "charging": {"charging": False, "cable_damaged": True},
    "status": {"laptop_powers_on": True},
}

# Flatten facts for the rules and the case similarity function.
facts = {key: value for category in knowledge_base.values() for key, value in category.items()}


def rule_damaged_cable(current_facts):
    """Recommend replacing a cable when visible damage is reported."""
    if current_facts["cable_damaged"]:
        return "Replace the damaged charging cable."
    return None


def rule_check_outlet(current_facts):
    """Check the power source before diagnosing the laptop."""
    if not current_facts["outlet_working"]:
        return "Test another outlet or restore power to the outlet."
    return None


def rule_adapter(current_facts):
    """Suggest adapter inspection when its indicator stays off on a working outlet."""
    if current_facts["outlet_working"] and not current_facts["adapter_light_on"]:
        return "Inspect the power adapter and its connection."
    return None


def rule_charging_port(current_facts):
    """Check laptop-side charging when it runs but does not charge."""
    if current_facts["laptop_powers_on"] and not current_facts["charging"]:
        return "Inspect the laptop charging port and battery."
    return None


RULES = [rule_damaged_cable, rule_check_outlet, rule_adapter, rule_charging_port]


def run_inference_engine(current_facts, rules=RULES):
    """Apply every rule to working facts and return all inferred actions."""
    actions = []
    for rule in rules:
        action = rule(current_facts)
        if action is not None:
            actions.append(action)
    return actions


# Three prior cases. Each case has problem features and an associated solution.
case_base = [
    {
        "problem": {"outlet_working": True, "adapter_light_on": False,
                    "charging": False, "cable_damaged": False,
                    "laptop_powers_on": True},
        "solution": "Inspect the power adapter and its connection.",
    },
    {
        "problem": {"outlet_working": False, "adapter_light_on": False,
                    "charging": False, "cable_damaged": False,
                    "laptop_powers_on": True},
        "solution": "Test another outlet or restore power to the outlet.",
    },
    {
        "problem": {"outlet_working": True, "adapter_light_on": False,
                    "charging": False, "cable_damaged": False,
                    "laptop_powers_on": False},
        "solution": "Inspect the power adapter and its connection.",
    },
]


def similarity(problem_a, problem_b):
    """Return the fraction of matching Boolean features (range 0.0 to 1.0)."""
    features = set(problem_a) | set(problem_b)
    if not features:
        return 0.0
    matches = sum(problem_a.get(feature) == problem_b.get(feature) for feature in features)
    return matches / len(features)


def retrieve_most_similar(new_problem, cases):
    """Retrieve the highest-scoring prior case and its similarity score."""
    if not cases:
        return None, 0.0
    ranked = [(similarity(new_problem, case["problem"]), case) for case in cases]
    return max(ranked, key=lambda item: item[0])


def revise_solution(proposed_solution, revised_solution=None):
    """Reuse a proposed answer; permit a manual replacement when supplied."""
    return revised_solution.strip() if revised_solution and revised_solution.strip() else proposed_solution


def retain_case(new_problem, final_solution, cases):
    """Add the resolved problem and solution to the case base for this run."""
    cases.append({"problem": deepcopy(new_problem), "solution": final_solution})


def run_cbr(new_problem, cases):
    """Run Retrieve, Reuse, Revise, and Retain for one new problem."""
    score, retrieved_case = retrieve_most_similar(new_problem, cases)  # Retrieve
    if retrieved_case is None:
        reused_solution = "No prior solution found; perform a new diagnosis."
    else:
        reused_solution = retrieved_case["solution"]  # Reuse
    final_solution = revise_solution(reused_solution)  # Revise (unchanged by default)
    retain_case(new_problem, final_solution, cases)  # Retain
    return score, retrieved_case, final_solution


def main():
    print("KNOWLEDGE BASE")
    for category, category_facts in knowledge_base.items():
        print(f"{category.title()}: {category_facts}")

    print("\nRULE-BASED REASONING ACTIONS")
    for action in run_inference_engine(facts):
        print(f"- {action}")

    print("\nCASE-BASED REASONING")
    score, case, solution = run_cbr(facts, case_base)
    if case:
        print(f"Retrieved case similarity: {score:.0%}")
        print(f"Reused solution: {case['solution']}")
    else:
        print("Retrieved case: none")
    print(f"Revised solution: {solution}")
    print(f"Retained new case. Case base now contains {len(case_base)} cases.")


if __name__ == "__main__":
    main()
