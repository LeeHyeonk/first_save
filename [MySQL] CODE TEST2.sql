-- 보호소에 들어올때 중성화 되지 않은 동물들 중에서, 나갈때 중성화 된 동물들 조회.
-- ANIMALS_INS : 보호소에 들어올때의 동물들의 정보
-- ANIMALS_OUTS : 보호소에서 나갈때의 동물들의 정보
-- SEX_UPON_INTAKE는 중성화 여부를 나타내는 컬럼이며, Intact로 시작하는 정보가 중성화가 되지 않았음을 나타낸다.
-- 들어올때엔 Intact 즉 중성화를 하지 않았으며, 나갈때는 Intact로 시작하지 않은 데이터를 조회하는 방법으로 구현.

SELECT A.ANIMAL_ID, A.ANIMAL_TYPE, A.NAME
FROM ANIMAL_INS A, ANIMAL_OUTS B
WHERE A.ANIMAL_ID = B.ANIMAL_ID
    AND LEFT(A.SEX_UPON_INTAKE, 6) = 'Intact'
    AND LEFT(B.SEX_UPON_OUTCOME, 6) != 'Intact'
