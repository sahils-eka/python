class India:
    def about(self):
        print("This is India")


class Japan:
    def about(self):
        print("This is Japan")


ind = India()
jpn = Japan()

for i in (ind, jpn):
    i.about()
