# Lets you postpone the object creation unless its actually required


class College:
    """ Resouce Intensive """
    def study_in_college(self):
        print("Studying in college")


class CollegeProxy:
    """ Relatively less """
    def __init__(self):
        self.dueBalance = 1000
        self.college = None

    def study_in_college(self):
        print("> Proxy in action. Checking if the student can study or not.")
        if self.dueBalance < 500:
            print("You can study")
            self.college = College()
            self.college.study_in_college()
        else:
            print(
                "Sorry, can't let you go to college with that much due balance"
            )


collegeProxy = CollegeProxy()
collegeProxy.study_in_college()
collegeProxy.dueBalance = 100
collegeProxy.study_in_college()
