class Player:
    def __init__(self, name, number, position, goals, matches):
        self.name = name
        self.number = number
        self.position = position
        self.goals = goals
        self.matches = matches
    def __str__(self):
        return f"{self.name} (Số áo: {self.number}) - Vị trí: {self.position}, Bàn thắng: {self.goals}, Trận đấu: {self.matches}"
class FootballTeam:
    def __init__(self):
        self.players = []
    def add_player(self, name, number, position, goals, matches):
        player = Player(name, number, position, goals, matches)
        self.players.append(player)
        print(f"Đã thêm cầu thủ: {name}")
    def update_player(self, number, goals=None, matches=None):
        for player in self.players:
            if player.number == number:
                if goals is not None:
                    player.goals = goals
                if matches is not None:
                    player.matches = matches
                print(f"Đã cập nhật thông tin cho cầu thủ số áo {number}.")
                return
        print("Không tìm thấy cầu thủ!")
    def remove_player(self, number):
        for player in self.players:
            if player.number == number:
                self.players.remove(player)
                print(f"Đã xóa cầu thủ số áo {number}.")
                return
        print("Không tìm thấy cầu thủ!")
    def display_players(self):
        if not self.players:
            print("Đội bóng chưa có cầu thủ.")
        for player in self.players:
            print(player)
    def search_player(self, query):
        found = [player for player in self.players if str(query) in player.name or str(query) == str(player.number)]
        if not found:
            print("Không tìm thấy cầu thủ!")
        for player in found:
            print(player)
def main():
    team = FootballTeam()
    while True:
        print("\nQuản lý đội bóng đá")
        print("1. Thêm cầu thủ")
        print("2. Cập nhật thông tin cầu thủ")
        print("3. Xóa cầu thủ")
        print("4. Hiển thị danh sách cầu thủ")
        print("5. Tìm kiếm cầu thủ")
        print("0. Thoát")
        choice = input("Chọn một tùy chọn: ")

        if choice == "1":
            name = input("Tên cầu thủ: ")
            number = int(input("Số áo: "))
            position = input("Vị trí: ")
            goals = int(input("Số bàn thắng: "))
            matches = int(input("Số trận đấu: "))
            team.add_player(name, number, position, goals, matches)

        elif choice == "2":
            number = int(input("Nhập số áo cầu thủ cần cập nhật: "))
            goals = int(input("Số bàn thắng mới: "))
            matches = int(input("Số trận đấu mới: "))
            team.update_player(number, goals, matches)

        elif choie == "3":
            number = int(input("Nhập số áo cầu thủ cần xóa: "))
            team.remove_player(number)

        elif choice == "4":
            print("\nDanh sách cầu thủ:")
            team.display_players()

        elif choice == "5":
            query = input("Nhập tên hoặc số áo cầu thủ: ")
            team.search_player(query)

        elif choice == "0":
            print("Thoát chương trình.")
            break

        else:
            print("Tùy chọn không hợp lệ!")

if __name__ == "__main__":
    main()
