import random


def red_envelope(money, person):
    # 计算每个红包的均值
    avg = money / person
    envelopes = []
    total_allocated = 0

    # 为每个人分配红包
    for i in range(person - 1):
        # 随机生成一个接近均值的小红包（避免某些红包金额过大）
        red_packet = round(random.uniform(avg / 2, avg * 1.5), 2)
        envelopes.append(red_packet)
        total_allocated += red_packet

    # 最后一个红包金额调整为剩余的金额
    last_packet = round(money - total_allocated, 2)
    envelopes.append(last_packet)

    # 找出获得最大红包的人
    max_packet = max(envelopes)
    max_person = envelopes.index(max_packet) + 1  # 人的编号从1开始

    return envelopes, max_person

