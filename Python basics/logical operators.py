high_income = True
good_credit = True

if high_income and good_credit:
    print('Eligible for loan. ')

if high_income or good_credit:
    print('Eligible for loan. ')



high_income = True
criminal_record = True

if high_income and not criminal_record:
    print('Eligible for loan. ')

if high_income or criminal_record:
    print('Not Eligible for loan. ')