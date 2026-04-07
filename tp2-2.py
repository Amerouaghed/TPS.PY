
# ============================================================
# التمرين 1 و 2: Dictionary + Forward Chaining
# ============================================================


# تعريف الحقائق
facts1 = ["rain", "cold"]

# تعريف القواعد باستخدام Dictionary
rules1 = [
    {"if": ["rain"], "then": "take_umbrella"},
    {"if": ["cold"], "then": "wear_jacket"},
    {"if": ["rain", "cold"], "then": "stay_home"}
]

# دالة الاستدلال الأمامي
def forward_chaining_dict(facts, rules):
    known_facts = facts.copy()           # ننسخ الحقائق المعروفة
    new_fact_added = True                 # متغير للتحقق من وجود حقائق جديدة
    
    while new_fact_added:                # نستمر طالما هناك حقائق جديدة
        new_fact_added = False            # نفترض في البداية أنه لن نضيف شيئاً
        
        for rule in rules:               # نمر على كل قاعدة
            all_conditions_met = True     # نفترض أن جميع الشروط متحققة
            
            for condition in rule["if"]: # نفحص كل شرط
                if condition not in known_facts:
                    all_conditions_met = False
                    break                 # نخرج من الحلقة، لا داعي لفحص باقي الشروط
            
            if all_conditions_met and rule["then"] not in known_facts:
                print(f"Applied rule: {rule['if']} -> {rule['then']}")
                known_facts.append(rule["then"])  # نضيف النتيجة الجديدة
                new_fact_added = True              # يوجد حقيقة جديدة
    
    return known_facts

# تشغيل التمرين 1 و 2
result1 = forward_chaining_dict(facts1, rules1)
print(f"\nFinal facts: {result1}\n")


# ============================================================
# التمرين 3 و 4: Tuple + Forward Chaining
# ============================================================


# تعريف الحقائق
facts2 = ["rain", "cold"]

# تعريف القواعد باستخدام Tuple
rules2 = (
    (["rain"], "take_umbrella"),
    (["cold"], "wear_jacket"),
    (["rain", "cold"], "stay_home")
)

# دالة الاستدلال الأمامي مع Tuple
def forward_chaining_tuple(facts, rules):
    known_facts = facts.copy()           # ننسخ الحقائق المعروفة
    new_fact_added = True                 # متغير للتحقق من وجود حقائق جديدة
    
    while new_fact_added:                # نستمر طالما هناك حقائق جديدة
        new_fact_added = False            # نفترض في البداية أنه لن نضيف شيئاً
        
        for conditions, conclusion in rules:  # نمر على كل قاعدة
            all_conditions_met = True     # نفترض أن جميع الشروط متحققة
            
            for condition in conditions: # نفحص كل شرط
                if condition not in known_facts:
                    all_conditions_met = False
                    break                 # نخرج من الحلقة
            
            if all_conditions_met and conclusion not in known_facts:
                print(f"Applied rule: {conditions} -> {conclusion}")
                known_facts.append(conclusion)    # نضيف النتيجة
                new_fact_added = True              # يوجد حقيقة جديدة
    
    return known_facts

# تشغيل التمرين 3 و 4
result2 = forward_chaining_tuple(facts2, rules2)
print(f"\nFinal facts: {result2}\n")


# ============================================================
# التمرين 5أ: Backward Chaining مع Dictionary
# ============================================================


# تعريف الحقائق
facts3 = ["rain", "cold"]

# تعريف القواعد
rules3 = [
    {"if": ["rain"], "then": "take_umbrella"},
    {"if": ["cold"], "then": "wear_jacket"},
    {"if": ["take_umbrella", "wear_jacket"], "then": "ready_to_go"}
]

# دالة الاستدلال الخلفي مع Dictionary
def backward_chaining_dict(goal, facts, rules, visited=None):
    # visited: قائمة الأهداف التي تم فحصها (لمنع الحلقات اللانهائية)
    
    if visited is None:                  # إذا كانت أول مرة
        visited = []
        print(f"\nTrying to prove: {goal}")
    
    if goal in facts:                    # الحالة 1: الهدف موجود كحقيقة
        print(f"  ✓ '{goal}' is a known fact")
        return True
    
    if goal in visited:                  # الحالة 2: لمنع الحلقات اللانهائية
        print(f"  ✗ '{goal}' already checked (cycle)")
        return False
    
    visited.append(goal)                 # نضيف الهدف إلى القائمة
    
    for rule in rules:                   # نبحث عن قواعد تنتج هذا الهدف
        if rule["then"] == goal:
            print(f"  Trying rule: {rule['if']} -> {goal}")
            
            all_conditions_true = True
            
            for condition in rule["if"]: # نفحص كل شرط
                if not backward_chaining_dict(condition, facts, rules, visited.copy()):
                    all_conditions_true = False
                    break                 # إذا فشل شرط، نخرج من الحلقة
            
            if all_conditions_true:
                print(f"  ✓ Successfully proved '{goal}'")
                return True
    
    print(f"  ✗ Failed to prove '{goal}'")
    return False

# تشغيل التمرين 5أ
result3 = backward_chaining_dict("ready_to_go", facts3, rules3)
print(f"\nFinal result: {result3}\n")


# ============================================================
# التمرين 5ب: Backward Chaining مع Tuple
# ============================================================


# تعريف الحقائق
facts4 = ["rain", "cold"]

# تعريف القواعد باستخدام Tuple
rules4 = (
    (["rain"], "take_umbrella"),
    (["cold"], "wear_jacket"),
    (["take_umbrella", "wear_jacket"], "ready_to_go")
)

# دالة الاستدلال الخلفي مع Tuple
def backward_chaining_tuple(goal, facts, rules, visited=None):
    # visited: قائمة الأهداف التي تم فحصها (لمنع الحلقات اللانهائية)
    
    if visited is None:                  # إذا كانت أول مرة
        visited = []
        print(f"\nTrying to prove: {goal}")
    
    if goal in facts:                    # الحالة 1: الهدف موجود كحقيقة
        print(f"  ✓ '{goal}' is a known fact")
        return True
    
    if goal in visited:                  # الحالة 2: لمنع الحلقات اللانهائية
        print(f"  ✗ '{goal}' already checked (cycle)")
        return False
    
    visited.append(goal)                 # نضيف الهدف إلى القائمة
    
    for conditions, conclusion in rules: # نبحث عن قواعد تنتج هذا الهدف
        if conclusion == goal:
            print(f"  Trying rule: {conditions} -> {conclusion}")
            
            all_conditions_true = True
            
            for condition in conditions: # نفحص كل شرط
                if not backward_chaining_tuple(condition, facts, rules, visited.copy()):
                    all_conditions_true = False
                    break                 # إذا فشل شرط، نخرج من الحلقة
            
            if all_conditions_true:
                print(f"  ✓ Successfully proved '{goal}'")
                return True
    
    print(f"  ✗ Failed to prove '{goal}'")
    return False

# تشغيل التمرين 5ب
result4 = backward_chaining_tuple("ready_to_go", facts4, rules4)
print(f"\nFinal result: {result4}")


# ============================================================
# ملخص جميع النتائج في النهاية
# ============================================================

print("\n" + "=" * 60)
print("SUMMARY OF ALL RESULTS")
print("=" * 60)

print(f"\nExercise 1 & 2 (Dict + Forward): {result1}")
print(f"Exercise 3 & 4 (Tuple + Forward): {result2}")
print(f"Exercise 5a (Dict + Backward): {result3}")
print(f"Exercise 5b (Tuple + Backward): {result4}")