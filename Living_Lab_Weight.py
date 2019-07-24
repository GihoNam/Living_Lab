def Weight(Rssi):
    Rssi_result = []
    Rssi_Weight = [1/7,1/7,1/7,1/7,3/7]
    for i in range(len(Rssi)):
        Rssi_result.append(Rssi[i] * Rssi_Weight[i])
    return Rssi_result
