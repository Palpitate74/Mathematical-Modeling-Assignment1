import random
from red_pocket import red_envelope  # 导入red_envelope函数
from engagement_and_excitement import calculate_engagement_index
from game_20 import RedPacketGame1  # 导入RedPacketGame类
from game_21 import RedPacketGame2
from improved_rule import RedPacketGame3
from improved_rule2 import RedPacketGame4
from tqdm import tqdm  # 导入tqdm库来显示进度条
from engagement_and_excitement import calculate_excited_index
import numpy as np
import matplotlib.pyplot as plt

def simulate_with_random_seeds():
    max_engagement_index = -1  # 用于记录最大活跃度
    # max_excitement_index = -1
    # best_excitement_seed = None  # 用于记录对应最大活跃度的种子
    best_engagement_seed = None
    engagement_indices1 = []  # 用于保存 RedPacketGame1 的 engagement_index 数据
    engagement_indices2 = []  # 用于保存 RedPacketGame2 的 engagement_index 数据
    engagement_indices3 = []
    excitement_indices = []
    # 使用tqdm来添加进度条，遍历1到100000的随机种子
    for seed in tqdm(range(1, 100001), desc="Simulating with seeds", unit="seed"):
        random.seed(seed)  # 设置随机种子

        # 创建游戏实例
        game1 = RedPacketGame1()
        game2 = RedPacketGame3()
        game3 = RedPacketGame4()
        # 模拟游戏
        game1.simulate_game()
        game2.simulate_game()
        game3.simulate_game()
        # 计算活跃度
        engagement_index1 = calculate_engagement_index(game1.participants, game1.members_in_game, game1.flag, game1.red_packet_data)
        excitement_index = calculate_excited_index(game1.envelopes, game1.flag, game1.members_in_game, game1.absent_flag)
        engagement_index2 = calculate_engagement_index(game2.participants, game2.members_in_game, game2.flag,
                                                      game2.red_packet_data)
        engagement_index3 = calculate_engagement_index(game3.participants, game3.members_in_game, game3.flag,
                                                       game3.red_packet_data)

        engagement_indices1.append(engagement_index1)
        engagement_indices2.append(engagement_index2)
        engagement_indices3.append(engagement_index3)
        excitement_indices.append(excitement_index)
        # 如果当前活跃度大于最大活跃度，则更新最大活跃度和对应种子
        if engagement_index1 > max_engagement_index:
            max_engagement_index = engagement_index1
            best_engagement_seed = seed
        # if excitement_index > max_excitement_index:
        #     max_excitement_index = excitement_index
        #     best_excitement_seed = seed
    # 输出最大活跃度和对应的种子
    # 计算平均值
    avg_eni1 = np.mean(engagement_indices1)
    avg_eni2 = np.mean(engagement_indices2)
    avg_eni3 = np.mean(engagement_indices3)
    avg_exi = np.mean(excitement_indices)
    print(f"最大活跃度为: {max_engagement_index}")
    # print(f"最大有趣度为: {max_excitement_index}")
    print(f"对应活跃度的最佳随机种子为: {best_engagement_seed}")
    # print(f"对应有趣度的最佳随机种子为: {best_excitement_seed}")
    print(f"平均活跃度1为: {avg_eni1}")
    print(f"平均活跃度2为: {avg_eni2}")
    print(f"平均活跃度3为: {avg_eni3}")


    # 设置图形的背景颜色
    plt.style.use('seaborn-whitegrid')  # 使用网格背景风格

    # 创建一个 12x6 英寸的图形
    plt.figure(figsize=(12, 6))

    # 第一张图：RedPacketGame1的engagement_index
    plt.subplot(1, 2, 1)
    plt.plot(range(1, 100001), engagement_indices3, color='#7532cd', linewidth=1.5, label='Engagement Index')  # 使用番茄红
    plt.axhline(y=avg_eni3, color='#cdc832', linestyle='--', linewidth=2, label=f'Average: {avg_eni3:.2f}')  # 使用钢青色
    plt.xlabel("Random Seed", fontsize=12, color='#333333')  # 设置标签字体和颜色
    plt.ylabel("Engagement Index", fontsize=12, color='#333333')
    plt.title("Engagement Index for RedPacketGame1", fontsize=14, fontweight='bold', color='#333333')
    plt.legend()

    # 第二张图：RedPacketGame2的engagement_index
    plt.subplot(1, 2, 2)
    plt.plot(range(1, 100001), excitement_indices, color='#3282cd', linewidth=1.5,
             label='Excitement Index')  # 使用绿宝石绿
    plt.axhline(y=avg_exi, color='#9ccd32', linestyle='--', linewidth=2, label=f'Average: {avg_exi:.2f}')  # 使用金色
    plt.xlabel("Random Seed", fontsize=12, color='#333333')
    plt.ylabel("Engagement Index", fontsize=12, color='#333333')
    plt.title("Engagement Index for RedPacketGame3", fontsize=14, fontweight='bold', color='#333333')
    plt.legend()

    # plt.subplot(1, 3, 3)
    # plt.plot(range(1, 100001), engagement_indices1, color='#32CD32', linewidth=1.5,
    #          label='Engagement Index 4')  # 使用绿宝石绿
    # plt.axhline(y=avg_eni1, color='#FFD700', linestyle='--', linewidth=2, label=f'Average: {avg_eni1:.2f}')  # 使用金色
    # plt.xlabel("Random Seed", fontsize=12, color='#333333')
    # plt.ylabel("Engagement Index", fontsize=12, color='#333333')
    # plt.title("Engagement Index for RedPacketGame4", fontsize=14, fontweight='bold', color='#333333')
    # plt.legend()
    # 调整图形布局
    plt.tight_layout()
    # 保存图像
    plt.tight_layout()
    plt.savefig('engagement_and_excitement_calculate.png')

    # 显示图像
    plt.show()
if __name__ == "__main__":
    simulate_with_random_seeds()