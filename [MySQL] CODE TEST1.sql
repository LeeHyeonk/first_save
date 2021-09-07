-- SQL code test Level 4 : 우유와 요거트가 담긴 장바구니
-- 우유와 요거트를 동시에 구입한 장바구니의 아이디 조회하기
-- MYSQL 기준으로 작성됨.

SELECT DISTINCT B.CART_ID
FROM CART_PRODUCTS B
WHERE B.CART_ID IN (
        SELECT A.CART_ID
        FROM CART_PRODUCTS A
        WHERE A.NAME = 'Milk')
    AND B.NAME = 'Yogurt'
ORDER BY B.CART_ID ASC;
