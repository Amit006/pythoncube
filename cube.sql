
drop table ibrd_balance;

create table ibrd_balance(
		Category_Code varchar(200),
		Category varchar(200),
		Subcategory_Code varchar(200),
		Subcategory varchar(200),
		Line_Item varchar(200),
		Fiscal_Year varchar(200),
		Amount  float(53)
)