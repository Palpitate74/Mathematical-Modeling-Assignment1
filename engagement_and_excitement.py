import numpy as np
def calculate_engagement_index(participants, members_in_game, N, red_packet_data):
    """
    计算活动的活跃程度
    :param members_in_game: 在场委员编号
           N: 活动轮数
           participants: 参与委员编号
           red_packet_data: 委员的红包获得和发放统计
    :return: 活跃程度得分：activity_scores：[0,100]
    """
    S = len(participants)
    S1 = len(members_in_game)
    T = sum(1 for member in members_in_game if red_packet_data[member]["sent"] == 0)
    activity_scores = S1 / N * np.log(1 + S / (T + 1))
    worst_score = 0
    best_score = S1 / S1 * np.log(1 + S / (S - S1 + 1))
    # activity_scores = activity_scores * 100 / (best_score - worst_score)
    activity_scores = activity_scores * 100 / 2.306120854470325
    return activity_scores

def calculate_excited_index(envelopes, N, members_in_game, absent_flag):
    """
    计算活动的有趣程度
    :param envelopes: 红包金额
           N: 活动轮数
           members_in_game: 在场委员编号
           absent_flag: 规则2.b触发次数
    :return: 有趣程度得分：excitement_score：[0,100]
    """
    S1 = len(members_in_game)
    S_i = np.var(envelopes)
    avg_amount = 100 / S1
    worst_score = 0
    best_score = (1 - avg_amount / 100) * avg_amount * avg_amount + avg_amount * (100 - avg_amount) * (100 - avg_amount) / 100 + 5 # 最大方差公式
    excitement_score = S_i + 5 * absent_flag / N
    # excitement_score = excitement_score * 100 / (best_score - worst_score)
    excitement_score = excitement_score * 100 / 37.02333051282051
    return excitement_score