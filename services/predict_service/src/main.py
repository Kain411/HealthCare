import pandas
import math
import os
from sklearn.model_selection import train_test_split

class Main:
    def __init__(self):
        self.symptoms = ["Tuổi", "Giới tính", "Sốt", "Đau ngực", "Khó thở", "Ho", "Chóng mặt", "Huyết áp", "Nhịp tim", "Bệnh"]
        self.df = self.readCSV()
        self.data = self.getData(self.df)
        self.data_train, self.data_test = train_test_split(self.data, test_size=0.2, random_state=42)
    
    def readCSV(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, 'dataset', 'DA.csv')
        csv = pandas.read_csv(file_path)
        csv = csv.drop(columns=['ID', "Đau đầu"])
        return csv.to_numpy()

    def fixAge(self, num):
        if num>=1 and num<20: return "0-19"
        elif num>=20 and num<50: return "20-49"
        return ">=50"

    def getData(self, lst):
        res = []
        for row in lst:
            save = {}
            for index in range(0, len(row)):
                if index==0: 
                    row[index] = self.fixAge(row[index])
                save.update({self.symptoms[index]: row[index]})
            res.append(save)
        return res  

    def entropy(self, lst):
        res = 0
        total = 0
        for num in lst: total += num
        for num in lst:
            if num!=0:
                tmp = num/total
                res += - tmp * math.log2(tmp)
        return res

    def getEntropyOriginal(self, lst):
        sum = 0
        total = 0
        for key in lst:
            total += lst[key]
        if lst["Tim"]!=0: sum += - (lst["Tim"]/total)*math.log2(lst["Tim"]/total) 
        if lst["Phổi"]!=0: sum += - (lst["Phổi"]/total)*math.log2(lst["Phổi"]/total) 
        if lst["Tiêu chảy"]!=0: sum += - (lst["Tiêu chảy"]/total)*math.log2(lst["Tiêu chảy"]/total) 
        if lst["Tim, Phổi"]!=0: sum += - (lst["Tim, Phổi"]/total)*math.log2(lst["Tim, Phổi"]/total) 
        if lst["Tim, Tiêu chảy"]!=0: sum += - (lst["Tim, Tiêu chảy"]/total)*math.log2(lst["Tim, Tiêu chảy"]/total) 
        if lst["Phổi, Tiêu chảy"]!=0: sum += - (lst["Phổi, Tiêu chảy"]/total)*math.log2(lst["Phổi, Tiêu chảy"]/total) 
        if lst["Tim, Phổi, Tiêu chảy"]!=0: sum += - (lst["Tim, Phổi, Tiêu chảy"]/total)*math.log2(lst["Tim, Phổi, Tiêu chảy"]/total) 
        if lst["Khác"]!=0: sum += - (lst["Khác"]/total)*math.log2(lst["Khác"]/total) 
        return sum

    def getIG(self, entropy, totalRow, lst, lstNum):
        total = 0
        for i in range(len(lst)):
            total = lstNum[i]/totalRow * lst[i]
        return entropy-total

    def run(self, labels):

        # lấy các trường ch xét
        lst = {}
        if labels!={}:
            for i in self.symptoms:
                ok = True
                for key in labels.keys():
                    if i==key or i=="Bệnh":
                        ok = False
                        break 
                if ok: lst.update({i : {}})
        else:
            for i in self.symptoms:
                if i!="Bệnh":
                    lst.update({i: {}})
        
        # lấy data mới khi đã lọc 
        newData = []
        for row in self.data_train:
            ok = True
            for key in labels.keys():
                if row[key]!=labels[key]:
                    ok = False
                    break
            if ok: newData.append(row)

        # lấy các giá trị của các trường ch xét
        for key in lst.keys():
            chk = []
            for row in newData:
                if not chk.__contains__(row[key]):
                    chk.append(row[key])
                    lst[key].update({row[key]: {}})
                    lst[key][row[key]].update({"Tim": 0})
                    lst[key][row[key]].update({"Phổi": 0})
                    lst[key][row[key]].update({"Tiêu chảy": 0})
                    lst[key][row[key]].update({"Tim, Phổi": 0})
                    lst[key][row[key]].update({"Tim, Tiêu chảy": 0})
                    lst[key][row[key]].update({"Phổi, Tiêu chảy": 0})
                    lst[key][row[key]].update({"Tim, Phổi, Tiêu chảy": 0})
                    lst[key][row[key]].update({"Khác": 0})
            
        # đếm số lượng theo nhãn
        for i in lst.keys():
            for j in lst[i].keys():
                for row in newData:
                    if row[i]==j:
                        lst[i][j].update({row["Bệnh"]: (lst[i][j][row["Bệnh"]] + 1)})

        # tính entropyOriginal
        labelSymptom = {
            "Tim": 0,
            "Phổi": 0,
            "Tiêu chảy": 0,
            "Tim, Phổi": 0,
            "Tim, Tiêu chảy": 0,
            "Phổi, Tiêu chảy": 0,
            "Tim, Phổi, Tiêu chảy": 0,
            "Khác": 0
        }
        totalRow = 0
        for row in newData:
            labelSymptom[row["Bệnh"]]+=1
            totalRow += 1

        entropyOriginal = self.getEntropyOriginal(labelSymptom)

        # tính IG
        lstIG = {}
        for label in lst.keys():
            lstEntropy = []
            lstNumEntropy= []
            for key in lst[label].keys():
                tmp = []
                tmpSum = 0
                for p in lst[label][key].keys():
                    tmp.append(lst[label][key][p])
                    tmpSum+=lst[label][key][p]
                lstEntropy.append(self.entropy(tmp))
                lstNumEntropy.append(tmpSum)

            lstIG.update({label: self.getIG(entropyOriginal, totalRow, lstEntropy, lstNumEntropy)})
        
        # print("-----------------------------")

        # chọn trường
        mx = None
        sv = None
        for label in lstIG.keys():
            if mx==None or lstIG[label]>mx:
                mx = lstIG[label]
                sv = label

        # kết luận
        lstRes = []
        if sv!=None:
            for key in lst[sv]:
                tmp = {}
                for i in labels.keys():
                    tmp.update({i: labels[i]})
                tmp.update({sv: key})
                kl = [
                    lst[sv][key]["Tim"], 
                    lst[sv][key]["Phổi"], 
                    lst[sv][key]["Tiêu chảy"], 
                    lst[sv][key]["Tim, Phổi"], 
                    lst[sv][key]["Tim, Tiêu chảy"], 
                    lst[sv][key]["Phổi, Tiêu chảy"], 
                    lst[sv][key]["Tim, Phổi, Tiêu chảy"], 
                    lst[sv][key]["Khác"]
                ]
                labelsKL = [
                    "Tim",
                    "Phổi",
                    "Tiêu chảy",
                    "Tim, Phổi",
                    "Tim, Tiêu chảy",
                    "Phổi, Tiêu chảy",
                    "Tim, Phổi, Tiêu chảy",
                    "Khác"
                ]
                totalKL = 0
                indexKL = 0
                labelKL = 0
                while indexKL<=7:
                    if kl[indexKL]!=0: 
                        totalKL+=1
                        labelKL = labelsKL[indexKL]
                    indexKL+=1
                if totalKL==1:
                    tmp.update({"Bệnh": labelKL})
                lstRes.append(tmp)
        return lstRes

    def test(self, lst):
        # print(len(data_test))
        res = {
            "Đúng": 0,
            "Sai": 0,
            "Không phân loại": 0
        }
        sv = []
        index = 0
        for row in self.data:
            index += 1
            test = "Không phân loại"
            for i in lst:
                ok = True
                for key in i.keys():
                    if key!="Bệnh":
                        if i[key]!=row[key]:
                            ok = False
                            break
                if ok: 
                    test = i["Bệnh"]
                    break

            if test==row["Bệnh"]:
                res["Đúng"]+=1
            elif test=="Không phân loại": 
                res["Không phân loại"]+=1
                print(index)
                if row not in sv: sv.append(row)
            else: 
                print(index)
                res["Sai"]+=1

        print(res)

        totalInRes = 0
        for key in res.keys(): totalInRes += res[key]
        print("Test %: ")
        for key in res.keys():
            print(key, end=": ")
            print(res[key]/totalInRes*100)

    def main(self):
        lst = []
        index = 0
        while index==0 or index<len(lst):
            if len(lst)!=0 and "Bệnh" in lst[index]:
                index += 1
            else:
                labels = {} if len(lst)==0 else lst[index]
                res = self.run(labels)
                if len(lst)!=0: lst.pop(index)
                if len(res)!=0:
                    for i in res:
                        lst.append(i)

        print("List:")
        for l in lst:
            print(l)
        print("=========" + str(len(lst)) + "========")

        self.test(lst)
        
        return lst