from sqlalchemy import create_engine
from cubes.tutorial.sql import create_table_from_csv

engine = create_engine('sqlite:///data.sqlite')

create_table_from_csv(engine,
                      "IBRD_Balance_Sheet__FY2010.csv",
                      table_name="ibrd_balance",
                      fields=[
                            ("category", "string"),
                            ("category_label", "string"),
                            ("subcategory", "string"),
                            ("subcategory_label", "string"),
                            ("line_item", "string"),
                            ("year", "integer"),
                            ("amount", "integer")],
                      create_id=True
                  )


from cubes import Workspace

workspace = Workspace()
workspace.register_default_store("sql", url="postgresql://postgres:N#123456@localhost/willowood")
workspace.import_model("Sales_model.json")

browser = workspace.browser("clv_sales_registerFCube")

result = browser.aggregate()

print(result.summary["record_count"])

print(result.summary["amount_sum"])

result = browser.aggregate(drilldown=["fiscal_year"])

for record in result:
    print(' record: ', record)