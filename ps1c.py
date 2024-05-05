#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 14:02:59 2024

@author: capehart
"""


def calculate_monthly_interest(current_savings, interest_rate):
    return current_savings * interest_rate / 12

def calculate_amount_saved(salary, savings_rate):
    # Assumptions:
    interest_rate = 0.04
    current_savings = 0
    months_per_raise = 6
    semi_annual_raise = 0.07
    months_to_save = 36
    
    for month in range(1, months_to_save+1):
        monthly_salary = salary/12
        # print(f"Interest: {(calculate_monthly_interest(current_savings=current_savings, interest_rate=interest_rate)):,.2f}")
        current_savings += calculate_monthly_interest(current_savings=current_savings,
                                                  interest_rate=interest_rate)
        # print(f"Amount saved from salary: {(monthly_salary * savings_rate):,.2f}")
        current_savings += monthly_salary * savings_rate
        if month % months_per_raise == 0:       
            salary *= 1 + semi_annual_raise
            # print(f"New salary is ${salary:,.2f}")
        # print(f"month: {month}: savings:{current_savings:.2f}")

    return current_savings

def checkblock(savings_range):
    # stop condition:
    pass

total_cost = 1000000  # 1 Meeeelion dolars
portion_down_payment = 0.25
downpayment_needed = total_cost * portion_down_payment

# Input collection
salary = int(input("Enter the starting salary: "))
possible_percents = range(1,10001)
for pct in possible_percents:
    savings_rate = pct/10000
    # print(f"Percent: {(savings_rate * 100):.2f}")
    savings_managed = calculate_amount_saved(salary=salary, savings_rate=savings_rate)
    # print(f"{(downpayment_needed - 100):,.2f} <= {savings_managed:,.2f} <= {(downpayment_needed + 100):,.2f}")
    if (downpayment_needed - 100  <= savings_managed <= downpayment_needed + 100):
        print(f"Percent Savings Required: {savings_rate}")
        break




