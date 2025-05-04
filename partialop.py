from collections import defaultdict
import itertools

class Action:
    def __init__(self, name, preconds, add_effects, del_effects):
        self.name = name
        self.preconds = set(preconds)
        self.add_effects = set(add_effects)
        self.del_effects = set(del_effects)

    def __repr__(self):
        return self.name

class Plan:
    def __init__(self):
        self.actions = []
        self.ordering = []
        self.agenda = []

    def add_action(self, action):
        if action not in self.actions:
            self.actions.append(action)

    def add_ordering(self, before, after):
        self.ordering.append((before, after))

    def add_to_agenda(self, goal, action):
        self.agenda.append((goal, action))

    def __repr__(self):
        return f"Plan:\n  Actions: {self.actions}\n  Ordering: {self.ordering}"

# Define all relevant actions with concrete instantiations
def get_all_actions():
    actions = []
    blocks = ['A', 'B', 'C']

    for x, y in itertools.permutations(blocks, 2):
        actions.append(Action(
            name=f"STACK({x}, {y})",
            preconds=[f"HOLDING({x})", f"CLEAR({y})"],
            add_effects=[f"ON({x}, {y})", "HAND_EMPTY", f"CLEAR({x})"],
            del_effects=[f"HOLDING({x})", f"CLEAR({y})"]
        ))
        actions.append(Action(
            name=f"UNSTACK({x}, {y})",
            preconds=[f"ON({x}, {y})", f"CLEAR({x})", "HAND_EMPTY"],
            add_effects=[f"HOLDING({x})", f"CLEAR({y})"],
            del_effects=[f"ON({x}, {y})", "HAND_EMPTY", f"CLEAR({x})"]
        ))

    for x in blocks:
        actions.append(Action(
            name=f"PICKUP({x})",
            preconds=["HAND_EMPTY", f"CLEAR({x})", f"ONTABLE({x})"],
            add_effects=[f"HOLDING({x})"],
            del_effects=["HAND_EMPTY", f"ONTABLE({x})"]
        ))
        actions.append(Action(
            name=f"PUTDOWN({x})",
            preconds=[f"HOLDING({x})"],
            add_effects=["HAND_EMPTY", f"ONTABLE({x})", f"CLEAR({x})"],
            del_effects=[f"HOLDING({x})"]
        ))

    return actions

# POP Algorithm
def pop(initial_state, goal_state):
    actions = get_all_actions()
    plan = Plan()

    start = Action("Start", [], initial_state, [])
    finish = Action("Finish", goal_state, [], [])

    plan.add_action(start)
    plan.add_action(finish)
    plan.add_ordering(start, finish)

    for goal in goal_state:
        plan.add_to_agenda(goal, finish)

    visited = set()

    while plan.agenda:
        goal, consumer = plan.agenda.pop(0)
        if goal in start.add_effects:
            plan.add_ordering(start, consumer)
            continue

        if (goal, consumer) in visited:
            continue
        visited.add((goal, consumer))

        provider = None
        for act in actions:
            if goal in act.add_effects:
                provider = act
                break

        if provider:
            plan.add_action(provider)
            plan.add_ordering(provider, consumer)
            for p in provider.preconds:
                plan.add_to_agenda(p, provider)
        else:
            print(f"❌ No action found to satisfy goal: {goal}")
            return None

    return plan

# Main driver
if __name__ == "__main__":
    initial_state = {
        "ONTABLE(A)", "ONTABLE(B)", "ON(C, A)",
        "CLEAR(B)", "CLEAR(C)", "HAND_EMPTY"
    }

    goal_state = {"ON(A, B)", "ON(B, C)"}

    plan = pop(initial_state, goal_state)

    if plan:
        print("✅ Valid Partial Order Plan:")
        print(plan)

        print("\n🔗 Partial Ordering (Adjacency List):")
        graph = defaultdict(list)
        for before, after in plan.ordering:
            graph[before].append(after)

        for node, edges in graph.items():
            print(f"{node} -> {edges}")
    else:
        print("⚠️ No valid plan found.")
