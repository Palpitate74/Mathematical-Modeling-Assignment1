import random
from red_pocket import red_envelope  # 从 red_pocket 模块导入 red_envelope 函数
from engagement_and_excitement import calculate_engagement_index
from engagement_and_excitement import calculate_excited_index
# random.seed(252)
class RedPacketGame3:
    def __init__(self, total_members=21, absent_member=[19, 20]):  # 允许多个缺席委员
        self.total_members = total_members  # 总委员人数
        self.participants = [i for i in range(total_members)]  # 委员编号
        self.red_packet_data = {i: {"received": 0, "sent": 0} for i in range(total_members)}  # 委员的红包获得和发放统计
        self.members_in_game = []  # 记录每一轮参与游戏的委员
        self.sent_members = set()  # 记录已经发过红包的委员
        self.received_members = set()  # 记录已经抢到红包的委员
        self.flag = 0  # 游戏进行的轮数
        self.absent_member = absent_member  # 缺席的委员编号（列表）
        self.absent_flag = 0
        self.envelopes = []

    def start_round(self, absent_member, last_winner):
        """
        开始一轮红包分配
        :param absent_member: 缺席委员
        :param last_winner: 上一轮最大红包获得者，如果所有人抢到红包则由该人发红包
        """
        self.members_in_game = [i for i in self.participants if i not in absent_member]  # 移除多个缺席委员

        # 确定发红包者
        if last_winner is not None:  # 如果上一轮所有人都抢到红包，则由最大红包获得者发红包
            first_member = last_winner
        else:
            # 第一次红包发放由编号为1的委员发放
            first_member = 0  # 编号为1的委员在列表中的索引是0
        self.members_in_game.remove(first_member)
        for member in absent_member:
            self.members_in_game.append(member)
        random.shuffle(self.members_in_game)
        non_participant = self.members_in_game[-1]

        self.members_in_game = [first_member] + self.members_in_game[:-1]

        # 记录这一轮发红包的委员编号并增加发红包次数
        self.red_packet_data[first_member]["sent"] += 1
        self.sent_members.add(first_member)

        # 红包金额：100元
        total_amount = 100  # 总金额
        num_people = len(self.members_in_game)  # 参与抢红包的总人数

        # 使用从 red_pocket 模块导入的 red_envelope 函数来进行红包分配
        self.envelopes, max_person = red_envelope(total_amount, num_people)  # 红包金额分配

        # 发放红包给每个参与的委员
        for i in range(num_people):  # 一共发20个红包
            # 将红包金额分发给对应的委员，并更新其收到红包次数
            current_member = self.members_in_game[i]  # 获取当前参与的委员
            self.red_packet_data[current_member]["received"] += 1
            self.received_members.add(current_member)

        # 判断下一轮发红包的人
        if non_participant in self.absent_member:  # 如果 non_participant 和 self.absent_member 完全相同
            # 如果 self.members_in_game[max_person - 1] 在缺席列表中，选择一个没有发过红包的成员作为 next first_member
            if self.members_in_game[max_person - 1] in self.absent_member:
                # 从没有发过红包且不是缺席成员的成员中选择
                available_members = [i for i in self.members_in_game if
                                     self.red_packet_data[i]["sent"] == 0 and i not in self.absent_member]
                if available_members:
                    first_member = random.choice(available_members)  # 随机选择一个没有发过红包且不在缺席名单中的成员
                else:
                    # 如果没有找到未发红包且不在缺席名单中的成员（理论上不会发生），可以做一些默认处理
                    first_member = self.members_in_game[0]
            else:
                first_member = self.members_in_game[max_person - 1]
        else:
            first_member = non_participant

        # 检查是否所有编号从1到20的委员都已经发过红包
        all_members_sent = all(self.red_packet_data[i]["sent"] > 0 for i in range(len(self.members_in_game)-1))  # 检查编号1到20的委员是否都发过红包
        self.flag += 1

        if all_members_sent:
            return True, first_member  # 游戏结束，返回最大红包获得者
        return False, first_member  # 游戏继续


    def simulate_game(self):
        """
        模拟游戏的多轮，计算每个委员的发红包和抢红包次数
        """
        absent_member = self.absent_member  # 初始时无缺席委员
        last_winner = None  # 初始时没有最大红包获得者

        # 使用while循环使游戏能够无限进行直到结束条件成立
        while True:
            game_ended, last_winner = self.start_round(absent_member, last_winner)  # 传递上一轮的最大红包获得者
            if game_ended:  # 如果游戏结束
                break

    def get_summary(self):
        """
        返回各委员的红包获得和发放统计
        """
        return self.red_packet_data


# 创建游戏实例
game = RedPacketGame3()

# 模拟游戏
game.simulate_game()

# 输出委员抢红包次数和发红包次数
for member in range(1, 22):  # 输出1到21号委员的红包统计
    print(
        f"委员{member}抢到红包次数: {game.red_packet_data[member - 1]['received']}, 发红包次数: {game.red_packet_data[member - 1]['sent']}")

# 计算并输出活跃程度
engagement_index = calculate_engagement_index(game.participants, game.members_in_game, game.flag, game.red_packet_data)
print(f"活跃程度 (Coverage Efficiency Index): {engagement_index}")
#
# 计算并输出有趣程度
excitement_index = calculate_excited_index(game.envelopes, game.flag, game.members_in_game, game.absent_flag)
print(f"有趣程度 (Excitement Index): {excitement_index}")