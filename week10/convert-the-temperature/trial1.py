class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        temp=[]
        kelvin=celsius+273.15
        fahrenheit=(celsius*1.8)+32
        temp+=[kelvin]+[fahrenheit]
        return temp
