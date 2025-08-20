SELECT category, AVG(sale.price) AS avg_profit, COUNT(sale.id) AS sold_count
FROM products
JOIN sales ON products.id = sales.product_id
GROUP BY category
ORDER BY avg_profit DESC, sold_count DESC
LIMIT 10;