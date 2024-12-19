string="i love python"
ch_count={}
for ch in string.split():
    if ch not in ch_count.keys():
       ch_count[ch]=string.count(ch)
print(ch_count)