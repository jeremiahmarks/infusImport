class Product(Base):
    __tablename__        = "Product"
    BottomHTML           = Column( Text )# nullable=false    Edit Add    # Read
    CityTaxable          = Column( Integer )# Read
    CountryTaxable       = Column( Integer )# Read
    Description          = Column( Text )# nullable=false    Edit Add    # Read
    HideInStore          = Column( Integer )
    Id                   = Column( Integer, primary_key=True )# Read
    InventoryLimit       = Column( Integer )
    InventoryNotifiee    = Column( String(250) )# nullable=false    Edit Add    # Read
    IsPackage            = Column( Integer )
    LargeImage           = Column( Blob )
    NeedsDigitalDelivery = Column( Integer )
    ProductName          = Column( Text )# nullable=false    Edit Add    # Read
    ProductPrice         = Column( Float )
    Shippable            = Column( Integer )
    ShippingTime         = Column( String(250) )# nullable=false    Edit Add    # Read
    ShortDescription     = Column( Text )# nullable=false    Edit Add    # Read
    Sku                  = Column( String(250) )# nullable=false    Edit Add    # Read
    StateTaxable         = Column( Integer )
    Status               = Column( Integer )
    Taxable              = Column( Integer )
    TopHTML              = Column( Text )# nullable=false    Edit Add    # Read
    Weight               = Column( Float )
class ProductCategory(Base):
    __tablename__ = "Productcategory"
    CategoryDisplayName = Column( String(250) )# nullable=false    Edit Delete Add    # Read
    CategoryImage = Column( Blob )
    CategoryOrder = Column( Integer )
    Id = Column( Integer, primary_key=True )# Read
    ParentId = Column( Integer, ForeignKey('Productcategory.Id'))
class ProductCategoryAssign( Base):
    __tablename__ = "Productcategoryassign"
    Id = Column( Integer, primary_key=True )# Read
    ProductCategoryId = Column( Integer, ForeignKey('Productcategory.Id'))
    ProductId = Column( Integer, ForeignKey('Product.Id') )
class ProductInterest(Base):
    __tablename__ = "Productinterest"
    DiscountPercent = Column( Integer )
    Id = Column( Integer, primary_key=True )# Read
    ObjType = Column( String(250) )# nullable=false    Edit Delete Add    # Read
    ObjectId = Column( Integer )
    ProductId = Column( Integer, ForeignKey('Product.Id') )
    ProductType = Column( String(250) )# nullable=false    Edit Delete Add    # Read
    Qty = Column( Integer )
class ProductInterestBundle(Base):
    __tablename__ = "Productinterestbundle"
    BundleName = Column( String(250) )# nullable=false    Edit Add    # Read
    Description = Column( String(250) )# nullable=false    Edit Add    # Read
    Id = Column( Integer, primary_key=True )# Read
class ProductOptValue(Base):
    __tablename__ = "Productoptvalue"
    Id = Column( Integer, primary_key=True )
    IsDefault = Column( Integer )
    Label = Column( String(250) )# nullable=false    Edit Delete Add    # Read
    Name = Column( String(250) )# nullable=false    Edit Delete Add    # Read
    OptionIndex = Column( Integer )
    PriceAdjustment = Column( Float )
    ProductOptionId = Column( Integer, ForeignKey('Productoption.Id') )
    Sku = Column( String(250) )# nullable=false    Edit Delete Add    # Read
class ProductOption( Base):
    __tablename__ = "Productoption"
    AllowSpaces = Column( Integer  default=1 )
    CanContain = Column( String(250) )# nullable=false    Edit Delete Add    # Read
    CanEndWith = Column( Integer )
    CanStartWith = Column( String(250) )# nullable=false    Edit Delete Add    # Read
    Id = Column( Integer, primary_key=True )
    IsRequired = Column( Integer default=0 )
    Label = Column( String(250) )# nullable=false    Edit Delete Add    # Read
    MaxChars = Column( Integer )
    MinChars = Column( Integer )
    Name = Column( String(250) )# nullable=false    Edit Delete Add    # Read
    OptionType = Column(Enum('FixedList', 'SomethingElse', name='option_types') )
    Order = Column( Integer )
    ProductId = Column( Integer, ForeignKey('Product.Id') )
    TextMessage = Column( Integer )