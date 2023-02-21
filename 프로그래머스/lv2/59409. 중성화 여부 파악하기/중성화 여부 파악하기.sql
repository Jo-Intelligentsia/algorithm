-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME,
    CASE 
        WHEN sex_upon_intake = 'Neutered Male' THEN 'O'
        WHEN sex_upon_intake = 'Spayed Female' THEN 'O'
        ELSE 'X'
        
    END '중성화'
FROM animal_ins