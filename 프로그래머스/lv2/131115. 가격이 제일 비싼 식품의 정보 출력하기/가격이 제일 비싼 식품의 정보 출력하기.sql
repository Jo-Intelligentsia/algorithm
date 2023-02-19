-- 코드를 입력하세요
# 문제
# FOOD_PRODUCT 테이블에서 가격이 제일 비싼 식품의 
# 식품 ID, 식품 이름, 식품 코드, 식품분류, 식품 가격을 조회하는 SQL문을 작성해주세요.
SELECT  
    *
FROM    
    FOOD_PRODUCT
WHERE PRICE = (SELECT MAX(PRICE) FROM FOOD_PRODUCT );    
# SELECT * from food_product;