# # # # EMPLOYEE_TYPE_FULL_TIME = 'full-time'
# # # # EMPLOYEE_TYPE_PART_TIME = 'part-time'
# # # # EMPLOYEE_HOLIDAY_BANK = 'bank-hol'
# # # # EMPLOYEE_SLEEP = 'normal-sleep'
# # # # EMPLOYEE_EXTRA_SLEEP = 'extra-sleep'
# # # # EMPLOYEE_WAKE_NIGHT = 'wake-night'

# # # # FULL_TIME_HOURS = 150
# # # # FULL_TIME_HOURLY_RATE = 11.25
# # # # FULL_TIME_OVERTIME_RATE = 13.75
# # # # FULL_TIME_BANK_HOLIDAY_RATE = 23.5
# # # # FULL_TIME_WAKING_NIGHT_RATE = 111.625
# # # # FULL_TIME_SLEEP_RATE = 30
# # # # FULL_TIME_EXTRA_SLEEP_RATE = 60

# # # # PART_TIME_HOURS = 80
# # # # PART_TIME_HOURLY_RATE = 11.75
# # # # PART_TIME_OVERTIME_RATE = 13.75
# # # # PART_TIME_BANK_HOLIDAY_RATE = 23.5
# # # # PART_TIME_WAKING_NIGHT_RATE = 11.75
# # # # PART_TIME_SLEEP_RATE = 30
# # # # PART_TIME_WAKING_NIGHT_RATE = 111.625
# # # # PART_TIME_EXTRA_SLEEP_RATE = 60

# # # # employee_type = input("Enter your employee type (full-time or part-time?): ")

# # # # regular_pay = 0
# # # # overtime_pay = 0
# # # # bh_pay = 0
# # # # N_worked = 0
# # # # sleeps_times = 0
# # # # extra_sleep_times = 0
# # # # wake_nights = 0


# # # # if employee_type == EMPLOYEE_TYPE_FULL_TIME:
# # # #     hours_worked = float(input("Enter the number of hours worked this month: "))

# # # #     if hours_worked <= FULL_TIME_HOURS:
# # # #         regular_pay = FULL_TIME_HOURLY_RATE * hours_worked

# # # #     elif hours_worked > FULL_TIME_HOURS:
# # # #         overtime_hours = hours_worked - FULL_TIME_HOURS
# # # #         overtime_pay = FULL_TIME_OVERTIME_RATE * overtime_hours
# # # #         regular_hours = hours_worked - overtime_hours
# # # #         regular_pay = FULL_TIME_HOURLY_RATE * regular_hours+overtime_pay
# # # #         N_worked = overtime_pay


# # # #     employee_bank = input("Enter your holiday (bank-hol or no-bank-hol?): ").lower()

# # # #     if employee_bank == EMPLOYEE_HOLIDAY_BANK:
# # # #         holiday_hour = float(input("Enter the holiday-hour: "))
# # # #         bh_pay = holiday_hour * FULL_TIME_BANK_HOLIDAY_RATE
# # # #         regular_pay += bh_pay
        

# # # #     sleep = input("Did you do a normal-sleep or no-sleep?: ").lower()

# # # #     if sleep == EMPLOYEE_SLEEP:
# # # #         sleep_times = float(input("How many sleeps did you do?: "))
# # # #         sleeps_times = sleep_times * FULL_TIME_SLEEP_RATE
# # # #         regular_pay += sleeps_times

# # # #     extra_sleep = input("Did you do an extra-sleep or no-extra-sleep?: ").lower()

# # # #     if extra_sleep == EMPLOYEE_EXTRA_SLEEP:
# # # #         extra_sleep_times = float(input("How many extra sleeps did you do?: "))
# # # #         extra_sleep_times = extra_sleep_times * FULL_TIME_EXTRA_SLEEP_RATE
# # # #         regular_pay += extra_sleep_times

        
# # # #     w_night = input("Do you have a wake-night or no-wake-night?: ").lower()

# # # #     if w_night == EMPLOYEE_WAKE_NIGHT:
# # # #         waking_night_times = float(input("How many waking nights?: "))
# # # #         wake_nights = waking_night_times * FULL_TIME_WAKING_NIGHT_RATE
# # # #         regular_pay += wake_nights
# # # # if employee_type == EMPLOYEE_TYPE_PART_TIME:
# # # #     hours_worked = float(input("Enter the number of hours worked this month: "))

# # # #     if hours_worked <= PART_TIME_HOURS:
# # # #         regular_pay = PART_TIME_HOURLY_RATE * hours_worked

# # # #     elif hours_worked > PART_TIME_HOURS:
# # # #         overtime_hours = hours_worked - PART_TIME_HOURS
# # # #         overtime_pay = PART_TIME_OVERTIME_RATE * overtime_hours
# # # #         regular_hours = hours_worked - overtime_hours
# # # #         regular_pay = PART_TIME_HOURLY_RATE * regular_hours+overtime_pay
# # # #         N_worked = overtime_pay


# # # #     employee_bank = input("Enter your holiday (bank-hol or no-bank-hol?): ").lower()

# # # #     if employee_bank == EMPLOYEE_HOLIDAY_BANK:
# # # #         holiday_hour = float(input("Enter the holiday-hour: "))
# # # #         bh_pay = holiday_hour * PART_TIME_BANK_HOLIDAY_RATE
# # # #         regular_pay += bh_pay

# # # #     sleep = input("Did you do a normal-sleep or no-sleep?: ").lower()

# # # #     if sleep == EMPLOYEE_SLEEP:
# # # #         sleep_times = float(input("How many sleeps did you do?: "))
# # # #         sleeps_times = sleep_times * PART_TIME_SLEEP_RATE
# # # #         regular_pay += sleeps_times
   


# # # #     extra_sleep = input("Did you do an extra-sleep or no-extra-sleep?: ").lower()

# # # #     if extra_sleep == EMPLOYEE_EXTRA_SLEEP:
# # # #         extra_sleep_times = float(input("How many extra sleeps did you do?: "))
# # # #         extra_sleep_times = extra_sleep_times * PART_TIME_EXTRA_SLEEP_RATE
# # # #         regular_pay += extra_sleep_times

# # # #     w_night = input("Do you have a wake-night or no-wake-night?: ").lower()

# # # #     if w_night == EMPLOYEE_WAKE_NIGHT:
# # # #         waking_night_times = float(input("How many waking nights?: "))
# # # #         wake_nights = waking_night_times * FULL_TIME_WAKING_NIGHT_RATE
# # # #         regular_pay += wake_nights

         
# # # # print(f"YOUR TOTAL WAGE FOR THIS MONTH is: {regular_pay}")

# # # from math import ceil

# # # # Constants
# # # EMPLOYEE_CATEGORY__SUPPORT_WORKER = 'support-worker'
# # # EMPLOYEE_CATEGORY_SENIOR_SUPPORT_WORKER = 'senior-support-worker'
# # # EMPLOYEE_CATEGORY_HOUSE_KEEPER = 'house-keeper'
# # # EMPLOYEE_CATEGORY_DEPUTY_MANAGER = 'deputy-manager'
# # # EMPLOYEE_TYPE_FULL_TIME = 'full-time'
# # # EMPLOYEE_TYPE_PART_TIME = 'part-time'
# # # FULL_TIME_HOURS = 150
# # # PART_TIME_HOURS = 80
# # # FULL_TIME_HOURLY_RATE_SUPPORT_WORKER = 11.75
# # # FULL_TIME_OVERTIME_RATE_SUPPORT_WORKER = 13.75
# # # FULL_TIME_BANK_HOLIDAY_RATE_SUPPORT_WORKER = 23.5
# # # FULL_TIME_HOURLY_RATE_SENIOR_SUPPORT_WORKER = 12.25
# # # FULL_TIME_OVERTIME_RATE_SENIOR_SUPPORT_WORKER = 14.25
# # # FULL_TIME_BANK_HOLIDAY_RATE_SENIOR_SUPPORT_WORKER = 24.50
# # # FULL_TIME_HOURLY_RATE_HOUSE_KEEPER = 10.42
# # # FULL_TIME_BANK_HOLIDAY_RATE_HOUSE_KEEPER = 20.84
# # # FULL_TIME_HOURLY_RATE_DEPUTY_MANAGER = 12.75
# # # FULL_TIME_OVERTIME_RATE_DEPUTY_MANAGER = 14.75
# # # FULL_TIME_BANK_HOLIDAY_RATE_DEPUTY_MANAGER = 25.5
# # # FULL_TIME_WAKING_NIGHT_RATE = 111.625
# # # FULL_TIME_SLEEP_RATE = 30
# # # FULL_TIME_EXTRA_SLEEP_RATE = 60
# # # PART_TIME_HOURLY_RATE_SUPPORT_WORKER = 11.75
# # # PART_TIME_OVERTIME_RATE_SUPPORT_WORKER = 13.75
# # # PART_TIME_BANK_HOLIDAY_RATE_SUPPORT_WORKER = 23.5
# # # PART_TIME_HOURLY_RATE_SENIOR_SUPPORT_WORKER = 12.25
# # # PART_TIME_OVERTIME_RATE_SENIOR_SUPPORT_WORKER = 14.25
# # # PART_TIME_BANK_HOLIDAY_RATE_SENIOR_SUPPORT_WORKER = 24.5
# # # PART_TIME_SLEEP_RATE = 30
# # # PART_TIME_WAKING_NIGHT_RATE = 111.625
# # # PART_TIME_EXTRA_SLEEP_RATE = 60

# # # # Get user input
# # # employeeCategory = input("Enter employee category: ")
# # # employeeType = input("Enter employee type: ")
# # # hoursWorked = float(input("Enter hours worked: "))
# # # holidayHour = float(input("Enter holiday hours: ") or 0)
# # # sleepTimes = float(input("Enter sleep times: ") or 0)
# # # extraSleepTimes = float(input("Enter extra sleep times: ") or 0)
# # # wakingNightTimes = float(input("Enter waking night times: ") or 0)

# # # # Initialize wage variable
# # # regularPay = 0

# # # # Calculation logic for house keeper
# # # if employeeCategory == EMPLOYEE_CATEGORY_HOUSE_KEEPER:
# # #     if employeeType == EMPLOYEE_TYPE_FULL_TIME:
# # #         regularPay = FULL_TIME_HOURLY_RATE_HOUSE_KEEPER * hoursWorked
# # #         regularPay += FULL_TIME_BANK_HOLIDAY_RATE_HOUSE_KEEPER * holidayHour
# # #         regularPay += FULL_TIME_SLEEP_RATE * sleepTimes
# # #         regularPay += FULL_TIME_EXTRA_SLEEP_RATE * extraSleepTimes
# # #         regularPay += FULL_TIME_WAKING_NIGHT_RATE * wakingNightTimes
# # #     else:
# # #         print("Error: There is no part-time for housekeeper")
# # #         exit()

# # # # Calculation logic for support worker
# # # elif employeeCategory == EMPLOYEE_CATEGORY__SUPPORT_WORKER:
# # #     if employeeType == EMPLOYEE_TYPE_FULL_TIME:
# # #         if hoursWorked <= FULL_TIME_HOURS:
# # #             regularPay = FULL_TIME_HOURLY_RATE_SUPPORT_WORKER * hoursWorked
# # #         else:
# # #             overtimeHours = hoursWorked - FULL_TIME_HOURS
# # #             regularPay = (
# # #                 FULL_TIME_HOURLY_RATE_SUPPORT_WORKER * FULL_TIME_HOURS +
# # #                 FULL_TIME_OVERTIME_RATE_SUPPORT_WORKER * overtimeHours
# # #             )
# # #         regularPay += FULL_TIME_BANK_HOLIDAY_RATE_SUPPORT_WORKER * holidayHour
# # #         regularPay += FULL_TIME_SLEEP_RATE * sleepTimes
# # #         regularPay += FULL_TIME_EXTRA_SLEEP_RATE * extraSleepTimes
# # #         regularPay += FULL_TIME_WAKING_NIGHT_RATE * wakingNightTimes
# # #     elif employeeType == EMPLOYEE_TYPE_PART_TIME:
# # #         if hoursWorked <= PART_TIME_HOURS:
# # #             regularPay = PART_TIME_HOURLY_RATE_SUPPORT_WORKER * hoursWorked
# # #         else:
# # #             overtimeHours = hoursWorked - PART_TIME_HOURS
# # #             regularPay = (
# # #                 PART_TIME_HOURLY_RATE_SUPPORT_WORKER * PART_TIME_HOURS +
# # #                 PART_TIME_OVERTIME_RATE_SUPPORT_WORKER * overtimeHours
# # #             )
# # #         regularPay += PART_TIME_BANK_HOLIDAY_RATE_SUPPORT_WORKER * holidayHour
# # #         regularPay += PART_TIME_SLEEP_RATE * sleepTimes
# # #         regularPay += PART_TIME_EXTRA_SLEEP_RATE * extraSleepTimes
# # #         regularPay += PART_TIME_WAKING_NIGHT_RATE * wakingNightTimes

# # # # Calculation logic for senior support worker
# # # elif employeeCategory == EMPLOYEE_CATEGORY_SENIOR_SUPPORT_WORKER:
# # #     if employeeType == EMPLOYEE_TYPE_FULL_TIME:
# # #         if hoursWorked <= FULL_TIME_HOURS:
# # #             regularPay = FULL_TIME_HOURLY_RATE_SENIOR_SUPPORT_WORKER * hoursWorked
# # #         else:
# # #             overtimeHours = hoursWorked - FULL_TIME_HOURS
# # #             regularPay = (
# # #                 FULL_TIME_HOURLY_RATE_SENIOR_SUPPORT_WORKER * FULL_TIME_HOURS +
# # #                 FULL_TIME_OVERTIME_RATE_SENIOR_SUPPORT_WORKER * overtimeHours
# # #             )
# # #         regularPay += FULL_TIME_BANK_HOLIDAY_RATE_SENIOR_SUPPORT_WORKER * holidayHour
# # #         regularPay += FULL_TIME_SLEEP_RATE * sleepTimes
# # #         regularPay += FULL_TIME_EXTRA_SLEEP_RATE * extraSleepTimes
# # #         regularPay += FULL_TIME_WAKING_NIGHT_RATE * wakingNightTimes
# # #     elif employeeType == EMPLOYEE_TYPE_PART_TIME:
# # #         if hoursWorked <= PART_TIME_HOURS:
# # #             regularPay = PART_TIME_HOURLY_RATE_SENIOR_SUPPORT_WORKER * hoursWorked
# # #         else:
# # #             overtimeHours = hoursWorked - PART_TIME_HOURS
# # #             regularPay = (
# # #                 PART_TIME_HOURLY_RATE_SENIOR_SUPPORT_WORKER * PART_TIME_HOURS +
# # #                 PART_TIME_OVERTIME_RATE_SENIOR_SUPPORT_WORKER * overtimeHours
# # #             )
# # #         regularPay += PART_TIME_BANK_HOLIDAY_RATE_SENIOR_SUPPORT_WORKER * holidayHour
# # #         regularPay += PART_TIME_SLEEP_RATE * sleepTimes
# # #         regularPay += PART_TIME_EXTRA_SLEEP_RATE * extraSleepTimes
# # #         regularPay += PART_TIME_WAKING_NIGHT_RATE * wakingNightTimes

# # # # Calculation logic for deputy manager
# # # elif employeeCategory == EMPLOYEE_CATEGORY_DEPUTY_MANAGER:
# # #     if employeeType == EMPLOYEE_TYPE_FULL_TIME:
# # #         if hoursWorked <= FULL_TIME_HOURS:
# # #             regularPay = FULL_TIME_HOURLY_RATE_DEPUTY_MANAGER * hoursWorked
# # #         else:
# # #             overtimeHours = hoursWorked - FULL_TIME_HOURS
# # #             regularPay = (
# # #                 FULL_TIME_HOURLY_RATE_DEPUTY_MANAGER * FULL_TIME_HOURS +
# # #                 FULL_TIME_OVERTIME_RATE_DEPUTY_MANAGER * overtimeHours
# # #             )
# # #         regularPay += FULL_TIME_BANK_HOLIDAY_RATE_DEPUTY_MANAGER * holidayHour
# # #         regularPay += FULL_TIME_SLEEP_RATE * sleepTimes
# # #         regularPay += FULL_TIME_EXTRA_SLEEP_RATE * extraSleepTimes
# # #         regularPay += FULL_TIME_WAKING_NIGHT_RATE * wakingNightTimes
# # #     else:
# # #         print("Error: There is no part-time for deputy manager")
# # #         exit()

# # # # Round up the result
# # # regularPay = ceil(regularPay)

# # # # Display result
# # # print(f"Your total wage for this month is: {regularPay}")


# # from math import ceil

# # def calculate_total_wage(employeeCategory, employeeType, hoursWorked, holidayHour=0, sleepTimes=0, extraSleepTimes=0, wakingNightTimes=0):
# #     # Constants
# #     EMPLOYEE_CATEGORY__SUPPORT_WORKER = 'support-worker'
# #     EMPLOYEE_CATEGORY_SENIOR_SUPPORT_WORKER = 'senior-support-worker'
# #     EMPLOYEE_CATEGORY_HOUSE_KEEPER = 'house-keeper'
# #     EMPLOYEE_CATEGORY_DEPUTY_MANAGER = 'deputy-manager'
# #     EMPLOYEE_TYPE_FULL_TIME = 'full-time'
# #     EMPLOYEE_TYPE_PART_TIME = 'part-time'
# #     FULL_TIME_HOURS = 150
# #     PART_TIME_HOURS = 80
# #     FULL_TIME_HOURLY_RATE_SUPPORT_WORKER = 11.75
# #     FULL_TIME_OVERTIME_RATE_SUPPORT_WORKER = 13.75
# #     FULL_TIME_BANK_HOLIDAY_RATE_SUPPORT_WORKER = 23.5
# #     FULL_TIME_HOURLY_RATE_SENIOR_SUPPORT_WORKER = 12.25
# #     FULL_TIME_OVERTIME_RATE_SENIOR_SUPPORT_WORKER = 14.25
# #     FULL_TIME_BANK_HOLIDAY_RATE_SENIOR_SUPPORT_WORKER = 24.50
# #     FULL_TIME_HOURLY_RATE_HOUSE_KEEPER = 10.42
# #     FULL_TIME_BANK_HOLIDAY_RATE_HOUSE_KEEPER = 20.84
# #     FULL_TIME_HOURLY_RATE_DEPUTY_MANAGER = 12.75
# #     FULL_TIME_OVERTIME_RATE_DEPUTY_MANAGER = 14.75
# #     FULL_TIME_BANK_HOLIDAY_RATE_DEPUTY_MANAGER = 25.5
# #     FULL_TIME_WAKING_NIGHT_RATE = 111.625
# #     FULL_TIME_SLEEP_RATE = 30
# #     FULL_TIME_EXTRA_SLEEP_RATE = 60
# #     PART_TIME_HOURLY_RATE_SUPPORT_WORKER = 11.75
# #     PART_TIME_OVERTIME_RATE_SUPPORT_WORKER = 13.75
# #     PART_TIME_BANK_HOLIDAY_RATE_SUPPORT_WORKER = 23.5
# #     PART_TIME_HOURLY_RATE_SENIOR_SUPPORT_WORKER = 12.25
# #     PART_TIME_OVERTIME_RATE_SENIOR_SUPPORT_WORKER = 14.25
# #     PART_TIME_BANK_HOLIDAY_RATE_SENIOR_SUPPORT_WORKER = 24.5
# #     PART_TIME_SLEEP_RATE = 30
# #     PART_TIME_WAKING_NIGHT_RATE = 111.625
# #     PART_TIME_EXTRA_SLEEP_RATE = 60

# #     # Initialize wage variable
# #     regularPay = 0

# #     # Calculation logic for house keeper
# #     if employeeCategory == EMPLOYEE_CATEGORY_HOUSE_KEEPER:
# #         if employeeType == EMPLOYEE_TYPE_FULL_TIME:
# #             regularPay = FULL_TIME_HOURLY_RATE_HOUSE_KEEPER * hoursWorked
# #             regularPay += FULL_TIME_BANK_HOLIDAY_RATE_HOUSE_KEEPER * holidayHour
# #             regularPay += FULL_TIME_SLEEP_RATE * sleepTimes
# #             regularPay += FULL_TIME_EXTRA_SLEEP_RATE * extraSleepTimes
# #             regularPay += FULL_TIME_WAKING_NIGHT_RATE * wakingNightTimes
# #         else:
# #          if employeeType == EMPLOYEE_TYPE_PART_TIME:
# #              raise ValueError("Error: There is no part-time for housekeeper")

# #     # Calculation logic for support worker
# #     elif employeeCategory == EMPLOYEE_CATEGORY__SUPPORT_WORKER:
# #         if employeeType == EMPLOYEE_TYPE_FULL_TIME:
# #             if hoursWorked <= FULL_TIME_HOURS:
# #                 regularPay = FULL_TIME_HOURLY_RATE_SUPPORT_WORKER * hoursWorked
# #             else:
# #                 overtimeHours = hoursWorked - FULL_TIME_HOURS
# #                 regularPay = (
# #                     FULL_TIME_HOURLY_RATE_SUPPORT_WORKER * FULL_TIME_HOURS +
# #                     FULL_TIME_OVERTIME_RATE_SUPPORT_WORKER * overtimeHours
# #                 )
# #             regularPay += FULL_TIME_BANK_HOLIDAY_RATE_SUPPORT_WORKER * holidayHour
# #             regularPay += FULL_TIME_SLEEP_RATE * sleepTimes
# #             regularPay += FULL_TIME_EXTRA_SLEEP_RATE * extraSleepTimes
# #             regularPay += FULL_TIME_WAKING_NIGHT_RATE * wakingNightTimes
# #         elif employeeType == EMPLOYEE_TYPE_PART_TIME:
# #             if hoursWorked <= PART_TIME_HOURS:
# #                 regularPay = PART_TIME_HOURLY_RATE_SUPPORT_WORKER * hoursWorked
# #             else:
# #                 overtimeHours = hoursWorked - PART_TIME_HOURS
# #                 regularPay = (
# #                     PART_TIME_HOURLY_RATE_SUPPORT_WORKER * PART_TIME_HOURS +
# #                     PART_TIME_OVERTIME_RATE_SUPPORT_WORKER * overtimeHours
# #                 )
# #             regularPay += PART_TIME_BANK_HOLIDAY_RATE_SUPPORT_WORKER * holidayHour
# #             regularPay += PART_TIME_SLEEP_RATE * sleepTimes
# #             regularPay += PART_TIME_EXTRA_SLEEP_RATE * extraSleepTimes
# #             regularPay += PART_TIME_WAKING_NIGHT_RATE * wakingNightTimes

# #     # Calculation logic for senior support worker
# #     elif employeeCategory == EMPLOYEE_CATEGORY_SENIOR_SUPPORT_WORKER:
# #         if employeeType == EMPLOYEE_TYPE_FULL_TIME:
# #             if hoursWorked <= FULL_TIME_HOURS:
# #                 regularPay = FULL_TIME_HOURLY_RATE_SENIOR_SUPPORT_WORKER * hoursWorked
# #             else:
# #                 overtimeHours = hoursWorked - FULL_TIME_HOURS
# #                 regularPay = (
# #                     FULL_TIME_HOURLY_RATE_SENIOR_SUPPORT_WORKER * FULL_TIME_HOURS +
# #                     FULL_TIME_OVERTIME_RATE_SENIOR_SUPPORT_WORKER * overtimeHours
# #                 )
# #             regularPay += FULL_TIME_BANK_HOLIDAY_RATE_SENIOR_SUPPORT_WORKER * holidayHour
# #             regularPay += FULL_TIME_SLEEP_RATE * sleepTimes
# #             regularPay += FULL_TIME_EXTRA_SLEEP_RATE * extraSleepTimes
# #             regularPay += FULL_TIME_WAKING_NIGHT_RATE * wakingNightTimes
# #         elif employeeType == EMPLOYEE_TYPE_PART_TIME:
# #             if hoursWorked <= PART_TIME_HOURS:
# #                 regularPay = PART_TIME_HOURLY_RATE_SENIOR_SUPPORT_WORKER * hoursWorked
# #             else:
# #                 overtimeHours = hoursWorked - PART_TIME_HOURS
# #                 regularPay = (
# #                     PART_TIME_HOURLY_RATE_SENIOR_SUPPORT_WORKER * PART_TIME_HOURS +
# #                     PART_TIME_OVERTIME_RATE_SENIOR_SUPPORT_WORKER * overtimeHours
# #                 )
# #             regularPay += PART_TIME_BANK_HOLIDAY_RATE_SENIOR_SUPPORT_WORKER * holidayHour
# #             regularPay += PART_TIME_SLEEP_RATE * sleepTimes
# #             regularPay += PART_TIME_EXTRA_SLEEP_RATE * extraSleepTimes
# #             regularPay += PART_TIME_WAKING_NIGHT_RATE * wakingNightTimes

# #     # Calculation logic for deputy manager
# #     elif employeeCategory == EMPLOYEE_CATEGORY_DEPUTY_MANAGER:
# #         if employeeType == EMPLOYEE_TYPE_FULL_TIME:
# #             if hoursWorked <= FULL_TIME_HOURS:
# #                 regularPay = FULL_TIME_HOURLY_RATE_DEPUTY_MANAGER * hoursWorked
# #             else:
# #                 overtimeHours = hoursWorked - FULL_TIME_HOURS
# #                 regularPay = (
# #                     FULL_TIME_HOURLY_RATE_DEPUTY_MANAGER * FULL_TIME_HOURS +
# # #                     FULL_TIME_OVERTIME_RATE_DEPUTY_MANAGER * overtimeHours
# # #                 )
# # #             regularPay += FULL_TIME_BANK_HOLIDAY_RATE_DEPUTY_MANAGER * holidayHour
# # #             regularPay += FULL_TIME_SLEEP_RATE * sleepTimes
# # #             regularPay += FULL_TIME_EXTRA_SLEEP_RATE * extraSleepTimes
# # #             regularPay += FULL_TIME_WAKING_NIGHT_RATE * wakingNightTimes
# # #         else:
# # #             raise ValueError("Error: There is no part-time for deputy manager")

# # #     # Round up the result
# # #     regularPay = ceil(regularPay)

# # #     return regularPay



# # # # Get user input
# # # employeeCategory = input("Enter employee category: ")
# # # employeeType = input("Enter employee type: ")
# # # hoursWorked = float(input("Enter hours worked: "))
# # # holidayHour = float(input("Enter holiday hours: ") or 0)
# # # sleepTimes = float(input("Enter sleep times: ") or 0)
# # # extraSleepTimes = float(input("Enter extra sleep times: ") or 0)
# # # wakingNightTimes = float(input("Enter waking night times: ") or 0)

# # # # Calculate and display the result
# # # totalWage = calculate_total_wage(employeeCategory, employeeType, hoursWorked, holidayHour, sleepTimes, extraSleepTimes, wakingNightTimes)
# # # print(f"Your total wage for this month is: {totalWage}")
# # # totalWage = calculate_total_wage("support-worker", "full-time", 6.0, 6.0, 7.0, 9.0, 9.0)

# # # print(totalWage)

from math import ceil
import json
from flask import Flask, request, jsonify
from flask_cors import CORS


def calculate_total_wage(employee_category, employee_type, hours_worked, holiday_hour=0, sleep_times=0,
                         extra_sleep_times=0, waking_night_times=0):
    # Constants
    employee_category_support_worker = 'support-worker'
    employee_category_senior_support_worker = 'senior-support-worker'
    employee_category_house_keeper = 'house-keeper'
    employee_category_deputy_manager = 'deputy-manager'
    employee_type_full_time = 'full-time'
    employee_type_part_time = 'part-time'
    full_time_hours = 150
    part_time_hours = 80
    full_time_hourly_rate_support_worker = 11.75
    full_time_overtime_rate_support_worker = 13.75
    full_time_bank_holiday_rate_support_worker = 23.5
    full_time_hourly_rate_senior_support_worker = 12.25
    full_time_overtime_rate_senior_support_worker = 14.25
    full_time_bank_holiday_rate_senior_support_worker = 24.50
    full_time_hourly_rate_house_keeper = 10.42
    full_time_bank_holiday_rate_house_keeper = 20.84
    full_time_hourly_rate_deputy_manager = 12.75
    full_time_overtime_rate_deputy_manager = 14.75
    full_time_bank_holiday_rate_deputy_manager = 25.5
    full_time_waking_night_rate = 111.625
    full_time_sleep_rate = 30
    full_time_extra_sleep_rate = 60
    part_time_hourly_rate_support_worker = 11.75
    part_time_overtime_rate_support_worker = 13.75
    part_time_bank_holiday_rate_support_worker = 23.5
    part_time_hourly_rate_senior_support_worker = 12.25
    part_time_overtime_rate_senior_support_worker = 14.25
    part_time_bank_holiday_rate_senior_support_worker = 24.5
    part_time_sleep_rate = 30
    part_time_waking_night_rate = 111.625
    part_time_extra_sleep_rate = 60

    # Initialize wage variable
    regular_pay = 0

    # Calculation logic for housekeeper
    if employee_category == employee_category_house_keeper:
        if employee_type == employee_type_full_time:
            regular_pay = full_time_hourly_rate_house_keeper * hours_worked
            regular_pay += full_time_bank_holiday_rate_house_keeper * holiday_hour
            regular_pay += full_time_sleep_rate * sleep_times
            regular_pay += full_time_extra_sleep_rate * extra_sleep_times
            regular_pay += full_time_waking_night_rate * waking_night_times
        else:
            if employee_type == employee_type_part_time:
                raise ValueError("Error: There is no part-time for housekeeper")

    # Calculation logic for support worker
    elif employee_category == employee_category_support_worker:
        if employee_type == employee_type_full_time:
            if hours_worked <= full_time_hours:
                regular_pay = full_time_hourly_rate_support_worker * hours_worked
            else:
                overtime_hours = hours_worked - full_time_hours
                regular_pay = (
                        full_time_hourly_rate_support_worker * full_time_hours +
                        full_time_overtime_rate_support_worker * overtime_hours
                )
            regular_pay += full_time_bank_holiday_rate_support_worker * holiday_hour
            regular_pay += full_time_sleep_rate * sleep_times
            regular_pay += full_time_extra_sleep_rate * extra_sleep_times
            regular_pay += full_time_waking_night_rate * waking_night_times
        elif employee_type == employee_type_part_time:
            if hours_worked <= part_time_hours:
                regular_pay = part_time_hourly_rate_support_worker * hours_worked
            else:
                overtime_hours = hours_worked - part_time_hours
                regular_pay = (
                        part_time_hourly_rate_support_worker * part_time_hours +
                        part_time_overtime_rate_support_worker * overtime_hours
                )
            regular_pay += part_time_bank_holiday_rate_support_worker * holiday_hour
            regular_pay += part_time_sleep_rate * sleep_times
            regular_pay += part_time_extra_sleep_rate * extra_sleep_times
            regular_pay += part_time_waking_night_rate * waking_night_times

    # Calculation logic for senior support worker
    elif employee_category == employee_category_senior_support_worker:
        if employee_type == employee_type_full_time:
            if hours_worked <= full_time_hours:
                regular_pay = full_time_hourly_rate_senior_support_worker * hours_worked
            else:
                overtime_hours = hours_worked - full_time_hours
                regular_pay = (
                        full_time_hourly_rate_senior_support_worker * full_time_hours +
                        full_time_overtime_rate_senior_support_worker * overtime_hours
                )
            regular_pay += full_time_bank_holiday_rate_senior_support_worker * holiday_hour
            regular_pay += full_time_sleep_rate * sleep_times
            regular_pay += full_time_extra_sleep_rate * extra_sleep_times
            regular_pay += full_time_waking_night_rate * waking_night_times
        elif employee_type == employee_type_part_time:
            if hours_worked <= part_time_hours:
                regular_pay = part_time_hourly_rate_senior_support_worker * hours_worked
            else:
                overtime_hours = hours_worked - part_time_hours
                regular_pay = (
                        part_time_hourly_rate_senior_support_worker * part_time_hours +
                        part_time_overtime_rate_senior_support_worker * overtime_hours
                )
            regular_pay += part_time_bank_holiday_rate_senior_support_worker * holiday_hour
            regular_pay += part_time_sleep_rate * sleep_times
            regular_pay += part_time_extra_sleep_rate * extra_sleep_times
            regular_pay += part_time_waking_night_rate * waking_night_times

    # Calculation logic for deputy manager
    elif employee_category == employee_category_deputy_manager:
        if employee_type == employee_type_full_time:
            if hours_worked <= full_time_hours:
                regular_pay = full_time_hourly_rate_deputy_manager * hours_worked
            else:
                overtime_hours = hours_worked - full_time_hours
                regular_pay = (
                        full_time_hourly_rate_deputy_manager * full_time_hours +
                        full_time_overtime_rate_deputy_manager * overtime_hours
                )
            regular_pay += full_time_bank_holiday_rate_deputy_manager * holiday_hour
            regular_pay += full_time_sleep_rate * sleep_times
            regular_pay += full_time_extra_sleep_rate * extra_sleep_times
            regular_pay += full_time_waking_night_rate * waking_night_times
        else:
            raise ValueError("Error: There is no part-time for deputy manager")

    # Round up the result
    regular_pay = ceil(regular_pay)

    return regular_pay


# # Get user input
# employeeCategory = input("Enter employee category: ")
# employeeType = input("Enter employee type: ")
# hoursWorked = int(input("Enter hours worked: "))
# holidayHour = int(input("Enter holiday hours: ") or 0)
# sleepTimes = int(input("Enter sleep times: ") or 0)
# extraSleepTimes = int(input("Enter extra sleep times: ") or 0)
# wakingNightTimes = int(input("Enter waking night times: ") or 0)

# # Calculate and display the result
# totalWage = calculate_total_wage(employeeCategory, employeeType, hoursWorked, holidayHour, sleepTimes, extraSleepTimes, wakingNightTimes)
# print(f"Your total wage for this month is: {totalWage}")

# totalWage = calculate_total_wage("support-worker", "full-time", 6, 6, 7, 9, 9)
# print(f"Your total wage for this hardcoded values is: {totalWage}")





# file = open("wage-values.txt", "r")
# line = file.readlines()

# employeeCategoryFromfile = (line[0])
# employeeTypeFromfile = (line[1])
# hourWorkedFromfile = (line[2])
# holidayhourFromfile = (line[3])
# sleepTimesFromfile = (line[4])
# extraSleepTimesFromfile = (line[5])
# wakingNightTimesFromfile =(line[6])

# calculate_total_wage(employeeCategoryFromfile, employeeTypeFromfile, hourWorkedFromfile, holidayhourFromfile, sleepTimesFromfile, extraSleepTimesFromfile, wakingNightTimesFromfile)
# print(f"your total wage for val is: {totalWage}")


# val = "userPrompts.json"
# with open(val, "r") as json_val:
#     input_display = json.load(json_val)
# print(input_display["employee_category"])
# print(input_display["employee_type"])
# print(input_display["hours_worked"])
# print(input_display["holiday_hour"])
# print(input_display["sleep_times"])
# print(input_display["extra_sleep_times"])
# print(input_display["waking_night_times"])

# totalWage = calculate_total_wage(input_display["employee_category"], input_display["employee_type"], input_display["hours_worked"], input_display["holiday_hour"], input_display["sleep_times"], input_display["extra_sleep_times"], input_display["waking_night_times"],)
# print(f"Your total wage for this month is: {totalWage}")

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/calculate-wage', methods=['POST'])
def handle_calculate_wage_request():
    react_json_object = request.json

    totalWage = calculate_total_wage(react_json_object["employee_category"], react_json_object["employee_type"], react_json_object["hours_worked"], react_json_object["holiday_hour"], react_json_object["sleep_times"], react_json_object["extra_sleep_times"], react_json_object["waking_night_times"],)

    response = {'total_wage': totalWage}
    return jsonify(response),200