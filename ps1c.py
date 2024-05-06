#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 14:02:59 2024

@author: capehart
"""


def calculate_monthly_interest(current_savings, interest_rate):
    return current_savings * interest_rate / 12


def savings_rate_ok(downpayment_needed, amount_saved):
    return downpayment_needed - 100 <= amount_saved <= downpayment_needed + 100


def calculate_amount_saved(salary, savings_rate):
    # Assumptions:
    interest_rate = 0.04
    current_savings = 0
    months_per_raise = 6
    semi_annual_raise = 0.07
    months_to_save = 36
    # convert savings rate to a decimal
    savings_rate = savings_rate / 10000

    for month in range(1, months_to_save + 1):
        monthly_salary = salary / 12
        current_savings += calculate_monthly_interest(current_savings=current_savings,
                                                      interest_rate=interest_rate)
        current_savings += monthly_salary * savings_rate
        if month % months_per_raise == 0:
            salary *= 1 + semi_annual_raise

    return current_savings


def check_block(savings_range, down_payment_needed, salary, steps=0):
    # if the list is only one element, and it's in range, return it, if it's not, fail:
    if len(savings_range) == 1:
        if savings_rate_ok(down_payment_needed, calculate_amount_saved(salary, savings_range[0])):
            return True, savings_range[0], steps
        else:
            return False, 0, 0

    # otherwise, the list is more than one element; bisect it and figure out which half to dig into
    midpoint = len(savings_range) // 2
    amount_saved = calculate_amount_saved(salary, savings_range[midpoint])
    if amount_saved < down_payment_needed:
        return check_block(savings_range[midpoint:], down_payment_needed, salary, steps + 1)
    else:
        return check_block(savings_range[:midpoint], down_payment_needed, salary, steps + 1)


def main():
    total_cost = 1000000  # 1 Meeeelion dollars
    portion_down_payment = 0.25
    down_payment_needed = total_cost * portion_down_payment

    # Input collection
    salary = int(input("Enter the starting salary: "))
    possible_percents = range(1, 10001)
    (ok, rate, sequence) = check_block(possible_percents, down_payment_needed, salary)
    if not ok:
        print("It is not possible to pay the down payment in three years.")
    else:
        print(f"Best savings rate: {rate/10000:.4f}")
        print(f"Steps in bisection search: {sequence}")


if __name__ == "__main__":
    main()
