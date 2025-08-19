class Article:

    all = []

    def __init__(self, author, magazine, title):
        self._magazine = magazine
        self._author = author
        self._title = title

        Article.all.append(self)

    @property
    def title(self):
        return self._title 
    
    @title.setter
    def title(self, value):
        if hasattr(self, "_title") and self._title is not None:
            return
        if isinstance(value, str) and 5 <= len(value) <= 50:
            self._title = value
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            return Exception("Author must be an instance")
        self._author = value

    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            return Exception("Magazine must be an instance")
        self._magazine = value


class Author:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if hasattr(self, "_name") and self._name is not None:
            return
        if isinstance(value, str) and len(value) > 0:
            self._name = value

    def articles(self):
        return [article for article in Article.all if article.author is self]

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
         return Article(self, magazine, title)

    def topic_areas(self):
        magazine = self.magazines()
        if not magazine:
            return None
        return list(set(magazine.category for magazine in self.magazines()))


class Magazine:
    def __init__(self, name, category):
        self._name = name
        self._category = category

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and (2 <= len(value) <= 16):
            self._name = value

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value

    def articles(self):
        return [article for article in Article.all if article.magazine is self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        title = [article.title for article in self.articles()]
        return title if title else None

    def contributing_authors(self):
        authors = [article.author for article in self.articles()]
        contributors = [author for author in set(authors) if authors.count(author) > 2]
        return contributors if contributors else None
    
# authors
author1 = Author("Said")
author2 = Author("Ali")

# magazines
mag1 = Magazine("TechNow", "Technology")
mag2 = Magazine("HealthPlus", "Health")

# ONE TO MANY (one author -> many articles)
author1.add_article(mag1, "The Future of AI")
author1.add_article(mag1, "Quantum Computing Basics")

# MANY TO MANY (many authors <-> many magazines)
author2.add_article(mag1, "AI in Everyday Life")
author2.add_article(mag2, "Mental Wellness")


# One-to-many: one author -> many articles
print("Articles by Said:", [a.title for a in author1.articles()])

# One-to-many: one magazine -> many articles
print("Articles in TechNow:", [a.title for a in mag1.articles()])

# Many-to-many: authors <-> magazines (through Article)
print("Magazines Said has written for:", [m.name for m in author1.magazines()])
print("Contributors in TechNow:", [a.name for a in mag1.contributors()])
