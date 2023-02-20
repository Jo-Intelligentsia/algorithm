-- 코드를 입력하세요
# 문제
# CAR_RENTAL_COMPANY_RENTAL_HISTORY 테이블에서 2022년 10월 16일에 대여 중인 자동차인 경우 '대여중' 이라고 표시하고, 
# 대여 중이지 않은 자동차인 경우 '대여 가능'을 표시하는 컬럼(컬럼명: AVAILABILITY)을 추가하여 
# 자동차 ID와 AVAILABILITY 리스트를 출력하는 SQL문을 작성해주세요. 
# 이때 반납 날짜가 2022년 10월 16일인 경우에도 '대여중'으로 표시해주시고 결과는 자동차 ID를 기준으로 내림차순 정렬해주세요.
SELECT car_id,
    CASE
        WHEN max(end_date) >= '2022-10-16' THEN '대여중'
    ELSE '대여 가능'
    END AS AVAILABILITY
FROM 
    CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE start_date <= '2022-10-16'
GROUP BY car_id
ORDER BY car_id DESC;   

# SELECT DATE_FORMAT(start_date, '%Y-%m-%d') FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
# WHERE DATE_FORMAT(start_date, '%Y-%m-%d') IS '2022-10-16'

# SELECT CAR_ID, if(max(END_DATE) >= '2022-10-16', '대여중', '대여 가능') AVAILABILITY
# from CAR_RENTAL_COMPANY_RENTAL_HISTORY
# where START_DATE <= '2022-10-16'
# group by CAR_ID
# order by CAR_ID desc;
# SELECT * FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
# ORDER BY car_id