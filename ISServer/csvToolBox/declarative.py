#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Jeremiah Marks
# @Date:   2015-05-24 00:39:44
# @Last Modified 2015-05-24
# @Last Modified time: 2015-05-24 02:58:07

# Is is a declarative list of sql tables and data

import os
import sys
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

metadata = MetaData()
projectDevServer="sqlite://///home/jlmarks/infusImport/ISServer/csvDatabase/DEV.sqlite"
Base = declarative_base()

class Product(Base):
    __tablename__        = "Product"
    BottomHTML           = Column( String )# nullable=false    Edit Add    # Read
    CityTaxable          = Column( Integer )# Read
    CountryTaxable       = Column( Integer )# Read
    Description          = Column( String )# nullable=false    Edit Add    # Read
    HideInStore          = Column( Integer )
    Id                   = Column( Integer, primary_key=True )# Read
    InventoryLimit       = Column( Integer )
    InventoryNotifiee    = Column( String(250) )# nullable=false    Edit Add    # Read
    IsPackage            = Column( Integer )
    LargeImage           = Column( BLOB )
    NeedsDigitalDelivery = Column( Integer )
    ProductName          = Column( String )# nullable=false    Edit Add    # Read
    ProductPrice         = Column( Float )
    Shippable            = Column( Integer )
    ShippingTime         = Column( String(250) )# nullable=false    Edit Add    # Read
    ShortDescription     = Column( String )# nullable=false    Edit Add    # Read
    Sku                  = Column( String(250) )# nullable=false    Edit Add    # Read
    StateTaxable         = Column( Integer )
    Status               = Column( Integer )
    Taxable              = Column( Integer )
    TopHTML              = Column( String )# nullable=false    Edit Add    # Read
    Weight               = Column( Float )
class ProductCategory(Base):
    __tablename__ = "Productcategory"
    CategoryDisplayName = Column( String(250) )# nullable=false    Edit Delete Add    # Read
    CategoryImage = Column( BLOB )
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
    AllowSpaces = Column( Integer, default=1 )
    CanContain = Column( String(250) )# nullable=false    Edit Delete Add    # Read
    CanEndWith = Column( Integer )
    CanStartWith = Column( String(250) )# nullable=false    Edit Delete Add    # Read
    Id = Column( Integer, primary_key=True )
    IsRequired = Column( Integer, default=0 )
    Label = Column( String(250) )# nullable=false    Edit Delete Add    # Read
    MaxChars = Column( Integer )
    MinChars = Column( Integer )
    Name = Column( String(250) )# nullable=false    Edit Delete Add    # Read
    OptionType = Column(Enum('FixedList', 'SomethingElse', name='option_types') )
    Order = Column( Integer )
    ProductId = Column( Integer, ForeignKey('Product.Id') )
    StringMessage = Column( Integer )
 
# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
def process():
    engine = create_engine(projectDevServer) 
    # Create all tables in the engine. This is equivalent to "Create Table"
    # statements in raw SQL.
    Base.metadata.create_all(engine)