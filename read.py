data = []
count = 0
with open ('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0: # 如果count和1000的餘數是0
            print(len(data))
print('檔案讀取完了,總共有', len(data), '筆資料')

#計算留言平均長度
sum_len = 0
for d in data:
   sum_len = sum_len + len(d)
print('留言的平均長度為', sum_len/len(data))

#篩選資料
new = []
for d in data:
   if len(d) < 100:
       new.append(d)
print('一共有', len(new), '筆留言長度小於100')
print(new[0])

good = []
for d in data:
   if 'good' in d:
       good.append(d)
print('一共有', len(good), '筆留言提到good')
print(good[0])


#文字計數
wc = {} # word_count的縮寫
for d in data:
    words = d.split(' ')
    for word in words:
        if word in wc: # 如果這筆word有在字典wc裡 # 要把假設改為否定時寫成not in即可
            wc[word] += 1 # 該word在字典裡的值加1
        else:
            wc[word] = 1 # 在字典裡新增該word，其值為1

for word in wc:
   if wc[word] > 100000:
       print(word, wc[word]) # 印出該word及該word在字典裡的值
   break

print('目前共有', len(wc), '個詞在字典裡') # 印出字典裡有幾個word(key)

while True:
    word = input('要查的字: ')
    if word == 'q':
        break
    if word in wc:
        print(word, '出現過的次數為:', wc[word])
    else:
        print('沒有這個字')
print('已離開')