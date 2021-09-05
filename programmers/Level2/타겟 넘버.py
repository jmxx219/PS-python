def solution(numbers, target):
    def dfs(index, T):
        if index == len(numbers) - 1:
            if T == 0:
                return 1
            else:
                return 0
        return dfs(index + 1, T - numbers[index]) + dfs(index + 1, T + numbers[index])

    return dfs(-1, target)


if __name__ == "__main__":
    numbers	= [1, 1, 1, 1, 1]
    target = 3
    print(solution(numbers, target))