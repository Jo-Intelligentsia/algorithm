-- 코드를 입력하세요
# 문제
# CAR_RENTAL_COMPANY_CAR 테이블과 CAR_RENTAL_COMPANY_RENTAL_HISTORY 테이블과 CAR_RENTAL_COMPANY_DISCOUNT_PLAN 테이블에서 자동차 종류가 '세단' 또는 'SUV' 인 자동차 중 
# 2022년 11월 1일부터 2022년 11월 30일까지 대여 가능하고 
# 30일간의 대여 금액이 50만원 이상 200만원 미만인 자동차에 대해서 
# 자동차 ID, 자동차 종류, 대여 금액(컬럼명: FEE) 리스트를 출력하는 SQL문을 작성해주세요. 
# 결과는 대여 금액을 기준으로 내림차순 정렬하고, 대여 금액이 같은 경우 자동차 종류를 기준으로 오름차순 정렬, 자동차 종류까지 같은 경우 자동차 ID를 기준으로 내림차순 정렬해주세요.
# SELECT * 
#     FROM 
#         car_rental_company_car
#         INNER JOIN car_rental_company_rental_history USING (CAR_ID)
#         INNER JOIN car_rental_company_discount_plan USING (car_type)
# WHERE 
#     where CAR_ID not in (
#         select CAR_ID
#         from CAR_RENTAL_COMPANY_RENTAL_HISTORY
#         where END_DATE > '2022-11-00'
#         and START_DATE < '2022-12-00')
# and CAR_TYPE in ('세단', 'SUV')
SELECT DISTINCT c.CAR_ID, 
    c.CAR_TYPE, 
    ROUND(c.DAILY_FEE * 30 * (100 - p.DISCOUNT_RATE) / 100) FEE
from CAR_RENTAL_COMPANY_CAR c join (select CAR_TYPE, DISCOUNT_RATE
                                    from CAR_RENTAL_COMPANY_DISCOUNT_PLAN
                                    where DURATION_TYPE = '30일 이상') p
on c.CAR_TYPE = p.CAR_TYPE
where c.CAR_ID not in (select CAR_ID
                       from CAR_RENTAL_COMPANY_RENTAL_HISTORY
                       where END_DATE > '2022-11-00'
                       and START_DATE < '2022-12-00')
and c.CAR_TYPE in ('세단', 'SUV')
having FEE >= 500000
and FEE < 2000000
order by FEE desc, c.CAR_TYPE, c.CAR_ID desc

