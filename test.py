import random
from red_pocket import red_envelope  # 导入red_envelope函数
from engagement_and_excitement import calculate_engagement_index
from game_20 import RedPacketGame1  # 导入RedPacketGame类
from game_21 import RedPacketGame2
from tqdm import tqdm  # 导入tqdm库来显示进度条
from engagement_and_excitement import calculate_excited_index
import numpy as np
import matplotlib.pyplot as plt

def simulate_with_random_seeds():
    max_engagement_index = -1  # 用于记录最大活跃度
    min_engagement_index = 10000
    max_excitement_index = -1  # 用于记录最大活跃度
    min_excitement_index = 10000
    # max_excitement_index = -1
    # best_excitement_seed = None  # 用于记录对应最大活跃度的种子
    best_engagement_seed = None
    worst_engagement_seed = None
    best_excitement_seed = None
    worst_excitement_seed = None
    engagement_indices = []
    excitement_indices = []
    # 使用tqdm来添加进度条，遍历1到100000的随机种子
    for seed in tqdm(range(1, 100001), desc="Simulating with seeds", unit="seed"):
        random.seed(seed)  # 设置随机种子

        # 创建游戏实例
        game1 = RedPacketGame1()

        # 模拟游戏
        game1.simulate_game()

        # 计算活跃度
        engagement_index1 = calculate_engagement_index(game1.participants, game1.members_in_game, game1.flag, game1.red_packet_data)
        excitement_index1 = calculate_excited_index(game1.envelopes, game1.flag,game1.members_in_game, game1.absent_flag)
        engagement_indices.append(engagement_index1)
        excitement_indices.append(excitement_index1)
        # 如果当前活跃度大于最大活跃度，则更新最大活跃度和对应种子
        if engagement_index1 > max_engagement_index:
            max_engagement_index = engagement_index1
            best_engagement_seed = seed

        if engagement_index1 < min_engagement_index:
            min_engagement_index = engagement_index1
            worst_engagement_seed = seed
        if excitement_index1 > max_excitement_index:
            max_excitement_index = excitement_index1
            best_excitement_seed = seed
        if excitement_index1 < min_excitement_index:
            min_excitement_index = excitement_index1
            worst_excitement_seed = seed
    # 输出最大活跃度和对应的种子
    # 计算平均值
    print(f"最大活跃度为: {max_engagement_index}")
    print(f"对应活跃度的最佳随机种子为: {best_engagement_seed}")
    print(f"最小活跃度为: {min_engagement_index}")
    print(f"对应活跃度的最差随机种子为: {worst_engagement_seed}")
    print(f"最大有趣度为: {max_excitement_index}")
    print(f"对应有趣度的最佳随机种子为: {best_excitement_seed}")
    print(f"最小有趣度为: {min_excitement_index}")
    print(f"对应有趣度的最差随机种子为: {worst_excitement_seed}")


    # 设置图形的背景颜色
    plt.style.use('seaborn-whitegrid')  # 使用网格背景风格

    # 创建一个 12x6 英寸的图形
    plt.figure(figsize=(12, 6))

    # 第一张图：RedPacketGame1的engagement_index
    plt.subplot(1, 2, 1)
    plt.plot(range(1, 100001), engagement_indices, color='#FF6347', linewidth=1.5, label='Engagement Index 1')  # 使用番茄红
    plt.axhline(y=max_engagement_index, color='#4682B4', linestyle='--', linewidth=2, label=f'Average: {max_engagement_index:.2f}')  # 使用钢青色
    plt.axhline(y=min_engagement_index, color='#4682B4', linestyle='--', linewidth=2,
                label=f'Average: {min_engagement_index:.2f}')  # 使用钢青色
    plt.xlabel("Random Seed", fontsize=12, color='#333333')  # 设置标签字体和颜色
    plt.ylabel("Engagement Index", fontsize=12, color='#333333')
    plt.title("Engagement Index for RedPacketGame1", fontsize=14, fontweight='bold', color='#333333')
    plt.legend()
    #
    # 第二张图：RedPacketGame2的engagement_index
    plt.subplot(1, 2, 2)
    plt.plot(range(1, 100001), excitement_indices, color='#32CD32', linewidth=1.5,
             label='Engagement Index 2')  # 使用绿宝石绿
    plt.axhline(y=max_excitement_index, color='#FFD700', linestyle='--', linewidth=2, label=f'Average: {max_excitement_index:.2f}')  # 使用金色
    plt.axhline(y=min_excitement_index, color='#FFD700', linestyle='--', linewidth=2, label=f'Average: {min_excitement_index:.2f}')  # 使用金色
    plt.xlabel("Random Seed", fontsize=12, color='#333333')
    plt.ylabel("Engagement Index", fontsize=12, color='#333333')
    plt.title("Engagement Index for RedPacketGame2", fontsize=14, fontweight='bold', color='#333333')
    plt.legend()
    #
    # 调整图形布局
    plt.tight_layout()
    # 保存图像
    plt.tight_layout()
    plt.savefig('max_and_min_engagement_and_excitement_indices.png')

    # 显示图像
    plt.show()
if __name__ == "__main__":
    simulate_with_random_seeds()