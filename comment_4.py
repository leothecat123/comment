#統計留言數目
data = []
count = 0
with open ('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0:
            print(len(data))
print('檔案讀取完了，總共有', len(data), '筆資料')

#計算留言總長度
#sum_len = 0
#for d in data:
#    sum_len = sum_len + len(d)
#    print(sum_len)

#留言平均長度
sum_len = 0
for d in data:
    sum_len = sum_len + len(d)
print('每個留言的平均長度為', sum_len / len(data))

new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print('一共有', len(new), '個留言長度小於100個字')
print(new[0])
print(new[1])

good = []
for d in data:
    if 'good' in d:
        good.append(d)
print('一共有', len(good), '個留言有包含good這個字')
print(good[0])

#清單快寫法
good = [d for d in data if 'good' in d]
print('一共有', len(good), '個留言有包含good這個字')

#會顯示每一筆true/false
bad = ['bad' in d for d in data]
print(bad)

# 等於以下寫法
# bad = []
# for d in data:
#     bad.append(d)
# print(bad)