class Convert:
    def __init__(self, number):
        self.number = number
        self.tensValue = 10
        self.hundredsValue = 100

    def convertNumberIntoWord(self):
        if(self.number < 10):
            return self.unit(self.number)
        elif(self.number < 20):
            return self.exceptions(self.number)
        elif(self.number < 100):
            return self.tens(self.number)
        elif(self.number < 1000):
            return self.hundreds(self.number)

    def unit(self, number):
        units = ("Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine")

        return units[number]
    
    def exceptions(self, number):
        exceptions = ("Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen")

        exceptionsIndex = int(number - self.tensValue)

        return exceptions[exceptionsIndex]

    def tens(self, number):
        tens = ("Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", 
        "Eighty", "Ninety")

        tensIndex = int(number / 10 - 2)
        unitIndex = int(number % 10)

        if(number % 10 == 0):
            return tens[tensIndex] 
        else: 
            return str(tens[tensIndex]) + " and " + str(self.unit(unitIndex))   

    def hundreds(self, number):
        hundreds = ("One Hundred", "Two Hundred", "Three Hundred", "Four Hundred", "Five Hundred", "Six Hundred", "Seven Hundred", "Eigth Hundred", "Nine Hundred") 

        hundredsIndex = int(number / 100 - 1)
        tensIndex = int(number - (int(number / 100) * 100) + 1)
        unitIndex = number - (int(number / 100) * 100)
        exceptionIndex = unitIndex - 10

        if(number % 100 == 0):
            return hundreds[hundredsIndex]
        elif(unitIndex < 10):
            return str(hundreds[hundredsIndex]) + " and " + str(self.unit(unitIndex))
        elif(unitIndex > 9 and unitIndex < 20):
            return hundreds[hundredsIndex] + " and " + self.exceptions(exceptionIndex)
        elif(number % 10 == 0):
            return str(hundreds[hundredsIndex]) + " and " + str(self.tens(tensIndex - 1))
        else:
            return str(hundreds[hundredsIndex]) + " and " + str(self.tens(int(unitIndex / 10) * 10)) + " " + str(self.unit(int(unitIndex / 10)))