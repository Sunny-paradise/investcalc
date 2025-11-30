def calc_local(capex, opex, training, period, savings, revenue):
    tco = capex + opex * period + training
    benefits = (savings + revenue) * period
    roi = (benefits - tco) / tco * 100
    pp = tco / (savings + revenue)
    return {"tco": tco, "roi": roi, "payback": pp}

def calc_cloud(subscription, training, period, savings, revenue):
    tco = subscription * period + training
    benefits = (savings + revenue) * period
    roi = (benefits - tco) / tco * 100
    pp = tco / (savings + revenue)
    return {"tco": tco, "roi": roi, "payback": pp}

