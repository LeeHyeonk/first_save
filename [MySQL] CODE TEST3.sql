-- 몇시에 입양이 가장 활발하게 일어나는지 알아보자., 시간순서대로 정렬
-- ANIMAL_OUTS 입양보낸 동물의 정보를 담은 테이블
-- ANIMAL_ID, ANIMAL_TYPE, DATETIME, NAME, SEX_UPON_OUTCOM : 동물의 아이디, 생물 종, 입양일, 이름, 성별 및 중성화 여부
-- DATETIME : 입양일 및 시간 데이터 (예: 2013-12-15 17:10:00 )


# 시간을 0부터 23시까지 보여주는 서브쿼리 함수 (재귀)
WITH RECURSIVE phours AS (
	SELECT 0 AS hour
	UNION ALL
	SELECT hour + 1 FROM phours
	WHERE hour < 23
)

#시간테이블과 각 시간일 경우에 동물들의 수 테이블을 left join 시킨 후, HOUR로 올림차순 정렬
SELECT P.hour AS HOUR, COUNT(A.ANIMAL_ID) AS COUNT
FROM phours P
LEFT JOIN ANIMAL_OUTS A on P.hour = HOUR(A.DATETIME)
GROUP BY HOUR
ORDER BY HOUR
