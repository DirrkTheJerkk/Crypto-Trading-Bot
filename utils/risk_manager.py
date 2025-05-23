def check_risk(exposure):
    if exposure > 10000:
        raise Exception("Exposure exceeds limits")
