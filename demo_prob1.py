class student :
    
    def __init__(self, name, courses_id):
        self.name = name
        self.courses_id = courses_id
        
    def describe(self):
        print(f"{self.name} registered courses {self.courses_id}")
   
if __name__ == '__main__':
    manee = student("Manee", "842004")
    mana = student("Mana", "842004", "842005", "813701")
    chujai = student("Chujai", "842004", "842005")
    # print(f"{manee.name} registered courses {manee.course_ids}")
    manee.describe()
    print(f"{mana.name} registered courses {mana.courses_id}")
    print(f"{chujai.name} registered courses {chujai.courses_id}")