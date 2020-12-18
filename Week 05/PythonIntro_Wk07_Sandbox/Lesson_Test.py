class Person:
  countPerson = 0

  def _init_(self, fname, lname):
    self.fname = fname
    self.lname = lname
    Person.countPerson += 1

    def myName(self):
      return self.fname + " " + self.lname


pat = Person("Patrick", "Mansour")
