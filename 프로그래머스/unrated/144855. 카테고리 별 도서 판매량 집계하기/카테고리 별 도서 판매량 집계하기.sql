-- 코드를 입력하세요
# 문제
# 2022년 1월의 카테고리 별 도서 판매량을 합산하고, 
# 카테고리(CATEGORY), 총 판매량(TOTAL_SALES) 리스트를 출력하는 SQL문을 작성해주세요.
# 결과는 카테고리명을 기준으로 오름차순 정렬해주세요.

# select a.category, sum(b.sales) as total_sales
# from book a
#     join book_sales b on a.book_id = b.book_id
# where date_format(b.sales_date, '%Y-%m') = '2022-01'
# group by a.category
# order by 1;

SELECT category, SUM(sales) AS total_sales
FROM book
    JOIN book_sales on book.book_id = book_sales.book_id
WHERE DATE_FORMAT(sales_date, '%Y-%m') = '2022-01'
GROUP BY category
order by category;