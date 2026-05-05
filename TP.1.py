# -*- coding: utf-8 -*-

class SystemeExpert:
    """
    كلاس نظام خبير - يقوم بإدارة الحقائق والقواعد وتطبيق الاستدلال الأمامي
    """
    
    # ============================================================
    # 1. دالة البناء (Constructor)
    # ============================================================
    
    def __init__(self):
        """
        دالة البناء: تهيئة قائمتين فارغتين للحقائق والقواعد
        """
        self.faits = []      # قائمة الحقائق المعروفة (تبدأ فارغة)
        self.regles = []     # قائمة القواعد (تبدأ فارغة)
        self._historique = [] # قائمة خاصة لتخزين تاريخ القواعد المطبقة (للـ trace)
    
    # ============================================================
    # 2. إدارة الحقائق (Gestion des faits)
    # ============================================================
    
    def afficheFaits(self):
        """
        عرض جميع الحقائق الموجودة في قاعدة المعرفة
        """
        if not self.faits:
            print("لا توجد حقائق في القاعدة.")
        else:
            print("الحقائق المعروفة:", self.faits)
    
    def ajouteFait(self, fait):
        """
        إضافة حقيقة جديدة إذا لم تكن موجودة مسبقاً
        """
        if fait not in self.faits:
            self.faits.append(fait)
            print(f"تمت إضافة الحقيقة: {fait}")
            return True
        print(f"الحقيقة '{fait}' موجودة بالفعل.")
        return False
    
    def initDBs(self):
        """
        تفريغ قاعدة الحقائق وقاعدة القواعد (حذف كل المحتويات)
        """
        self.faits = []
        self.regles = []
        self._historique = []
        print("تم تفريغ القاعدتين بنجاح.")
    
    # ============================================================
    # 3. إدارة القواعد (Gestion des règles)
    # ============================================================
    
    def afficheRegles(self):
        """
        عرض جميع القواعد مع أرقامها
        """
        if not self.regles:
            print("لا توجد قواعد في القاعدة.")
        else:
            print("قواعد النظام:")
            for i, regle in enumerate(self.regles, 1):
                print(f"  R{i}: إذا {regle[0]} فإن {regle[1]}")
    
    def ajouteRegle(self, conditions, consequence):
        """
        إضافة قاعدة جديدة
        conditions: قائمة الشروط (مثال: ['مطر', 'بارد'])
        consequence: النتيجة (مثال: 'لا تخرج')
        """
        regle = [conditions, consequence]
        self.regles.append(regle)
        print(f"تمت إضافة قاعدة: إذا {conditions} فإن {consequence}")
    
    def conditionsRegle(self, regle):
        """
        إرجاع قائمة شروط قاعدة معينة
        """
        return regle[0]
    
    def consequenceRegle(self, regle):
        """
        إرجاع نتيجة قاعدة معينة
        """
        return regle[1]
    
    def satisfaitUneCondition(self, regle, le_fait):
        """
        التحقق مما إذا كانت حقيقة معينة موجودة ضمن شروط القاعدة
        """
        conditions = self.conditionsRegle(regle)
        return le_fait in conditions
    
    def satisfaitConditions(self, regle):
        """
        التحقق مما إذا كانت جميع شروط القاعدة موجودة في الحقائق المعروفة
        """
        conditions = self.conditionsRegle(regle)
        for condition in conditions:
            if condition not in self.faits:
                return False
        return True
    
    # ============================================================
    # 4. الاستدلال الأمامي (Chaînage avant / Forward Chaining)
    # ============================================================
    
    def chainageAvantSimple(self, faitsInitiaux, regles=None):
        """
        تنفيذ خوارزمية الاستدلال الأمامي
        - faitsInitiaux: قائمة الحقائق الأولية
        - regles: قائمة القواعد (إذا لم تُعط، نستخدم self.regles)
        """
        # تهيئة الحقائق
        self.faits = faitsInitiaux.copy()
        self._historique = []
        
        # تحديد القواعد المراد استخدامها
        if regles is None:
            regles = self.regles
        
        cycle = 1                  # رقم الدورة الحالية
        nouveauFait = True         # هل تمت إضافة حقيقة جديدة؟
        
        print("\n" + "=" * 50)
        print("بداية الاستدلال الأمامي (Chaînage avant)")
        print("=" * 50)
        print(f"الحقائق الأولية: {self.faits}\n")
        
        while nouveauFait:
            nouveauFait = False
            print(f"--- الدورة {cycle} ---")
            
            # نمر على كل قاعدة
            for i, regle in enumerate(regles, 1):
                # نتحقق إذا كانت جميع شروط القاعدة موجودة
                if self.satisfaitConditions(regle):
                    consequence = self.consequenceRegle(regle)
                    
                    # إذا كانت النتيجة جديدة (غير موجودة)
                    if consequence not in self.faits:
                        print(f"  تطبيق القاعدة R{i}: {self.conditionsRegle(regle)} -> {consequence}")
                        self.faits.append(consequence)
                        nouveauFait = True
                        
                        # تسجيل في التاريخ (للاستخدام في trace)
                        self._historique.append({
                            'cycle': cycle,
                            'rule_num': i,
                            'conditions': self.conditionsRegle(regle).copy(),
                            'new_fact': consequence
                        })
            
            cycle += 1
            
            # أمان: منع الحلقات اللانهائية
            if cycle > 20:
                print("تم التوقف: تم الوصول إلى الحد الأقصى للدورات (20)")
                break
        
        print(f"\nالحقائق النهائية: {self.faits}")
        return self.faits
    
    # ============================================================
    # 5. دالة التتبع (Trace)
    # ============================================================
    
    def trace(self):
        """
        عرض التاريخ المفصل للقواعد التي تم تفعيلها
        يُظهر:
        - رقم الدورة
        - القاعدة التي تم تفعيلها
        - الحقيقة الجديدة التي تم استنتاجها
        """
        if not self._historique:
            print("لا يوجد تاريخ. قم بتنفيذ chainageAvantSimple أولاً.")
            return
        
        print("\n" + "=" * 50)
        print("تاريخ الاستدلال (Trace)")
        print("=" * 50)
        
        for step in self._historique:
            print(f"الدورة {step['cycle']}: تم تفعيل القاعدة R{step['rule_num']}")
            print(f"         الشروط: {step['conditions']}")
            print(f"         الحقيقة الجديدة المستنتجة: {step['new_fact']}")
            print("-" * 40)


# ============================================================
# مثال تشغيلي (اختبار النظام)
# ============================================================

if __name__ == "__main__":
    
    print("=" * 60)
    print("إنشاء نظام خبير جديد")
    print("=" * 60)
    
    # إنشاء كائن من الكلاس
    expert = SystemeExpert()
    
    # ===== إضافة القواعد =====
    print("\n--- إضافة القواعد ---")
    expert.ajouteRegle(["rain"], "take_umbrella")
    # قاعدة: إذا كان مطر ← خذ مظلة
    
    expert.ajouteRegle(["cold"], "wear_jacket")
    # قاعدة: إذا كان بارد ← البس معطف
    
    expert.ajouteRegle(["take_umbrella", "wear_jacket"], "ready_to_go_out")
    # قاعدة: إذا أخذت مظلة ولبست معطف ← مستعد للخروج
    
    expert.ajouteRegle(["snow"], "stay_home")
    # قاعدة: إذا كان ثلج ← ابق في المنزل
    
    # ===== عرض القواعد =====
    print("\n--- عرض القواعد ---")
    expert.afficheRegles()
    
    # ===== تنفيذ الاستدلال الأمامي =====
    print("\n--- تنفيذ الاستدلال الأمامي ---")
    expert.chainageAvantSimple(["rain", "cold"])
    # نبدأ بحقيقتين: مطر و بارد
    
    # ===== عرض التتبع =====
    expert.trace()
    
    # ===== عرض الحقائق النهائية =====
    print("\n--- الحقائق النهائية ---")
    expert.afficheFaits()
    
    # ===== تجربة تفريغ القاعدتين =====
    print("\n--- تجربة تفريغ القاعدتين ---")
    expert.initDBs()
    expert.afficheFaits()
    expert.afficheRegles()
