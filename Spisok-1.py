# n = int(input())
# a = []
# for i in range(n):
#     a.append(list(map(int, input().split())))
# is_symmetry = True
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         if a[i][j] != a[j][i]:
#             is_symmetry = False
# if is_symmetry:
#     print("yes")
# else:
#     print("no")


# n = int(input())
# a = []
# for i in range(n):
#     a.append([0] * n)
#
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         if n - 1 == j + i:
#             a[i][j] = 1
#         if n - 1 < j + i:
#             a[i][j] = 2
# for i in a:
#     print(*i)


# n, m = map(int, input().split())
# a = []
# for i in range(n):
#     a.append([2] * m)
# b = 0
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         a[i][j] = b
#         b += 2
# for i in a:
#     print(*i)


# n, m = map(int, input().split())
# a = []
# for i in range(n):
#     a.append(list(map(int, input().split())))
# b = 1
# c = []
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         if a[i][j] > b:
#             b = a[i][j]
#             c.append(i)
# print(c)

# n, m = map(int, input().split())
# a = []
# for i in range(n):
#     a.append(list(map(int, input().split())))
# b = 1
# c = []
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         if a[i][j] > b:
#             c = []
#             b = a[i][j]
#             c.append(i)
#         elif a[i][j] == b:
#             c.append(i)
#         # Пробегаешься по списку "с", если он не равен 1, и уже смотришь суммы списков по индексу с[i]
# print(*c[-1:])

# n, m = map(int, input().split())
# a = []
# s = 0
# for i in range(n):
#     a.append([0] * m)
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         a[i][j] = s
#         s += 1
#     if i % 2 != 0:
#         a[i].reverse()
#
# for i in a:
#     print(*i)


n, m = map(int, input().split())
scores = []
potential_winners = []
max_score = 0
for i in range(n):
    scores.append(list(map(int, input().split())))

for player in range(len(scores)):
    max_player_score = max(scores[player])
    if max_score < max_player_score:
        potential_winners = [player]
        max_score = max_player_score
    elif max_score == max_player_score:
        potential_winners.append(player)

if len(potential_winners) == 1:
    print(*potential_winners)
else:
    sum_scores = []
    for player in potential_winners:
        sum_scores.append(sum(scores[player]))
    max_sum = max(sum_scores)
    print(potential_winners[sum_scores.index(max_sum)])
