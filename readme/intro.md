童话商场项目：



## 数据库：

已完成：

​	用户信息、商品信息、商品关键词（可以用于检索和分类）、购物记录

​	约束：主键、外键（级联删除）、触发器



---

待完成：

​	视图、用户权限、添加一些表来增加网页功能（购物车）

​	以及一些安全性问题（防sql注入）



## Web：

已完成：

1. 注册页面：注册功能（密码加密保存）、查看用户守则（弹出新网页）、登录入口

2. 登录页面：注册入口、登录功能、登录状态保持

3. 个人主页：登出、个人信息展示

4. 商品展示和购买页：商品信息展示，购买表单提交

   

---

待完成/改进：

1. 注册：提示用户名和密码条件，使用jquery对注册用户名是否重复进行后台查询，实时返回结果，以及用户守则编写。

2. 登录：第三方登录功能

3. 用户：修改密码功能、历史购买记录查询、购物车

4. 商品：购物功能（仍无法提交购买表单到后台），商品图片（Redis图片缓存），商品分类/搜索功能，翻页

5. 网页实时更新：不需要重新加载网页就能更新网页内容

6. 网页美观性：css布局还可以再优化，或者使用一些模板

7. 用户说明书

   

---

演示：

​	注册：

​	登录：

​	个人主页：

​	商品页：

​	登出：

​	数据库购买insert触发器

