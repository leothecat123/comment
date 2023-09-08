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