import sqlite3
projectDevServer="home/jlmarks/infusImport/ISServer/csvDatabase/DEV.sqlite"
# engine=create_engine(projectDevServer)
# cursor.execute('''
#     CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT,
#                        phone TEXT, email TEXT unique, password TEXT)
# ''')
db=sqlite3.connect("/home/jlmarks/infusImport/ISServer/csvDatabase/DEV.sqlite")
cursor=db.cursor()
tablenames=[
    "Product",
    "Productcategory",
    "Productcategoryassign",
    "Productinterest",
    "Productinterestbundle",
    "Productoptvalue",
    "Productoption",
    ]
for eachTable in tablenames:
    cursor.execute("DROP TABLE IF EXISTS "+ eachTable)
allCreationStrings=[]

allCreationStrings.append("""CREATE TABLE Product(
    BottomHTML Text,
    CityTaxable Integer,
    CountryTaxable Integer,
    Description Text,
    HideInStore Integer,
    Id Integer, primary_key=True,
    InventoryLimit Integer,
    InventoryNotifiee String(250),
    IsPackage Integer,
    LargeImage BLOB,
    NeedsDigitalDelivery Integer,
    ProductName Text,
    ProductPrice Float,
    Shippable Integer,
    ShippingTime String(250),
    ShortDescription Text,
    Sku String(250),
    StateTaxable Integer,
    Status Integer,
    Taxable Integer,
    TopHTML Text,
    Weight Floa)
)""")
allCreationStrings.append("""CREATE TABLE Productcategory(
    CategoryDisplayName String(250),
    CategoryImage BLOB,
    CategoryOrder Integer,
    Id Integer, primary_key=True,
    ParentId Integer, ForeignKey('Productcategory.Id)
))""")
allCreationStrings.append("""CREATE TABLE Productcategoryassign(
    Id Integer, primary_key=True,
    ProductCategoryId Integer, ForeignKey('Productcategory.Id',
    ProductId Integer, ForeignKey('Product.Id')
)""")
allCreationStrings.append("""CREATE TABLE Productinterest(
    DiscountPercent Integer,
    Id Integer, primary_key=True,
    ObjType String(250),
    ObjectId Integer,
    ProductId Integer, ForeignKey('Product.Id'),
    ProductType String(250),
    Qty Intege)
)""")
allCreationStrings.append("""CREATE TABLE Productinterestbundle(
    BundleName String(250),
    Description String(250),
    Id Integer, primary_key=Tru)
)""")
allCreationStrings.append("""CREATE TABLE Productoptvalue(
    Id Integer, primary_key=True,
    IsDefault Integer,
    Label String(250),
    Name String(250),
    OptionIndex Integer,
    PriceAdjustment Float,
    ProductOptionId Integer, ForeignKey('Productoption.Id'),
    Sku String(250)
)""")
allCreationStrings.append("""CREATE TABLE Productoption(
    AllowSpaces Integer,  default=1,
    CanContain String(250),
    CanEndWith Integer,
    CanStartWith String(250),
    Id Integer, primary_key=True,
    IsRequired Integer, default=0,
    Label String(250),
    MaxChars Integer,
    MinChars Integer,
    Name String(250),
    OptionTypeEnum('FixedList', 'SomethingElse', name='option_types'),
    Order Integer,
    ProductId Integer, ForeignKey('Product.Id'),
    TextMessage Intege)
)""")


