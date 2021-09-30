import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import datetime


def get_info(item):
    try:
        stdr_de_id = item.find('stdr_de_id')
        signgu_nm = item.find('signgu_nm')
        tot_lvpop_co = item.find('tot_lvpop_co')
        lvpop_co = item.find('lvpop_co')
        lngtr_stay_frgnr_co = item.find('lngtr_stay_frgnr_co')
        srtpd_stay_frgnr_co = item.find('srtpd_stay_frgnr_co')
        dail_mxmm_lvpop_co = item.find('dail_mxmm_lvpop_co')
        dail_mumm_lvpop_co = item.find('dail_mumm_lvpop_co')
        day_lvpop_co = item.find('day_lvpop_co')
        night_lvpop_co = item.find('night_lvpop_co')
        dail_mxmm_mvmn_lvpop_co = item.find('dail_mxmm_mvmn_lvpop_co')
        su_else_inflow_lvpop_co = item.find('su_else_inflow_lvpop_co')
        sam_adstrd_mvmn_lvpop_co = item.find('sam_adstrd_mvmn_lvpop_co')
        signgu_mvmn_lvpop_co = item.find('signgu_mvmn_lvpop_co')
    except:
        print('No data')

    return {"기간": stdr_de_id.text, "지역구": signgu_nm.text, "총생활인구수": tot_lvpop_co.text, "내국인생활인구수": lvpop_co.text,
            "장기체류외국인인구수": lngtr_stay_frgnr_co.text, "단기체류외국인인구수": srtpd_stay_frgnr_co.text,
            "일최대인구수": dail_mxmm_lvpop_co.text, "일최소인구수": dail_mumm_lvpop_co.text, "주간인구수(09~18)": day_lvpop_co.text,
            "야간인구수(19~08)": night_lvpop_co.text, "일최대이동인구수": dail_mxmm_mvmn_lvpop_co.text,
            "서울외유입인구수": su_else_inflow_lvpop_co.text, "동일자치구행정동간이동인구수": sam_adstrd_mvmn_lvpop_co.text,
            "자치구간이동인구수": signgu_mvmn_lvpop_co.text}

def get_page_info(url) :
    global day
    result = requests.get(url) # api 서비스 호출
    bs_obj = BeautifulSoup(result.content,"html.parser")
    items = bs_obj.findAll('row')
    prod_info_list = [get_info(item) for item in items]

    return prod_info_list


day = datetime.datetime(2018,4,4)
df_fin = pd.DataFrame()
for i in range(1, 1000) :

    day_p = (day + datetime.timedelta(days=i)).strftime('%y%m%d')
    if day_p >= '200101' :
        break
    key = '63436c636c77686636305077534b45'
    url = 'http://openapi.seoul.go.kr:8088/'+ key + '/xml/SPOP_DAILYSUM_JACHI/1/100/20'+ day_p
    page_product = get_page_info(url)
    df = pd.DataFrame(page_product)
    df_fin = pd.concat([df_fin,df],axis=0,ignore_index=True)

#df_fin.to_csv('./프젝_2_유동인구2.csv')