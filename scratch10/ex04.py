import pandas as pd

from scratch10.ex02 import peak_to_peak

if __name__ == '__main__':
    #tips.csv 파일을 읽어서 파일에서 데이터 프레임 생성
    tips_df = pd.read_csv('tips.csv')
    # 앞 5개의 데이터 출력
    # print(tips_df.head())
    print(tips_df.iloc[0:5])
    print(tips_df.shape) # df에 colnames가 제대로 들어갔는지 확인하기 위해!

    # 데이터 프레임에 tip_pct컬럼 추가: tip_pct = tip/total
    # tip_pct = tips_df['tip']/tips_df['total_bill']
    # tips_df['tip_pct'] = tip_pct #abajo en una linea! mejor :)
    tips_df['tip_pct'] = tips_df['tip']/tips_df['total_bill']
    print(tips_df.head())

    # day, smoker 별 그룹을 지어서 tip_pct의 평균을 출력
    grouped = tips_df.groupby(['day','smoker'])

    # 요일별 팁의 평균에 차이가 나는지, 비/흡연가별 팁 평균에 차이가 나는지
    tip_by_day_smoker = grouped['tip_pct']
    print(tip_by_day_smoker.mean())
    # above one line and below two lines are the same code
    # result_tipds = tip_by_day_smoker.agg('mean')
    # print(result_tipds) # or #print(tip_by_day_smoker.agg('mean'))

    # day, smoker별 그룹의 tip_pct의 평균, 표준편차, 최대/최소 차이
    result_tipds = tip_by_day_smoker.agg(['mean', 'std', peak_to_peak])
    print(result_tipds)

    # day, smoker별 그룹의 tip_pct, total_bill 의 평균, 표준편차, 최대/최소 차이
    grouped_pct_bill = grouped[['tip_pct','total_bill']]
    print(grouped_pct_bill.agg(['mean','std', peak_to_peak]))
    print(grouped_pct_bill.agg([('average','mean'),
                                ('std-dev','std'),
                                ('range',peak_to_peak)]))

    # 키워드 argument -> 안된다

    # GroupBy 객체의 컬럼들마다 다른 함수를 agg로 적용하고 싶은 때
    # agg({'col_name':[functions], ...})
    # groupby 객체에 있는 컬럼이름
    # grouping된 데이터 프레임에 tip 컬럼에는 max() 함수를 aggregate 하고,
    # 싸이즈 컬럼에는 sum()함수를 aggregate함.
    result = grouped.agg({'tip':'max','size':'max'})
    print(result)

    functions = ['mean','std',peak_to_peak]
    result = grouped.agg({
        'tip_pct': functions,
        'total_bill': functions
    })
    print(result)

    # we can also give them names
    functions = [('mu', 'mean'), ('sigma','std'),
                 ('range', peak_to_peak) ]
    result = grouped.agg({
        'tip_pct': functions,
        'total_bill': functions
    })
    print(result)

    # grouping 컬럼들이 aggregate 결과에서 인덱스로 사용하지 않고자 할 때,
    groupt = tips_df.groupby(['day','smoker'], as_index = False)
    print(grouped['tip'].mean())
    


























