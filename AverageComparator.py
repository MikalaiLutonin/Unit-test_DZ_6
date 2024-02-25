class AverageComparator:
    def calculate_average(self, numbers):
        return sum(numbers) / len(numbers)

    def compare_averages(self, list1, list2):
        average_list1 = self.calculate_average(list1)
        average_list2 = self.calculate_average(list2)

        if average_list1 > average_list2:
            return "Первый список имеет большее среднее значение"
        elif average_list2 > average_list1:
            return "Второй список имеет большее среднее значение"
        else:
            return "Средние значения равны"
