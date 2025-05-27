import random
from tqdm import tqdm  # 导入tqdm库来显示进度条
from red_pocket import red_envelope  # 导入red_envelope函数
from engagement_and_excitement import calculate_engagement_index
from game_20 import RedPacketGame1  # 导入RedPacketGame类


def simulate_with_total_members():
    max_engagement_index = -1  # 用于记录最大活跃度
    best_total_members = None  # 用于记录对应最大活跃度的total_members
    worst_total_members = None

    # 固定随机数种子
    random.seed(252)

    # 遍历total_members从2到100，并使用tqdm显示进度条
    for total_members in tqdm(range(3, 101), desc="Simulating with total_members", unit="total_members"):
        # 创建游戏实例，模拟每种total_members情况
        game = RedPacketGame1(total_members=total_members, absent_member=total_members - 1)

        # 模拟游戏
        game.simulate_game()

        # 计算活跃度
        engagement_index = calculate_engagement_index(game.participants, game.members_in_game, game.flag, game.red_packet_data)

        # 如果当前活跃度大于最大活跃度，则更新最大活跃度和对应的total_members
        if engagement_index > max_engagement_index:
            max_engagement_index = engagement_index
            best_total_members = total_members

    # 输出最大活跃度和对应的total_members
    print(f"最大活跃度为: {max_engagement_index}")
    print(f"对应的最佳total_members为: {best_total_members}")

if __name__ == "__main__":
    simulate_with_total_members()
