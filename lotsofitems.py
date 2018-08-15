from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Category, CategoryItem, User

engine = create_engine('sqlite:///catalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

# Create category for Faith
category1 = Category(user_id=1, name="Faith")

session.add(category1)
session.commit()


categoryItem1 = CategoryItem(user_id=1, name="Psalm 9:10", description="Those who know your name trust in you, for you, LORD, have never forsaken those who seek you.",
                     category=category1)

session.add(categoryItem1)
session.commit()

categoryItem2 = CategoryItem(user_id=1, name="2 Chronicles 20:20", description="Have faith in the LORD your God and you will be upheld; have faith in his prophets and you will be successful.",
                     category=category1)

session.add(categoryItem2)
session.commit()

categoryItem3 = CategoryItem(user_id=1, name="Psalm 46:10", description="Be still, and know that I am God.",
                     category=category1)

session.add(categoryItem3)
session.commit()


# Create category for Hope
category2 = Category(user_id=1, name="Hope")

session.add(category2)
session.commit()


categoryItem1 = CategoryItem(user_id=1, name="Jeremiah 29:11", description="For I know the plans I have for you, declares the Lord, plans for welfare and not for evil, to give you a future and a hope.",
                     category=category2)

session.add(categoryItem1)
session.commit()

categoryItem2 = CategoryItem(user_id=1, name="Romans 15:13", description="May the God of hope fill you with all joy and peace in believing, so that by the power of the Holy Spirit you may abound in hope.",
                     category=category2)

session.add(categoryItem2)
session.commit()

categoryItem3 = CategoryItem(user_id=1, name="Romans 12:12", description="Rejoice in hope, be patient in tribulation, be constant in prayer.",
                     category=category2)

session.add(categoryItem3)
session.commit()


# Create category for Love
category3 = Category(user_id=1, name="Love")

session.add(category3)
session.commit()


categoryItem1 = CategoryItem(user_id=1, name="1 Corinthians 13:13", description="And now these three remain: faith, hope and love. But the greatest of these is love.",
                     category=category3)

session.add(categoryItem1)
session.commit()

categoryItem2 = CategoryItem(user_id=1, name="Romans 13:10", description="Love does no harm to a neighbor. Therefore love is the fulfillment of the law.",
                     category=category3)

session.add(categoryItem2)
session.commit()

categoryItem3 = CategoryItem(user_id=1, name="1 John 4:11", description="Dear friends, since God so loved us, we also ought to love one another.",
                     category=category3)

session.add(categoryItem3)
session.commit()


# Create category for Thankfulness
category4 = Category(user_id=1, name="Thankfulness")

session.add(category4)
session.commit()


categoryItem1 = CategoryItem(user_id=1, name="1 Chronicles 16:34", description="Give thanks to the LORD, for he is good; his love endures forever.",
                     category=category4)

session.add(categoryItem1)
session.commit()

categoryItem2 = CategoryItem(user_id=1, name="1 Thessalonians 5:18", description="give thanks in all circumstances; for this is God's will for you in Christ Jesus.",
                     category=category4)

session.add(categoryItem2)
session.commit()


# Category for Forgiveness
category5 = Category(user_id=1, name="Forgiveness")

session.add(category5)
session.commit()


categoryItem1 = CategoryItem(user_id=1, name="Ephesians 1:7", description="In him we have redemption through his blood, the forgiveness of sins, in accordance with the riches of God's grace",
                     category=category5)

session.add(categoryItem1)
session.commit()

categoryItem2 = CategoryItem(user_id=1, name="Psalm 103:12", description="as far as the east is from the west, so far has he removed our transgressionsfrom us.",
                     category=category5)

session.add(categoryItem2)
session.commit()



print "added category items!"
