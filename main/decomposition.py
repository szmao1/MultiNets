from PyEMD import EMD

def apply_emd(carbon_series):
    emd = EMD()
    IMFs = emd(carbon_series)
    return IMFs
