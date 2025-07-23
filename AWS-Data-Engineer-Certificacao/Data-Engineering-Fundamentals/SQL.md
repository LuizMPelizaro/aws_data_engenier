#tema/fundamentals  
O exame de certificação espera que você tenha **conhecimento sólido de SQL**, pois é uma ferramenta fundamental no dia a dia de qualquer engenheiro de dados.

---

## 📊 Agregações Básicas

### `COUNT`
Conta o número total de linhas (ou valores não nulos de uma coluna).

```sql
SELECT COUNT(*) AS total_rows FROM employees;
```
### `SUM`

Soma os valores de uma coluna numérica.
```sql
SELECT SUM(salary) AS total_salary FROM employees;
```
### AVG
Para obter a média
```sql
SELECT AVG(salary) AS  mean_salary FROM employees;
```

### MAX / MIN 
Para obter o maximo e o minimo.
```sql
SELECT MAX(salary) AS  max_salary FROM employees;
SELECT MIN(salary) AS  min_salary FROM employees;
```

## Agregação com CASE

### WHERE
É um filtro para apenas uma condição expecifica, ex. pegar todos funcionarios que ganham acima de 10000
```sql
SELECT COUNT(salary) AS high_salary_count FROM employees WHERE salary > 10000;
```

### Usando `CASE` para múltiplas condições em uma mesma agregação
```sql
SELECT 
	COUNT(CASE WHEN salary > 70000 THEN 1 END) AS high_salary_count,
	COUNT(CASE WHEN salary BETWEEN 50000 AND 70000 THEN 1 END) AS medium_salary_count,
	COUNT(CASE WHEN salary < 50000 THEN 1 END) AS low_salary_count
FROM employees;
```

## Agrupamento (`GROUP BY`)
Agrupar dados por uma ou mais colunas para aplicar funções de agregação.
Exemplo: contar funcionários por departamento após 2020:

```SQL
SELECT departament_id, COUNT(*) AS number_of_employees
FROM employees
WHERE join_date > '2020-01-01'
GROUP BY departament_id
```

## Agrupamento com Ordenação (`ORDER BY`)

Exemplo: total de vendas por produto por ano, ordenado pelas vendas.
```SQL
SELECT YEAR(sale_date) AS sale_year, product_id, SUM(amount) AS total_sales
FROM sales
GROUP BY sale_year, product_id
ORDER BY sale_year, total_sales DESC;
```

## Pivotamento
Pivot com `PIVOT` (suporte depende do SGBD)
* Pivoting é o ato de transformar dados em nível de linha em dados colunares.
* Como isso funciona é muito específico do banco de dados. Alguns têm comando PIVOT.
* Por exemplo imagine que temos dados de venda por funcionários e temos a quantidade que eles venderam por mês.
```SQL
SELECT salesperson, [Jan] AS Jan_sales, [Feb] AS Feb_sales
FROM (
SELECT salesperson, month, sales FROM sales) AS sourceTable
PIVOT(
	SUM(sales),
	FROM month IN ([Jan],[Feb])
) AS PivotTable
```
Esse será o resultado:
![[Pasted image 20250721175254.png]]

### Pivot com Agregação Condicional (forma universal)
* Funciona em qualquer banco de dados relacional::
```SQL
SELECT 
	salesperson,
	SUM(CASE WHEN month = 'Jan' THEN sales ELSE 0 END) AS Jan_sales
	SUM(CASE WHEN month = 'Feb' THEN sales ELSE 0 END) AS Feb_sales
FROM sales
GROUP BY salesperson;
```

## Joins 

### INNER JOIN 
Retorna **apenas os registros com correspondência** entre as tabelas.
```SQL
SELECT c.customerName, p.paymentDate, p.amount
FROM customers c 
INNER JOIN payments p ON c.customerNumber = p.customerNumber
```
### LEFT OTHER JOIN
Retorna **todos os registros da tabela da esquerda**, mesmo que não haja correspondência na direita.
```SQL
SELECT c.customerName, p.paymentDate, p.amount
FROM customers c 
LEFT JOIN payments p ON c.customerNumber = p.customerNumber
```
### RIGHT OTHER JOIN 
Retorna **todos os registros da tabela da direita**, com ou sem correspondência na esquerda.
```SQL
SELECT c.customerName, p.paymentDate, p.amount
FROM customers c 
RIGHT JOIN customers p ON c.customerNumber = p.customerNumber
```
### FULL OTHER JOIN
Retorna **todos os registros das duas tabelas**, combinando quando possível, e preenchendo com `NULL` quando não houver correspondência. Útil para detectar **inconsistências**.
```sql
SELECT c.customerName, p.paymentDate, p.amount
FROM customers c
FULL OUTER JOIN payments p ON c.customerNumber = p.customerNumber;
```
### CROSS OUTER JOIN 
Produz o **produto cartesiano** entre as tabelas — todas as combinações possíveis.

```sql
SELECT c.customerName, p.paymentDate, p.amount
FROM payments p
CROSS JOIN customers c 
```
### Tipos de join existentes
![[Pasted image 20250721181342.png]]

## Expressões Regulares no SQL

### Operadores:

- `~` → case-sensitive
- `~*` → case-insensitive
- `!~*` → negação (não corresponde), insensível a maiúsculas/minúsculas

### Metacaracteres úteis:

- `^` → início da string
- `$` → fim da string ($boo não acha book mas acha boo , pois procura só pelo final da string)
- `|` → alternância (ou)
- `[a-z]` → range de caracteres
- `[a-z]{4}` → exatamente 4 letras minúsculas
- `\d` → dígitos (0–9)
- `\w` → caracteres alfanuméricos
- `\s` → espaço
- `\t` → tabulação
### Exemplo 
```sql
 SELECT * FROM  name WHERE name ~*'^(fire|ice);
```
 
Retorna todas as linhas que tiverem nomes que comecem com "fire" ou "ice" (case insensitive)
