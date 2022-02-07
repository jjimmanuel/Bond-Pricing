
# 5-year bond
# face value = $1000
# market rate of 3%
# annual coupon payment of 5%

import QuantLib as ql
from QuantLib import *

# Yield Curve

day = Date(1, 1, 2010)
Settings.instance().evaluationDate = day 

spotDates = [Date(1, 1, 2010), Date(1, 1, 2011), Date(1, 1, 2015), Date(1, 1, 2020), Date(1, 1, 2040)]
spotRates = [0.03, 0.03, 0.03, 0.03, 0.03]

day_count = Actual365Fixed()
calendar = NullCalendar()
interpolation = Linear()
compounding = Compounded
compounding_frequency = Annual

spotCurve = ZeroCurve(spotDates, spotRates, day_count, calendar, interpolation, compounding, compounding_frequency)
spotCurveHandle = YieldTermStructureHandle(spotCurve)


# Bond Schedule

issuedate = Date(1, 1, 2010)
maturitydate = Date(1, 1, 2040)
tenor = Period(Annual)
calendar = NullCalendar()
businessconvention = Unadjusted
dategeneration = DateGeneration.Backward
monthend = False

schedule = Schedule(issuedate, maturitydate, tenor, calendar, businessconvention, businessconvention, dategeneration, monthend)

# Fixed Rate Bond

coupons = [0.05]
settlement_days = 0
face_value = 1000

fixed_rate_bond = FixedRateBond(settlement_days, face_value, schedule, coupons, day_count)

# Valuation  

bond_engine = DiscountingBondEngine(spotCurveHandle)
fixed_rate_bond.setPricingEngine(bond_engine)

# Present Value

value = fixed_rate_bond.NPV()
print(value)


























