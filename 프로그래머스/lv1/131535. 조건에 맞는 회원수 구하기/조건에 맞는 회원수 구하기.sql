-- 코드를 입력하세요
# 문제
# USER_INFO 테이블에서 2021년에 가입한 회원 중 나이가 20세 이상 29세 이하인 회원이 몇 명인지 출력하는 SQL문을 작성해주세요.
SELECT COUNT(USER_ID) AS USERS FROM USER_INFO
WHERE YEAR(joined) = 2021
AND AGE BETWEEN 19 AND 29