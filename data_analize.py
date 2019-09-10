import os
def content(i,j):
  now = os.getcwd()
  txt = now+'\content\\{}.{}.txt'.format(i,j)
  bb =[]
  c = 0
  try:
    with open(txt.format(i,j),'rb') as f:
        BB = ''
        for line in f.readlines():
            if line == '\n' or len(line) == 0 or len(line) == 1:
                continue
            this = line.decode('utf-8')
            if c == 0:
                time = this
                c +=1
            elif c == 1:
                title = this
                c += 1
            else:
                if this == '[表白]\n':
                    if len(BB) != 0:
                        aa = BB.strip()
                        cc = aa.strip('\n')
                        bb.append(cc)
                        BB = ''
                else:
                    BB+=this
    return (time,bb)
  except:
      pass
def search(x):
  sum = 0
  all = 0
  for i in range(65):
    for j in range(1,10):
        this = content(i,j)
        if this!= None:
            context = this[1]
            for item in context:
                if x in item:
                    print(this[0])
                    print(item)
                    sum += 1
  print(all)
  return sum
def isEnglish(y):
    english = True
    for x in y:
        if (ord(x) <= 122 and ord(x) >= 97) or (ord(x) >= 65 and ord(x) <= 90):
            english = True
        else:
            english = False
            break
    return english
common_firstname=['赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '褚', '卫', '蒋', '沈', '韩', '杨', '朱', '秦', '尤', '许',
'何', '吕', '施', '张', '孔', '曹', '严', '华', '金', '魏', '陶', '姜', '戚', '谢', '邹', '喻', '柏', '窦', '章',
'云', '苏', '潘', '葛', '奚', '范', '彭', '郎', '鲁', '韦', '昌', '马', '苗', '凤', '花', '方', '俞', '任', '袁', '柳',
'酆', '鲍', '史', '唐', '费', '廉', '岑', '薛', '雷', '贺', '倪', '汤', '滕', '殷', '罗', '毕', '郝', '邬', '安', '常',
'乐', '于', '时', '傅', '皮', '卞', '齐', '康', '伍', '余', '元', '卜', '顾', '孟', '平', '黄', '和', '穆', '萧', '尹',
'姚', '邵', '堪', '汪', '祁', '毛', '禹', '狄', '米', '贝', '明', '臧', '计', '伏', '成', '戴', '谈', '宋', '茅', '庞',
'熊', '纪', '舒', '屈', '项', '祝', '董', '梁']
common_english = ['to','you','his','her','rua','Day','isu','air','boy','girl','old','Eve','ve','are','and','And','our','can','ive','mmm','TO','rom']
def namecheck_E():
  NC = {}
  for i in range(65):
    for j in range(1,10):
        this = content(i,j)
        if this!= None:
            contexts = this[1]
            for context in contexts:
              for t in range(len(context)-2):
                if isEnglish(context[t]):
                    name_raw = ''
                    if t+3 >len(context)-1 and t!= len(context)-1 and isEnglish(context[-1]):
                        name_raw1 = context[t:]
                        if isEnglish(name_raw1) and name_raw1 not in common_english:
                            name_raw = name_raw1
                            #print(name_raw)
                        t = len(context)
                    elif t+3 <= len(context) -1 and isEnglish(context[t+3]) == False:
                        if isEnglish(context[t:t+3]):
                             name_raw1 = context[t:t+3]
                             if name_raw1 not in common_english:
                                 name_raw = name_raw1
                                #print(name_raw)
                             t += 3
                        elif isEnglish(context[t:t+2]) and name_raw not in common_english:
                             name_raw1 = context[t:t+2]
                             if  name_raw1 not in common_english:
                                 name_raw = name_raw1
                                #print(name_raw)
                             t += 2
                    elif isEnglish(context[t+1]) == False:
                        if i>=1 and isEnglish(context[t-1]) == False:
                            if context[t-1] in common_firstname:
                                print(context[t-1:t+1])
                    if len(name_raw)!=0:
                        if name_raw in NC:
                            NC[name_raw] += 1
                        else:
                            NC[name_raw] = 1
print(search("I do like you"))
namecheck_E()
