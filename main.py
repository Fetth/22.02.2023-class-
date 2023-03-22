# Реализуйте класс «Человек». Необходимо хранить в
# полях класса: ФИО, дату рождения, контактный телефон,
# город, страну, домашний адрес. Реализуйте методы класса
# для ввода данных, вывода данных, реализуйте доступ к
# отдельным полям через методы класса.

# class Human():
#     def __init__(self, carName, year, proiz, city, carColor, Cost):
#         self.carName = carName
#         self.year = year
#         self.proiz = proiz
#         self.city = city
#         self.carColor = carColor
#         self.Cost = Cost

#     def setcityName(self):
#         self.carName = input("Введите вашу фамилию ")

#     def setregionName(self):
#         self.year = input("Введите вашу дату рождения ")
        
#     def setproiz(self):
#         self.proiz = input("Введите ваш номер телефона ")

#     def setCity(self):
#         self.city = input("Введите название вашего города ")

#     def setpostCode(self):
#         self.carColor = input("Введите название вашей страны ")

#     def setCost(self):
#         self.Cost = input("Введите ваш адрес ")
    
#     def setAll(self):
#         self.carName = input("Введите вашу фамилию ")
#         self.year = input("Введите вашу дату рождения ")
#         self.proiz = input("Введите ваш номер телефона ")
#         self.city = input("Введите название вашего города ")
#         self.carColor = input("Введите название вашей страны ")
#         self.Cost = input("Введите ваш адрес ")

#     def getcityName(self):
#         print(self.carName)

#     def getregionName(self):
#         print(self.year)

#     def getproiz(self):
#         print(self.proiz)

#     def getCity(self):
#         print(self.city)

#     def getpostCode(self):
#         print(self.carColor)

#     def getCost(self):
#         print(self.Cost)

#     def out(self):
#         print("carName =", self.carName)
#         print("year =", self.year)
#         print("proiz =", self.proiz)
#         print("city =", self.city)
#         print("carColor =", self.carColor)
#         print("Cost =", self.Cost)

# I = Human("Egor", "09.06.2007", "+799999999", "Sochi", "RF", "Centr" )
# I.out()
# I.setcityName()
# I.out()

# anon = Human(" ", " ", " ", " ", " ", " ",)
# anon.out()
# anon.setAll()
# anon.out()


# class Gorod():
#     def __init__(self, carName, year, proiz, Dvig, carColor, Cost):
#         self.carName = carName
#         self.year = year
#         self.proiz = proiz
#         self.Dvig = Dvig
#         self.carColor = carColor
#         self.Cost = Cost

#     def setcityName(self):
#         self.carName = input("Введите название вашего города ")

#     def setregionName(self):
#         self.year = input("Введите название вашего региона ")
        
#     def setproiz(self):
#         self.proiz = input("Введите название вашей страны ")

#     def setChisl(self):
#         self.Dvig = input("Введите численность населения ")

#     def setpostCode(self):
#         self.carColor = input("Введите пост код вашего города ")

#     def setCost(self):
#         self.Cost = input("Введите телефонный код города ")
    
#     def setAll(self):
#         self.carName = input("Введите название вашего города ")
#         self.year = input("Введите название вашего региона ")
#         self.proiz = input("Введите название вашей страны ")
#         self.Dvig = input("Введите численность населения ")
#         self.carColor = input("Введите пост код вашего города ")
#         self.Cost = input("Введите телефонный код города ")

#     def getcityName(self):
#         print(self.carName)

#     def getregionName(self):
#         print(self.year)

#     def getproiz(self):
#         print(self.proiz)

#     def getCity(self):
#         print(self.Dvig)

#     def getpostCode(self):
#         print(self.carColor)

#     def getCost(self):
#         print(self.Cost)

#     def out(self):
#         print("carName =", self.carName)
#         print("year =", self.year)
#         print("proiz =", self.proiz)
#         print("Dvig =", self.Dvig)
#         print("carColor =", self.carColor)
#         print("Cost =", self.Cost)

# I = Gorod("Sochi", "Krasnodar", "RF", "700000", "515151", "+7")
# I.out()
# I.setAll()
# I.out()
# I.setcityName()
# I.out()
# I.setregionName()
# I.out()
# I.setproiz()
# I.out()
# I.setChisl()
# I.out()
# I.setpostCode()
# I.out()
# I.setCost()
# I.out()

class Avtomobile():
    def __init__(self, carName, year, proiz, Dvig, carColor, Cost):
        self.carName = carName
        self.year = year
        self.proiz = proiz
        self.Dvig = Dvig
        self.carColor = carColor
        self.Cost = Cost

    def setcarName(self):
        self.carName = input("Введите название вашего города ")

    def setregionName(self):
        self.year = input("Введите название вашего региона ")
        
    def setproiz(self):
        self.proiz = input("Введите название вашей страны ")

    def setChisl(self):
        self.Dvig = input("Введите численность населения ")

    def setpostCode(self):
        self.carColor = input("Введите пост код вашего города ")

    def setCost(self):
        self.Cost = input("Введите телефонный код города ")
    
    def setAll(self):
        self.carName = input("Введите название вашего города ")
        self.year = input("Введите название вашего региона ")
        self.proiz = input("Введите название вашей страны ")
        self.Dvig = input("Введите численность населения ")
        self.carColor = input("Введите пост код вашего города ")
        self.Cost = input("Введите телефонный код города ")
 
    def getcarname(self):
        print(self.carName)

    def getregionName(self):
        print(self.year)

    def getproiz(self):
        print(self.proiz)

    def getCity(self):
        print(self.Dvig)

    def getpostCode(self):
        print(self.carColor)

    def getCost(self):
        print(self.Cost)

    def out(self):
        print("carName =", self.carName)
        print("year =", self.year)
        print("proiz =", self.proiz)
        print("Dvig =", self.Dvig)
        print("carColor =", self.carColor)
        print("Cost =", self.Cost)

I = Avtomobile("Paid", "2020", "Teals", " ", "Black", "5000000")
I.out()
I.setAll()
I.out()
I.setcarName()
I.out()
I.setregionName()
I.out()
I.setproiz()
I.out()
I.setChisl()
I.out()
I.setpostCode()
I.out()
I.setCost()
I.out()