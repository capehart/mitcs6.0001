#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 14:02:59 2024

@author: capehart
"""


def calculate_monthly_interest(current_savings, interest_rate):
    return current_savings * interest_rate / 12

# Assumptions:
interest_rate = 0.04
current_savings = 0
portion_down_payment = 0.25
months_per_year = 12

# Input collection
salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal (eg '.10'): "))
total_cost = int(input("Enter the cost of your dream home: "))
savings_required = total_cost * portion_down_payment
monthly_salary = salary/months_per_year

months_elapsed = 0

while current_savings <= savings_required:
    months_elapsed += 1
    current_savings += calculate_monthly_interest(current_savings=current_savings,
                                                  interest_rate=interest_rate)
    current_savings += monthly_salary * portion_saved

(years,months) = divmod(months_elapsed, months_per_year)
print(f"After {years} years and {months} months ({months_elapsed} total months), you will have saved ${current_savings:,.2f} which is enough to cover a ${savings_required:,.2f} down payment.")
