# from sqlalchemy import create_engine
# from cubes.tutorial.sql import create_table_from_csv

# engine = create_engine('sqlite:///data.sqlite')
#
# create_table_from_csv(engine,
#                       "IBRD_Balance_Sheet__FY2010.csv",
#                       table_name="ibrd_balance",
#                       fields=[
#                             ("category", "string"),
#                             ("category_label", "string"),
#                             ("subcategory", "string"),
#                             ("subcategory_label", "string"),
#                             ("line_item", "string"),
#                             ("year", "integer"),
#                             ("amount", "integer")],
#                       create_id=True
#                   )


from cubes import Workspace

workspace = Workspace()
workspace.register_default_store("sql", url="postgresql://postgres:N#123456@localhost/willowood")
workspace.import_model("SalesTable.json")

browser = workspace.browser("salestable")

result = browser.aggregate()

print(result.summary["record_count"])

print(result.summary["Qty"])
print(result.summary["Value"])

result = browser.aggregate(drilldown=["billing_date"])

for record in result:
    print(' record: ', record)