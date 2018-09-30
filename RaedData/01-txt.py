def read_txt():
    with open('../DataPool/txt.txt','r',encoding='utf-8') as f:
        arrs = []
        datas = f.readlines()
        for data in datas:
            arrs.append(data.strip().split())
        return arrs

print(read_txt())