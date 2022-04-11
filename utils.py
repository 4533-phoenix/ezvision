import psutil
import time
import os

def net_usage(inf=None):
    if inf is None:
        inf = os.listdir("/sys/class/net/")[0]

    net_stat = psutil.net_io_counters(pernic=True, nowrap=True)[inf]
    net_in_1 = net_stat.bytes_recv
    net_out_1 = net_stat.bytes_sent
    time.sleep(0.25)
    net_stat = psutil.net_io_counters(pernic=True, nowrap=True)[inf]
    net_in_2 = net_stat.bytes_recv
    net_out_2 = net_stat.bytes_sent

    net_in = (net_in_2 - net_in_1) / 1024 / 1024 * 4
    net_out = (net_out_2 - net_out_1) / 1024 / 1024 * 4

    return {"Network In (MB/s)": round(net_in, 1), "Network Out (MB/s)": round(net_out, 1)}