
    age = int(input("What is your current age?"))

    current_age_days = 365 * age
    current_age_weeks = 52 * age
    current_age_months = 12 * age

    days_90 = 90 * 365
    weeks_90 = 90 *52
    months_90 = 12 * 90

    left_days = days_90 - current_age_days
    left_weeks = weeks_90 - current_age_weeks
    left_months = months_90 - current_age_months

    print(f'You have {left_days} days, {left_weeks} weeks, and {left_months} months left.')

