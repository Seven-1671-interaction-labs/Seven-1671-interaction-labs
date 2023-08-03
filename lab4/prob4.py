class ComEnStudent:
    def __init__(self,name,courses):
        self.name=name
        self.courses=courses

    def __str__(self):
        return f"{self.name} has taken these courses: {self.courses}"

    def take_courses(self,*new_courses):
        self.courses.extend(new_courses)


class CoEStudent(ComEnStudent):
    def __init__(self,name,courses):
        super().__init__(name,courses)

    def __init__(self,name,courses):
        super().__init__(name,courses)

    def take_courses(self,*new_courses):
        super().take_courses(*new_courses)


class DMEStudent(ComEnStudent):
    def __init__(self, name,courses):
        super().__init__(name,courses)

    def __str__(self):
        return f"{super().__str__()} specialized in creating content type: {self.content_type}"

    def make_content_type(self,content_type):
        self.content_type=content_type
        
if __name__=="__main__":
    com_student = []
    manee = CoEStudent("Manee" , ["EN813701"])
    mana = DMEStudent("Manee" , ["EN842004"])  
    manee.take_courses("EN813702", "EN811301", "EN811302")
    mana.take_courses ("EN842005")
    mana.make_content_type("Infographics")
    com_student.append(manee)
    com_student.append(mana)
    for com_student in com_student:
        com_student.take_courses("SC401206")
        print(com_student)