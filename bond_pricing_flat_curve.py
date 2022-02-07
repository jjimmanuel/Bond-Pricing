
# 5-year bond
# face value = $1000
# market rate of 3%
# annual coupon payment of 5%

import QuantLib as ql
from QuantLib import *

# Constructing Yield Curve

day = Date(1, 1, 2010)
Settings.instance().evaluationDate = day 
dayCounter = Actual365Fixed()
rate = 0.03
compounding = Compounded
frequency = Annual


flatCurve = FlatForward(day, rate, dayCounter, compounding, frequency)
flatCurveHandle = YieldTermStructureHandle(flatCurve)

#Bond Schedule

issuedate = Date(1, 1, 2010)
maturitydate = Date(1, 1, 2040)
tenor = Period(Annual)
calendar = NullCalendar()
businessconvention = Unadjusted
dategeneration = DateGeneration.Backward
monthend = False

schedule = Schedule(issuedate, maturitydate, tenor, calendar, businessconvention, businessconvention, dategeneration, monthend)

#Fixed Rate Bond

coupons = [0.05]
settlement_days = 0
face_value = 1000

fixed_rate_bond = FixedRateBond(settlement_days, face_value, schedule, coupons, dayCounter)

#Bond engine

engine = DiscountingBondEngine(flatCurveHandle)
fixed_rate_bond.setPricingEngine(engine)

#Present Bond Value

value = fixed_rate_bond.NPV()
print(value)