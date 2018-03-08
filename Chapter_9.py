# /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "0LIN1ISA"
# Date:2018/3/8 18:57

# 第9章 类

# 创建Dog类
from pip._vendor.six import class_types


class Dog():
    """一次模拟小狗的简单尝试"""

    def __init__(self, name, age):
        """初始化name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """模拟小狗被命令打滚"""
        print(self.name.title() + " rolled over!")


mydog = Dog('jak', 21)
mydog.sit()
mydog.roll_over()


# Car类
class Car():
    """一次简单模拟汽车的类"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        # 给属性指定默认值
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name


mycar = Car('audi', 'a4', 2016)
print(mycar.get_descriptive_name())


class Battery():
    """一次模拟电动车电瓶的简单尝试"""

    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("this car has a" + str(self.battery_size) + "-kWh battery.")


# 继承
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def get_descriptive_name(self):
        return super().get_descriptive_name()


my_electric_car = ElectricCar('audi', 'a4', 2016)
print(my_electric_car.battery.battery_size)

