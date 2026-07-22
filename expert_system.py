# -----------------------------------------
# Rule-Based Expert System using Forward Chaining
# -----------------------------------------

print("=" * 50)
print("      RULE-BASED EXPERT SYSTEM")
print("=" * 50)

# ------------------------------
# Take user input (Facts)
# ------------------------------

facts = set()

fever = input("Do you have fever? (yes/no): ").lower()
cough = input("Do you have cough? (yes/no): ").lower()
body_pain = input("Do you have body pain? (yes/no): ").lower()
headache = input("Do you have headache? (yes/no): ").lower()
sore_throat = input("Do you have sore throat? (yes/no): ").lower()

if fever == "yes":
    facts.add("fever")

if cough == "yes":
    facts.add("cough")

if body_pain == "yes":
    facts.add("body_pain")

if headache == "yes":
    facts.add("headache")

if sore_throat == "yes":
    facts.add("sore_throat")

# ------------------------------
# Rule Base
# ------------------------------

rules = [

    {
        "conditions": {"fever", "cough"},
        "conclusion": "flu"
    },

    {
        "conditions": {"fever", "headache"},
        "conclusion": "viral_fever"
    },

    {
        "conditions": {"cough", "sore_throat"},
        "conclusion": "cold"
    },

    {
        "conditions": {"flu"},
        "conclusion": "visit_doctor"
    },

    {
        "conditions": {"viral_fever"},
        "conclusion": "take_rest"
    },

    {
        "conditions": {"cold"},
        "conclusion": "drink_warm_water"
    }

]

# ------------------------------
# Forward Chaining
# ------------------------------

reasoning = []

new_fact_added = True

while new_fact_added:

    new_fact_added = False

    for rule in rules:

        if rule["conditions"].issubset(facts):

            if rule["conclusion"] not in facts:

                facts.add(rule["conclusion"])

                reasoning.append(
                    f"{rule['conditions']}  --->  {rule['conclusion']}"
                )

                new_fact_added = True

# ------------------------------
# Display Result
# ------------------------------

print("\n")
print("=" * 50)
print("RESULT")
print("=" * 50)

if "flu" in facts:
    print("Possible Disease : Flu")

elif "viral_fever" in facts:
    print("Possible Disease : Viral Fever")

elif "cold" in facts:
    print("Possible Disease : Common Cold")

else:
    print("No disease identified.")

print("\nRecommendations")

if "visit_doctor" in facts:
    print("- Visit Doctor")

if "take_rest" in facts:
    print("- Take Proper Rest")

if "drink_warm_water" in facts:
    print("- Drink Warm Water")

print("\nReasoning Path")

if len(reasoning) == 0:
    print("No inference generated.")

else:
    for step in reasoning:
        print(step)

print("\nFinal Facts")

for fact in facts:
    print("-", fact)

print("\nThank You for using the Expert System.")