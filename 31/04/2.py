# s * n の書式を使ってシーケンスを作成すると、浅いコピーになる
# 使いどころがないだけでなく、混乱の元になるだけな気がする
lists = [[]] * 3
print(lists) #[[], [], []]
lists[0].append(3)
print(lists) #[[3], [3], [3]]

# 深いコピーにする
lists = [[] for i in range(3)]
lists[0].append(3)
lists[1].append(5)
lists[2].append(7)
print(lists) #[[3], [5], [7]]

#一次元配列でやる
lists = [] * 3
print(lists)
lists = [1,2] * 3
print(lists)
