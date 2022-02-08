
# 1-year, 5-year, 10-year, 30-year bond pricing
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

# Bond Schedule 1-year

issuedate1 = Date(1, 1, 2010)
maturitydate1 = Date(1, 1, 2011)
tenor = Period(Annual)
calendar = UnitedStates()
businessconvention = Unadjusted
dategeneration = DateGeneration.Backward
monthend = False

schedule1 = Schedule(issuedate1, maturitydate1, tenor, calendar, businessconvention, businessconvention, dategeneration, monthend)

# Bond Schedule 5-year

issuedate5 = Date(1, 1, 2010)
maturitydate5 = Date(1, 1, 2015)
tenor = Period(Annual)
calendar = UnitedStates()
businessconvention = Unadjusted
dategeneration = DateGeneration.Backward
monthend = False

schedule5 = Schedule(issuedate5, maturitydate5, tenor, calendar, businessconvention, businessconvention, dategeneration, monthend)

# Bond Schedule 10-year

issuedate10 = Date(1, 1, 2010)
maturitydate10 = Date(1, 1, 2020)
tenor = Period(Annual)
calendar = UnitedStates()
businessconvention = Unadjusted
dategeneration = DateGeneration.Backward
monthend = False

schedule10 = Schedule(issuedate10, maturitydate10, tenor, calendar, businessconvention, businessconvention, dategeneration, monthend)

#Bond Schedule 30-year

issuedate = Date(1, 1, 2010)
maturitydate = Date(1, 1, 2040)
tenor = Period(Annual)
calendar = NullCalendar()
businessconvention = Unadjusted
dategeneration = DateGeneration.Backward
monthend = False

schedule = Schedule(issuedate, maturitydate, tenor, calendar, businessconvention, businessconvention, dategeneration, monthend)

# Fixed Rate Bond 1-year

coupons = [0.05]
settlement_days = 0
face_value = 1000

fixed_rate_bond1 = FixedRateBond(settlement_days, face_value, schedule1, coupons, dayCounter)

# Fixed Rate Bond 5-year

coupons = [0.05]
settlement_days = 0
face_value = 1000

fixed_rate_bond5 = FixedRateBond(settlement_days, face_value, schedule5, coupons, dayCounter)

# Fixed Rate Bond 10-year

coupons = [0.05]
settlement_days = 0
face_value = 1000

fixed_rate_bond10 = FixedRateBond(settlement_days, face_value, schedule10, coupons, dayCounter)

#Fixed Rate Bond 30-year

coupons = [0.05]
settlement_days = 0
face_value = 1000

fixed_rate_bond30 = FixedRateBond(settlement_days, face_value, schedule, coupons, dayCounter)


# Valuation 1-year

bond_engine = DiscountingBondEngine(flatCurveHandle)
fixed_rate_bond1.setPricingEngine(bond_engine)

# Valuation 5-year

bond_engine = DiscountingBondEngine(flatCurveHandle)
fixed_rate_bond5.setPricingEngine(bond_engine)

# Valuation 10-year

bond_engine = DiscountingBondEngine(flatCurveHandle)
fixed_rate_bond10.setPricingEngine(bond_engine)

# Valuation 30-year

BondEngine = DiscountingBondEngine(flatCurveHandle)
fixed_rate_bond30.setPricingEngine(BondEngine)


# Present Bond Value 1-year

value1 = fixed_rate_bond1.NPV()
print(value1)

# Present Bond Value 5-year

value5 = fixed_rate_bond5.NPV()
print(value5)

# Present Bond Value 10-year

value10 = fixed_rate_bond10.NPV()
print(value10)

#Present Bond Value 30-year

value30 = fixed_rate_bond30.NPV()
print(value30)

import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
import numpy as np

x = np.array([1, 5, 10, 30])
y = np.array([value1, value5, value10, value30])

abSpline = make_interp_spline(x, y)
a = np.linspace(x.min(), x.max())
b = abSpline(a)

plt.plot(a, b)
plt.show()
