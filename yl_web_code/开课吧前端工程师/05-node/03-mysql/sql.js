// sql 增、删、改、查； 对于数据操作； crud(create/update/retrieve/delete);
// 增：
// INSERT INTO users(字段一,字段二,字段三) VALUES ("值一"，"值二"，值三);
// 删：（假删除：通过更新代替删除）； is_delete:
// DELETE FROM 表名 条件语句；

// 修改：
// UPDATE 表名 SET 字段=’值‘ 条件语句;

// 查：
// SELECT * FROM 表名 条件语句；
// 条件 年龄=20；
// SELECT * FROM 表名 WHERE age=20;

// = > < ;
// SELECT username,age FROM users WHERE age=20;
// 选取字段 SELECT 字段一,字段二... FROM users WHERE age=20;
// OR  AND;
// SELECT * FROM users WHERE age=20 AND username='李四';
// SELECT * FROM users WHERE age=20 OR age=21;

// 排列：正序ASC、倒叙DESC；
// SELECT * FROM users ORDER BY age ASC;

// 分页相关；LIMIT 限制；
// perPage = 5; p=1;
// SELECT * FROM users LIMIT 0,5;

// SELECT * FROM users WHERE id>1 ORDER BY age LIMIT 0,5;

// 查询姓李的数据
// SELECT * FROM users WHERE username LIKE "李%";

// AS  JOIN ON  ;联表查询；
// SELECT * FROM products AS p LEFT JOIN users AS u ON p.uid=u.id;
