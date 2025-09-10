-- Actualiza Total Spent del id 8720
UPDATE `genial-stage-432712-t7.marketing_dataset.marketing_clean`
SET TotalSpent = MntFishProducts 
               + MntFruits 
               + MntGoldProds 
               + MntMeatProducts 
               + MntSweetProducts 
               + MntWines
WHERE ID = 8720;

-- Actualiza avgspentperpurchase del id 8720
UPDATE `genial-stage-432712-t7.marketing_dataset.marketing_clean`
SET AvgSpentPerPurchase = ROUND(SAFE_DIVIDE(TotalSpent, TotalPurchases), 2)
WHERE ID = 8720;

-- Actualiza age group vacíos
UPDATE `genial-stage-432712-t7.marketing_dataset.marketing_clean`
SET AgeGroup = '45-59'
WHERE AgeGroup IS NULL OR AgeGroup = '';

-- Actualiza monto en carne de registro con valor atípico
UPDATE `genial-stage-432712-t7.marketing_dataset.marketing_clean` t
SET MntMeatProducts = CAST(sub.mediana AS INT64)
FROM (
  SELECT DISTINCT PERCENTILE_CONT(MntMeatProducts, 0.5) OVER() AS mediana
  FROM `genial-stage-432712-t7.marketing_dataset.marketing_clean`
) sub
WHERE t.MntMeatProducts = 1607;

-- Actualiza TotalSpent y AvgSpentPerPurchase en clientes sin compras
UPDATE `genial-stage-432712-t7.marketing_dataset.marketing_clean`
SET 
  TotalSpent = 0,
  AvgSpentPerPurchase = 0
WHERE TotalPurchases = 0;

-- Actualiza edad en registros con valores atípicos
UPDATE `genial-stage-432712-t7.marketing_dataset.marketing_clean`
SET Age = CAST(mediana AS INT64)
FROM (
  SELECT PERCENTILE_CONT(Age, 0.5) OVER() AS mediana
  FROM `genial-stage-432712-t7.marketing_dataset.marketing_clean`
  LIMIT 1
) AS sub
WHERE Age >= 100;

-- Actualiza año de nacimiento en registros con valores inválidos
UPDATE `genial-stage-432712-t7.marketing_dataset.marketing_clean`
SET Year_Birth = CAST(mediana AS INT64)
FROM (
  SELECT PERCENTILE_CONT(Year_Birth, 0.5) OVER() AS mediana
  FROM `genial-stage-432712-t7.marketing_dataset.marketing_clean`
  LIMIT 1
) AS sub
WHERE Year_Birth <= 1900;
