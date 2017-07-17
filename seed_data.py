from app import db, Section, Article

db.drop_all()
db.create_all()

news = Section(name="News", slug="news", description="The news.")
opinions = Section(name="Opinions", slug="opinions", description="The opinions.")

apple = Article(title="Apples Rain in New York City",
                slug="apples-rain-in-newy-york-city",
                content="Apples rain. Oranges do not.",
                datetime=datetime.utcnow(),
                volume=108,
                issue=2,
                isDraft=false,
                section=news)

banana = Article(title="Bananas Fall in Boston: Opinion Piece",
                 slug="bananas-fall-in-boston",
                 content="Bananas fall. Kiwis do not.",
                 datetime=datetime.utcnow(),
                 volume=108,
                 issue=2,
                 isDraft=false,
                 section=opinion)

db.session.add(news)
db.session.add(opinions)
db.session.add(apple)
db.session.add(banana)
db.session.commit()