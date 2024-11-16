dob = "15022005"


def n_bn(n):
    if n < 10:
        return f'0{n}'
    else:
        return str(n)
def pif_sqr(dob:str):
    ch = ['очень слабовыраженное качество',"слабовыраженное качество","удовлетворительно развитое","нормально развитое качество","сильно развитое","предельно развитое"," избыток качества"]
    qualities = ["Характер","Энергия","Наука","Здоровье","Логика","Труд","Удача","Долг","Ум"]

    dob_list = [int(s) for s in dob]
    bn_1 = sum(dob_list)
    bn_2 = bn_1%10 + bn_1//10
    bn_3 = bn_1 - 2*dob_list[0]
    bn_4 = bn_3%10 + bn_3//10

    bn_1 = n_bn(bn_1)
    bn_2 = n_bn(bn_2)
    bn_3 = n_bn(bn_3)
    bn_4 = n_bn(bn_4)
    nd_str = bn_1 + bn_3 + bn_2 + bn_4

    p_sqr = [0] * 9
    for i in range(1,10):
        p_sqr[i-1] = dob.count(str(i)) + nd_str.count(str(i))

    result = {}
    for i in range(9):
        result[qualities[i]] = ch[p_sqr[i]]
    return result


d = str(input("введите дату рождения : "))
sqr = pif_sqr(d)
for i in sqr:
    print(i,":",sqr[i])