def HellowWorld():
    #基本資料
    name = input()

    id_s = input()
    id = int(id_s)
    #輸入學生成績
    S1_score_s = input()
    S1_score = int(S1_score_s)
    
    S2_score_s = input()
    S2_score = int(S2_score_s)

    S3_score_s = input()
    S3_score = int(S3_score_s)
    #平均
    Total = S1_score + S2_score + S3_score
    Average = int(Total / 3)
    
    name = "Name:"+name
    id = "Id:"+str(id)
    Total = "Total:"+str(Total)
    Average = "Average:"+str(Average)

    print(name)
    print(id)
    print(Total)
    print(Average)
    
def main():
    HellowWorld()

main()