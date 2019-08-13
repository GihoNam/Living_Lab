def Weight(Rssi):
    Rssi_result = []
    Rssi_Weight = [1/7,1/7,1/7,1/7,3/7]
    for i in ((Rssi)):
        for j in range(len(i)):
            Rssi_result.append(round(i[j] * Rssi_Weight[j],3))
    return Rssi_result
